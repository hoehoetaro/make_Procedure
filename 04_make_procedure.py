import csv
import os
from html import escape

# Change the working directory to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Initialize the HTML components
title = None
thumbnail_path = None
body = ''

# Initialize the procedure links section
body += '<div class="div-procedure-links">\n'
body += '<h2>Procedure Links</h2>\n'
body += '<ol>\n'

# CSVファイルを読み込む
procedures = []
procedure_content = ''
procedure_counter = 1
with open('HTML_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        command = row[0]
        content = row[1]

        if command == 'title':
            title = content
            body += f'<h1>{title}</h1>\n'  # Add title to body here
        elif command == 'thumbnail':
            thumbnail_path = content
            if os.path.exists(thumbnail_path):
                body += f'<div class="div-img"><img src="{escape(thumbnail_path)}" alt="Image"></div>\n'
        elif command == 'procedure':
            if procedure_content:  # If there was a previous procedure, append it
                procedures.append((procedure_heading, procedure_content))
                procedure_content = ''
            procedure_heading = f'{procedure_counter}. {content}'  # Set the new heading with number
            body += f'<li><a href="#{escape(procedure_heading)}">{escape(procedure_heading)}</a></li>\n'
            procedure_counter += 1
        elif command == 'description':
            # Replace the newline character with <br> for paragraphs
            content = content.replace('\n', '<br>')
            procedure_content += f'<p>{content}</p>\n'
        elif command == 'img':
            procedure_content += f'<div class="div-img"><img src="{escape(content)}" alt="Image"></div>\n'
        elif command == 'video':
            procedure_content += f'<div class="div-video"><video controls onmouseover="this.play()" onmouseout="this.pause();">\n<source src="{escape(content)}" type="video/mp4">\nYour browser does not support the video tag.\n</video></div>\n'
        elif command == 'code':
            procedure_content += f'<div class="div-code code-container"><button onclick="copyToClipboard(\'codeBlock\')">Copy to clipboard</button>\n<pre id="codeBlock"><code>{escape(content)}</code></pre></div>\n'

if procedure_content:  # Append the last procedure
    procedures.append((procedure_heading, procedure_content))

body += '</ol>\n'
body += '</div>\n'  # Close div-procedure-links

# Add each procedure to the body
for heading, content in procedures:
    body += f'<div class="div-procedure" id="{escape(heading)}">\n'
    body += f'<h3>{escape(heading)}</h3>\n'
    body += content
    body += '</div>\n'  # Close div-procedure

# HTMLを出力
output_filename = os.path.basename(os.getcwd()) + '.html'
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <script>
    function copyToClipboard(elementId) {{
        var aux = document.createElement("textarea");
        aux.innerHTML = document.getElementById(elementId).textContent;
        document.body.appendChild(aux);
        aux.select();
        document.execCommand("copy");
        document.body.removeChild(aux);
    }}
    </script>
</head>
<body>
{body}
</body>
</html>""")
