BRANCHLINE CHARTS

Windows: Extract the ZIP, then double-click Start_Charts.bat.
Mac/Linux: Run sh Start_Charts.sh from the extracted folder.
Python 3 is required. Keep the launcher window open while using the page.
In a browser that supports folder access, you can also open index.html
directly and click Choose inputs folder. Select the extracted inputs folder.
The page checks the selected folder while it remains open.

Place any UTF-8 .txt file directly in the inputs folder. The Files dropdown
checks that folder every four seconds. When ALL is selected, newly added
files are selected automatically and their charts appear on the page.
Removing a .txt file removes it from the dropdown on the next refresh.
The Refresh inputs button checks immediately.

Click Edit beside a file to change its chart text and its individual
continuous, dashed, or dotted line style, colors, origin, and spacing.
Click Save to inputs to write edited text back to that .txt file.
Open .txt files can add or replace several files in inputs at once.

For static website hosting without the launcher, add each new .txt filename
to inputs/files.json, or paste inputs/your-file.txt into Add file link.
The link option is remembered in that browser. Updating files.json makes
the list available to everyone viewing the hosted page.

index.html contains no embedded chart text. It reads the .txt files in inputs
through the launcher, a selected local folder, or the hosted files.json list.
Opening index.html directly shows no charts until you choose inputs. Adding
new files or changing existing text then updates the corresponding charts.
Click SEE TEXT above a chart to open its file in the initially hidden input
panel. Use Hide input panel to collapse it completely again.
