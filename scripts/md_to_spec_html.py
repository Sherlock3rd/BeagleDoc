#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io
import sys
import argparse

def build_html(md_text, title):
    if sys.version_info[0] < 3:
        try:
            if isinstance(title, str):
                enc = sys.getfilesystemencoding() or 'utf-8'
                title = title.decode(enc, 'ignore')
        except Exception:
            pass
    md_content_js = (
        md_text.replace("\\", "\\\\")
        .replace("`", "\\`")
        .replace("${", "\\${")
        .replace("</script>", "<\\/script>")
    )

    html_head = u"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{TITLE}}</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

        :root {
            --primary-color: #2c3e50;
            --accent-color: #3498db;
            --bg-color: #fdfbf7;
            --text-color: #333;
            --border-color: #333;
            --comic-font: 'Patrick Hand', cursive, sans-serif;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            font-size: 18px;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 20px;
            background-image: radial-gradient(#e5e5e5 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 2px;
            border: 2px solid #333;
            box-shadow: 8px 8px 0px rgba(0,0,0,0.1);
        }
        h1 {
            font-family: var(--comic-font);
            border-bottom: 3px solid var(--primary-color);
            padding-bottom: 10px;
            color: var(--primary-color);
            margin-top: 0;
            font-size: 3.5em !important;
            text-align: center;
        }
        h2 {
            font-family: var(--comic-font);
            margin-top: 40px;
            color: var(--primary-color);
            border-left: 8px solid var(--accent-color);
            padding-left: 15px;
            font-size: 2.2em !important;
        }
        h3 {
            font-family: var(--comic-font);
            color: var(--accent-color);
            margin-top: 30px;
            font-size: 1.6em !important;
        }
        h4 {
            font-family: var(--comic-font);
            color: #444;
            font-weight: bold;
            margin-top: 20px;
            font-size: 1.3em !important;
        }
        p { margin-bottom: 1em; }
        ul, ol { margin-bottom: 1em; padding-left: 20px; }
        li { margin-bottom: 10px; font-size: 1.05em; }
        table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin: 25px 0;
            border: 2px solid #333;
            border-radius: 4px;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        th, td {
            border-bottom: 2px solid #333;
            border-right: 2px solid #333;
            padding: 10px 15px;
            text-align: left;
            font-family: var(--comic-font);
        }
        th:last-child, td:last-child { border-right: none; }
        tr:last-child td { border-bottom: none; }
        th {
            background-color: #e2e8f0;
            color: #333;
            font-weight: bold;
            font-size: 1.1em;
            text-transform: uppercase;
        }
        tr:nth-child(even) { background-color: #f8fafc; }
        blockquote {
            background-color: #fff3e0;
            border-left: 5px solid #333;
            border: 2px solid #333;
            border-left-width: 8px;
            margin: 20px 0;
            padding: 15px;
            color: #444;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
            font-family: var(--comic-font);
            font-size: 1.2em;
            font-style: italic;
        }
        .highlight-box {
            background-color: #e3f2fd;
            border: 2px solid #333;
            border-radius: 15px 225px 15px 255px / 255px 15px 225px 15px;
            padding: 20px;
            margin: 20px 0;
        }
        .scene-container {
            background: #fff;
            border: 3px solid #333;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            padding: 20px;
            margin: 30px 0;
            box-shadow: 5px 5px 0px rgba(0,0,0,0.2);
        }
        .visual-scene {
            position: relative;
            width: 100%;
            max-width: 800px;
            margin: 0 auto;
        }
        svg { display: block; width: 100%; height: 100%; }
        .sketch-line { fill: none; stroke: #333; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
        .sketch-fill { fill: #fff; stroke: #333; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
        .sketch-title { font-family: 'Patrick Hand', cursive; font-size: 20px; font-weight: bold; fill: #333; text-anchor: middle; }
        .sketch-text { font-family: 'Patrick Hand', cursive; font-size: 16px; fill: #333; text-anchor: middle; }
        .mermaid { background: #fff; border: 2px solid #333; border-radius: 10px; padding: 15px; margin: 20px 0; }
    </style>
</head>
<body>
<div class="container">
    <h1>{{TITLE}}</h1>
    <div id="content"></div>
</div>
<script>
const md = `{{MD}}`;
document.getElementById('content').innerHTML = marked.parse(md);

// Mermaid: transform <pre><code class="language-mermaid">...</code></pre> to <div class="mermaid">...</div>
document.querySelectorAll('pre code.language-mermaid').forEach(code => {
  const pre = code.parentElement;
  const container = document.createElement('div');
  container.className = 'mermaid';
  container.textContent = code.textContent;
  pre.replaceWith(container);
});
mermaid.initialize({ startOnLoad: true, securityLevel: 'loose' });

// Auto Visuals: insert a simple SVG callout after long sections
function insertAutoVisuals() {
  const headers = Array.from(document.querySelectorAll('#content h2'));
  for (let i = 0; i < headers.length; i++) {
    const h = headers[i];
    let chars = 0;
    let cursor = h.nextElementSibling;
    while (cursor && cursor.tagName !== 'H2' && cursor.tagName !== 'H1') {
      chars += (cursor.innerText || '').length;
      cursor = cursor.nextElementSibling;
    }
    if (chars > 400) {
      const scene = document.createElement('div');
      scene.className = 'scene-container';
      scene.innerHTML = `
        <div class="visual-scene">
          <svg viewBox="0 0 600 160">
            <defs>
              <g id="marker">
                <rect x="-60" y="-20" width="120" height="40" class="sketch-fill" style="fill:#e3f2fd"/>
                <text x="0" y="5" class="sketch-title">图示说明</text>
              </g>
            </defs>
            <g transform="translate(300,40)"><use href="#marker"/></g>
            <text x="300" y="100" class="sketch-text">${h.innerText}</text>
          </svg>
        </div>
      `;
      h.insertAdjacentElement('afterend', scene);
    }
  }
}
insertAutoVisuals();
</script>
</body>
</html>"""

    html_head = html_head.replace(u"{{TITLE}}", title)
    html_head = html_head.replace(u"{{MD}}", md_content_js)
    return html_head

def main():
    parser = argparse.ArgumentParser(description="将 Markdown 生成符合发布规范的 HTML（对标 publish/pvp_tile_detailed_design.html）")
    parser.add_argument("--input", "-i", required=True, help="输入 Markdown 文件路径")
    parser.add_argument("--output", "-o", required=True, help="输出 HTML 文件路径")
    parser.add_argument("--title", "-t", required=False, default="Spec 文档", help="HTML 页面标题与主标题")
    args = parser.parse_args()

    in_path = os.path.abspath(args.input)
    out_path = os.path.abspath(args.output)
    if not os.path.exists(in_path):
        raise RuntimeError("输入文件不存在: {}".format(in_path))

    with io.open(in_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # 过滤规则：移除内部管理或补充说明性质的章节（如第8章及以后的内部规划与索引内容）
    # 这里通过正则匹配常见的内部章节标题，或直接截断到特定章节
    import re
    # 查找“## 8. CP 发散方法总结”或类似内部章节作为截断点
    cutoff_match = re.search(r'\n## 8\. .+', md_text)
    if cutoff_match:
        md_text = md_text[:cutoff_match.start()]

    html = build_html(md_text, args.title)

    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir)
    with io.open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

if __name__ == "__main__":
    main()
