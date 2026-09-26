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

The input editor soft-wraps long lines without changing the .txt file. Type
/n at the desired position within an item or note to force a new chart line.
Under Customize, Text wrap can use Automatic + /n or Manual /n only. The
Chart width / screen setting defaults to 7:10: automatic text fits within
about seven tenths of the chart viewport width, including in full screen.

Select text in the input and use the B, I, U buttons or Ctrl/Cmd+B, I, U.
These insert **bold**, *italic*, and __underline__ text markers in the .txt
file, and the chart displays the formatting. Text before an arrow (→ or ->)
always appears bold in the configurable Text before arrow color. The text
after the arrow uses only the formatting selected in the input. Capitalized
words (including YES and NO) elsewhere retain their ordinary appearance.
When a long statement follows an arrow, wrapped lines align below the start
of the statement, not below the arrow or its preceding label.

Add a line such as Caption: **My chart** anywhere in a .txt input to display
that text in the chart. The caption supports B, I, U markers and /n breaks;
Customize lets you place it above or below the chart and set its alignment,
size, and color. The caption is included in image, SVG, and DOCX exports.

Use the copy icons to copy input text or all visible charts as one PNG image.
A green tick briefly confirms success. If image clipboard access is
unavailable, Copy chart copies its visible text instead. Neither copy mode
adds the input file name to the output. The DOCX download
exports the current chart as paginated, high-resolution images in a Word
document, preserving connectors, dashes, dots, and text appearance.
