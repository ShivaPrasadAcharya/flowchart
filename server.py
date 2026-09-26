#!/usr/bin/env python3
"""Serve the chart page and keep its inputs/ folder available to the browser."""
import argparse
import json
import os
from pathlib import Path
import tempfile
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit
import webbrowser

ROOT = Path(__file__).resolve().parent
INPUTS = ROOT / "inputs"
MAX_FILE = 2 * 1024 * 1024
INPUTS.mkdir(exist_ok=True)


def valid_name(value):
    return (
        isinstance(value, str)
        and value.lower().endswith(".txt")
        and value.lower() != ".txt"
        and value == Path(value).name
        and "/" not in value
        and "\\" not in value
        and "\0" not in value
    )


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def _json(self, status, payload):
        raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):
        if urlsplit(self.path).path != "/api/inputs":
            return super().do_GET()
        files = []
        for path in sorted(INPUTS.iterdir(), key=lambda p: p.name.casefold()):
            if not path.is_file() or path.is_symlink() or not valid_name(path.name):
                continue
            try:
                if path.stat().st_size > MAX_FILE:
                    continue
                files.append({
                    "name": path.name,
                    "text": path.read_text(encoding="utf-8-sig"),
                    "mtime": str(path.stat().st_mtime_ns),
                })
            except (OSError, UnicodeError):
                continue
        self._json(200, {"app": "branchline", "files": files})

    def do_POST(self):
        if urlsplit(self.path).path != "/api/inputs":
            return self._json(404, {"error": "Unknown endpoint"})
        port = self.server.server_port
        origin = self.headers.get("Origin")
        if origin and origin not in {f"http://127.0.0.1:{port}", f"http://localhost:{port}"}:
            return self._json(403, {"error": "Origin not allowed"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= MAX_FILE + 4096:
                return self._json(413, {"error": "Text file is too large"})
            value = json.loads(self.rfile.read(length))
            name, text = value.get("name"), value.get("text")
            if not valid_name(name) or not isinstance(text, str):
                return self._json(400, {"error": "A .txt file name and text are required"})
            raw = text.encode("utf-8")
            if len(raw) > MAX_FILE:
                return self._json(413, {"error": "Text file is too large"})
            target = INPUTS / name
            if target.is_symlink():
                return self._json(400, {"error": "File name is not allowed"})
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(dir=INPUTS, prefix=".new-", delete=False) as stream:
                    temporary = Path(stream.name)
                    stream.write(raw)
                os.replace(temporary, target)
            finally:
                if temporary and temporary.exists():
                    temporary.unlink()
            return self._json(200, {"saved": name})
        except (ValueError, OSError, UnicodeError, TypeError):
            return self._json(400, {"error": "Could not save text file"})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
        address = f"http://127.0.0.1:{server.server_port}/index.html"
        print(f"Branchline is ready: {address}", flush=True)
        print("Keep this window open while editing. Press Ctrl+C to stop.", flush=True)
        if not args.no_browser:
            threading.Timer(0.5, lambda: webbrowser.open(address)).start()
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
