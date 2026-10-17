# CATopalian_PY_Build_HTML_App.pyw

import os

def build_complete_html_with_titles():
    # project folder setup
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.join(base_dir, "src")
    css_dir = os.path.join(src_dir, "css")
    js_dir = os.path.join(src_dir, "js")
    index_html = os.path.join(base_dir, "index.html")

    # grab everything from top of index.html through </title>
    header_lines = []
    with open(index_html, "r", encoding="utf-8") as f:
        inside_title = False
        for line in f:
            header_lines.append(line)
            if "<title" in line:
                inside_title = True
            if inside_title and "</title>" in line:
                break

    # ensure newline after </title> block
    if not header_lines[-1].endswith("\n"):
        header_lines[-1] = header_lines[-1] + "\n"
    header_lines.append("\n")

    # read css
    css_content = ""
    css_file = os.path.join(css_dir, "style001.css")
    if os.path.exists(css_file):
        with open(css_file, "r", encoding="utf-8") as f:
            css_content = f.read()

    # read js files with titles inserted
    js_content = ""
    for folder, _, files in os.walk(js_dir):
        files.sort()
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(folder, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    js_content += "// " + file + "\n"
                    js_content += f.read().strip() + "\n\n"

    # build final HTML
    output_html = "".join(header_lines)

    if css_content:
        output_html += "<style>\n" + css_content + "\n</style>\n\n"

    if js_content:
        output_html += "<script>\n" + js_content + "</script>\n\n"

    # close head AFTER styles & scripts
    output_html += "</head>\n"

    # open body with onload, then close at the end
    output_html += "<body onload=\"whenLoaded()\">\n"
    output_html += "</body>\n</html>"

    # write to file
    out_name = "complete_" + os.path.basename(index_html)
    out_path = os.path.join(base_dir, out_name)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_html)

    print("✅ html with file titles generated:", out_name)

if __name__ == "__main__":
    build_complete_html_with_titles()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

