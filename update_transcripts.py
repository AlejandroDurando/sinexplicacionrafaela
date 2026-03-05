import os
import re

base_dir = "/Users/alejandodurando/Desktop/SER"

def update_html_transcription(html_file, txt_file, end_marker):
    html_path = os.path.join(base_dir, html_file)
    txt_path = os.path.join(base_dir, txt_file)

    # Read txt file
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        with open(txt_path, 'r', encoding='utf-16le') as f:
            lines = f.readlines()

    transcription_html = ""
    for line in lines:
        line = line.strip()
        if not line: continue
        if ":" in line:
            speaker, text = line.split(":", 1)
            transcription_html += f"                                <p><strong>{speaker}:</strong>{text}</p>\n"
        else:
            transcription_html += f"                                <p>{line}</p>\n"

    # Read html
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the transcription section
    start_marker = "<h3>[ TRANSCRIPCIÓN OFICIAL ]</h3>"
    
    start_idx = html.find(start_marker)
    if start_idx == -1:
        print(f"Start marker not found in {html_file}")
        return
    start_idx += len(start_marker)

    end_idx = html.find(end_marker)
    if end_idx == -1:
        print(f"End marker not found in {html_file}")
        return

    # Replace
    new_html = html[:start_idx] + "\n\n" + transcription_html + "            " + html[end_idx:]

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Updated {html_file}")


update_html_transcription("grabacion_5.html", "assets/Casos/Caso Ignacio Pieruccioni /Transcripcion_entrevista_Ignacio.txt", "</div>\n\n            \n        </section>")
