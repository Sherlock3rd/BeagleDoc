# -*- coding: utf-8 -*-
import os
import io

# 读取 Markdown 文件
md_path = r"d:\charlie\social\docs\beagle_map_gameplay_design.md"
with io.open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# 转义 Markdown 内容以放入 JS 字符串
# 需要转义反引号 ` 和 反斜杠 \
# 在 Python 2 中，read() 返回 unicode，replace 也是 unicode 操作
md_content_js = md_content.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${").replace("</script>", "<\\/script>")

html_template_start = u"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beagle Map Gameplay Design</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
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

        /* Benchmark Cards & Visual Scenes - COMIC STYLE */
        .benchmark-card, .scene-container {
            background: #fff;
            border: 3px solid #333;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            padding: 20px;
            margin: 30px 0;
            box-shadow: 5px 5px 0px rgba(0,0,0,0.2);
            transition: transform 0.2s;
        }
        .benchmark-card:hover, .scene-container:hover {
            box-shadow: 8px 8px 0px rgba(0,0,0,0.2);
        }
        
        /* Typography */
        .container h1, h1 {
            font-family: var(--comic-font);
            border-bottom: 3px solid var(--primary-color);
            padding-bottom: 10px;
            color: var(--primary-color);
            margin-top: 0;
            font-size: 3.5em !important;
        }

        .container h2, h2 {
            font-family: var(--comic-font);
            margin-top: 40px;
            color: var(--primary-color);
            border-left: 8px solid var(--accent-color);
            padding-left: 15px;
            font-size: 2.8em !important;
        }

        .container h3, h3 {
            font-family: var(--comic-font);
            color: var(--accent-color);
            margin-top: 30px;
            font-size: 2.2em !important;
            border-bottom: none;
        }

        .container h4, h4 {
            font-family: var(--comic-font);
            color: #444;
            font-weight: bold;
            margin-top: 20px;
            font-size: 1.6em !important;
        }

        p { margin-bottom: 1em; }
        ul, ol { margin-bottom: 1em; padding-left: 20px; }
        li { margin-bottom: 10px; font-size: 1.1em; }

        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 25px 0;
            font-size: 1.1em;
            font-family: var(--comic-font);
            box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
            border: 2px solid #333;
            border-radius: 4px;
            overflow: hidden;
        }
        th, td {
            padding: 12px 15px;
            border: 1px solid #333;
        }
        th {
            background-color: var(--primary-color);
            color: #fff;
            text-align: left;
            font-size: 1.2em;
        }
        tr:nth-child(even) {
            background-color: #f3f3f3;
        }

        /* Images - Comic Style */
        img {
            max-width: 100%;
            border: 3px solid #333;
            border-radius: 2px;
            margin: 25px 0;
            box-shadow: 5px 5px 0px rgba(0,0,0,0.2);
            display: block;
            transform: rotate(0.5deg);
        }
        img:hover {
            /* No transform */
        }

        /* Custom Boxes - Comic Style */
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
        }
        
        .rule-box {
            background-color: #f0f9ff;
            border: 2px solid #333;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
            position: relative;
        }
        .rule-box::before {
            content: 'RULE';
            position: absolute;
            top: -12px;
            left: 20px;
            background: #333;
            color: #fff;
            padding: 2px 8px;
            font-size: 0.8em;
            font-weight: bold;
            transform: rotate(-2deg);
            font-family: var(--comic-font);
        }
        
        .def-box {
            background-color: #fffbeb;
            border: 2px solid #333;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
            position: relative;
        }
        .def-box::before {
            content: 'DEF';
            position: absolute;
            top: -12px;
            left: 20px;
            background: #333;
            color: #fff;
            padding: 2px 8px;
            font-size: 0.8em;
            font-weight: bold;
            transform: rotate(2deg);
            font-family: var(--comic-font);
        }
        
        .warning {
            background-color: #fff7ed;
            padding: 20px;
            border: 2px solid #333;
            margin: 20px 0;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
            color: #9a3412;
            font-family: var(--comic-font);
            font-weight: bold;
        }

        .highlight {
            background-color: #e8f5e9;
            padding: 2px 5px;
            border-radius: 3px;
            color: #2e7d32;
            font-weight: bold;
            font-family: var(--comic-font);
            border: 1px solid #333;
        }

        .rule-id {
            font-family: var(--comic-font);
            font-weight: bold;
            color: #0366d6;
            background-color: rgba(27,31,35,0.05);
            padding: 2px 4px;
            border-radius: 3px;
            border: 1px solid #ccc;
        }

        code {
            background-color: rgba(27,31,35,0.05);
            padding: 2px 4px;
            border-radius: 3px;
            font-family: monospace;
            color: #e83e8c;
        }

        pre {
            background: #f6f8fa;
            padding: 15px;
            border-radius: 6px;
            overflow-x: auto;
            border: 2px solid #333;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.1);
        }

        /* Tables - Comic Style */
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

        /* Mermaid */
        .mermaid {
            background: white;
            padding: 20px;
            text-align: center;
            margin: 25px 0;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }

        /* Visual Scenes Updates */
        .scene-title {
            font-size: 2.0rem;
            font-weight: bold;
            color: var(--primary-color);
            margin-bottom: 15px;
            text-align: center;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            border-bottom: 3px solid #eee;
            padding-bottom: 10px;
            font-family: var(--comic-font);
        }

        
        /* CP1: Tarkov Style */
        .scene-tarkov .map {
            position: relative;
            height: 220px;
            background-image: radial-gradient(#aaa 1px, transparent 1px);
            background-size: 15px 15px;
            background-color: #f4f4f4;
            border: 3px solid #333;
            border-radius: 2px 5px 2px 5px;
            overflow: hidden;
            box-shadow: inset 5px 5px 0px rgba(0,0,0,0.05);
        }
        .tarkov-entry {
            position: absolute;
            bottom: 10px;
            left: 10px;
            width: 25px;
            height: 25px;
            background: #22c55e;
            border: 3px solid #333;
            border-radius: 50%;
            box-shadow: 2px 2px 0px rgba(0,0,0,0.2);
            animation: pulse 2s infinite;
        }
        .tarkov-exit {
            position: absolute;
            top: 10px;
            right: 10px;
            padding: 5px 10px;
            background: #3b82f6;
            color: white;
            font-size: 14px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 5px;
            border: 3px solid #333;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.2);
            font-family: var(--comic-font);
        }
        .tarkov-loot {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 32px;
            filter: drop-shadow(3px 3px 0px rgba(0,0,0,0.2));
        }
        .tarkov-skull {
            position: absolute;
            font-size: 20px;
            opacity: 0.8;
            filter: grayscale(0%);
        }
        .tarkov-path {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 80%;
            height: 80%;
            transform: translate(-50%, -50%);
            border-top: 4px dashed #94a3b8;
            border-right: 4px dashed #94a3b8;
            border-radius: 0 50px 0 0;
            pointer-events: none;
        }

        /* CP2: PUBG Style */
        .scene-pubg .map {
            position: relative;
            height: 220px;
            background: #ecfdf5; 
            border: 3px solid #333;
            border-radius: 3px;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: inset 5px 5px 0px rgba(0,0,0,0.05);
        }
        .pubg-circle-outer {
            position: absolute;
            width: 180px;
            height: 180px;
            border: 4px solid rgba(239, 68, 68, 0.8);
            border-radius: 50%;
            animation: shrink 4s infinite alternate;
            background: rgba(239, 68, 68, 0.05);
            box-shadow: 0 0 0 2px rgba(0,0,0,0.1);
        }
        .pubg-circle-safe {
            position: absolute;
            width: 60px;
            height: 60px;
            border: 3px solid #fff;
            border-radius: 50%;
            background: rgba(255,255,255,0.4);
            box-shadow: 0 0 0 3px #34d399, 4px 4px 0px rgba(0,0,0,0.1);
        }
        .pubg-airdrop {
            z-index: 10;
            font-size: 36px;
            animation: bounce 1s infinite;
            filter: drop-shadow(4px 4px 0px rgba(0,0,0,0.1));
        }
        .pubg-arrow {
            position: absolute;
            width: 0; 
            height: 0; 
            border-left: 8px solid transparent;
            border-right: 8px solid transparent;
            border-bottom: 16px solid #059669;
            filter: drop-shadow(2px 2px 0px rgba(0,0,0,0.2));
        }

        /* CP3: Arena Style */
        .scene-arena .map {
            position: relative;
            height: 180px;
            background: #f8fafc;
            border: 3px solid #333;
            border-radius: 3px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 30px;
            box-shadow: inset 5px 5px 0px rgba(0,0,0,0.05);
        }
        .arena-zone {
            width: 90px;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            opacity: 0.9;
            font-size: 1rem;
            border: 3px solid transparent;
            font-family: var(--comic-font);
        }
        .arena-blue { background: rgba(59,130,246,0.1); color: #2563eb; border-left: 5px solid #3b82f6; }
        .arena-red { background: rgba(239,68,68,0.1); color: #dc2626; text-align: right; border-right: 5px solid #ef4444; }
        .arena-flag {
            font-size: 48px;
            filter: drop-shadow(4px 4px 0px rgba(0,0,0,0.2));
        }
        .arena-score {
            position: absolute;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: #333;
            color: #fff;
            padding: 5px 15px;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            font-family: var(--comic-font);
            font-weight: bold;
            font-size: 1.2rem;
            box-shadow: 3px 3px 0px rgba(0,0,0,0.3);
            border: 2px solid #000;
        }

        @keyframes pulse { 0% { opacity: 0.5; transform: scale(0.95); } 50% { opacity: 1; transform: scale(1.05); } 100% { opacity: 0.5; transform: scale(0.95); } }
        @keyframes shrink { from { width: 180px; height: 180px; border-width: 4px; } to { width: 80px; height: 80px; border-color: red; border-width: 6px; } }
        @keyframes bounce { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
        @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-5px); } 100% { transform: translateY(0px); } }
        @keyframes dash { to { stroke-dashoffset: -20; } }
        
        .tag {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            font-size: 0.9rem;
            font-weight: 600;
            margin-right: 0.5rem;
            border: 2px solid #333;
            box-shadow: 2px 2px 0px rgba(0,0,0,0.1);
            font-family: var(--comic-font);
        }
        .tag-red { background: #fee2e2; color: #b91c1c; }
        .tag-yellow { background: #fef9c3; color: #a16207; }
        .tag-green { background: #dcfce7; color: #15803d; }

        /* CP4: GVG Style */
        .scene-gvg .map {
            position: relative;
            height: 220px;
            background: #f0fdf4;
            border: 3px solid #333;
            border-radius: 3px;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: inset 5px 5px 0px rgba(0,0,0,0.05);
        }
        .castle {
            font-size: 50px;
            position: absolute;
            z-index: 10;
            filter: drop-shadow(3px 3px 0px rgba(0,0,0,0.2));
        }
        .castle-blue { left: 15%; color: #3b82f6; }
        .castle-red { right: 15%; color: #ef4444; }
        .army-group {
            position: absolute;
            display: flex;
            gap: 3px;
            flex-wrap: wrap;
            width: 80px;
            justify-content: center;
        }
        .army-dot { width: 8px; height: 8px; border-radius: 50%; border: 1px solid #333; }
        .blue-army { left: 25%; top: 50%; }
        .blue-army .army-dot { background: #60a5fa; }
        .red-army { right: 25%; top: 50%; }
        .red-army .army-dot { background: #f87171; }
        .clash-point {
            position: absolute;
            left: 50%; top: 50%;
            transform: translate(-50%, -50%);
            font-size: 40px;
            /* animation: shake 0.5s infinite; */
            filter: drop-shadow(3px 3px 0px rgba(0,0,0,0.2));
        }
        /* @keyframes shake { 0% { transform: translate(-52%, -48%) rotate(-5deg); } 50% { transform: translate(-48%, -52%) rotate(5deg); } 100% { transform: translate(-52%, -48%) rotate(-5deg); } } */

        /* Risk-Reward Spectrum (Comic Theme) */
        .spectrum-container {
            position: relative;
            height: 280px;
            margin: 3rem 0;
            background: #fff;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            padding: 20px;
            border: 3px solid #333;
            box-shadow: 6px 6px 0px rgba(0,0,0,0.2);
        }
        .spectrum-axis {
            position: absolute;
            bottom: 50px;
            left: 5%;
            width: 90%;
            height: 4px;
            background: #333;
            border-radius: 2px;
        }
        .spectrum-axis::after {
            content: '';
            position: absolute;
            right: -12px;
            top: -8px;
            border-left: 15px solid #333;
            border-top: 10px solid transparent;
            border-bottom: 10px solid transparent;
        }
        .spectrum-label {
            position: absolute;
            bottom: 15px;
            font-size: 1.4rem;
            color: #333;
            font-weight: bold;
            font-family: var(--comic-font);
        }
        .label-left { left: 5%; }
        .label-right { right: 5%; }
        
        .spectrum-item {
            position: absolute;
            bottom: 70px;
            transform: translateX(-50%);
            background: #fff;
            border: 3px solid #333;
            padding: 10px 15px;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            text-align: center;
            min-width: 160px;
            /* transition: all 0.3s ease; */
            cursor: default;
            box-shadow: 4px 4px 0px rgba(0,0,0,0.15);
        }
        .spectrum-item:hover {
            box-shadow: 8px 8px 0px rgba(0,0,0,0.2);
            z-index: 10;
        }
        .item-title {
            font-weight: bold;
            color: #333;
            margin-bottom: 4px;
            font-size: 1.5rem;
            font-family: var(--comic-font);
        }
        .item-ref {
            font-size: 0.9rem;
            color: #666;
            font-family: var(--comic-font);
        }
        .item-cp1 { left: 20%; border-color: #333; border-top: 8px solid #22c55e; }
        .item-cp2 { left: 50%; border-color: #333; border-top: 8px solid #eab308; }
        .item-cp3 { left: 80%; border-color: #333; border-top: 8px solid #ef4444; }
        
        .connector-line {
            position: absolute;
            bottom: 50px;
            height: 25px;
            width: 3px;
            background: #333;
            transform: translateX(-50%);
            border-left: 1px dashed #fff; /* Dotted look */
        }

        .flex { display: flex; }
        .justify-between { justify-content: space-between; }
        .items-center { align-items: center; }
        .gap-2 { gap: 0.5rem; }
        .mb-2 { margin-bottom: 0.5rem; }
        .mt-1 { margin-top: 0.25rem; }
        .mt-4 { margin-top: 1rem; }
        .text-xs { font-size: 0.75rem; }
        .text-sm { font-size: 0.875rem; }
        .text-gray-400 { color: #94a3b8; }
        .text-gray-500 { color: #64748b; }
        .font-bold { font-weight: bold; }
        .italic { font-style: italic; }

    </style>
</head>
<body class="p-8">
    <div class="container">
        <div id="content" class="prose mx-auto"></div>
    </div>

    <script type="module">
        const md = `"""

html_template_end = u"""`;
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        
        // Configure Mermaid
        mermaid.initialize({ 
            startOnLoad: false, 
            theme: 'neutral',
            securityLevel: 'loose',
        });
        
        mermaid.parseError = function(err, hash) {
            console.error('Mermaid error:', err);
            const errorDiv = document.createElement('div');
            errorDiv.style.color = 'red';
            errorDiv.style.border = '1px solid red';
            errorDiv.style.padding = '10px';
            errorDiv.textContent = 'Mermaid Syntax Error: ' + err;
            document.body.prepend(errorDiv);
        };

        // Parse Markdown
        document.getElementById('content').innerHTML = marked.parse(md);

        // Transform Mermaid code blocks to div
        // marked renders: <pre><code class="language-mermaid">...</code></pre>
        const mermaidBlocks = document.querySelectorAll('pre code.language-mermaid');
        mermaidBlocks.forEach(block => {
            const pre = block.parentElement;
            const div = document.createElement('div');
            div.className = 'mermaid';
            // Decode HTML entities if necessary, but usually textContent is fine
            div.textContent = block.textContent;
            pre.replaceWith(div);
        });

        // Initialize Mermaid
        try {
            await mermaid.run({
                nodes: document.querySelectorAll('.mermaid')
            });
        } catch (e) {
            console.error('Mermaid run error:', e);
            // Fallback for simple errors
            document.querySelectorAll('.mermaid').forEach(el => {
                if (!el.innerHTML.includes('<svg')) {
                    el.style.border = '1px solid red';
                    el.style.padding = '10px';
                    el.innerHTML += '<br><span style="color:red">Render Error</span>';
                }
            });
        }

        // Function to insert HTML after specific headers
        function insertAfterHeader(headerText, htmlContent) {
            const headers = document.querySelectorAll('h3');
            for (const h of headers) {
                if (h.textContent.includes(headerText)) {
                    const container = document.createElement('div');
                    container.innerHTML = htmlContent;
                    h.parentNode.insertBefore(container, h.nextSibling);
                    return;
                }
            }
        }

        // Common Defs for Stickmen & Icons
        const commonDefs = `
            <defs>
                <!-- Stickman Definition -->
                <g id="stickman">
                    <circle cx="0" cy="-15" r="8" fill="white" stroke="#333" stroke-width="2"/>
                    <line x1="0" y1="-7" x2="0" y2="15" stroke="#333" stroke-width="2"/>
                    <line x1="-10" y1="0" x2="10" y2="0" stroke="#333" stroke-width="2" />
                    <line x1="0" y1="15" x2="-8" y2="30" stroke="#333" stroke-width="2" />
                    <line x1="0" y1="15" x2="8" y2="30" stroke="#333" stroke-width="2" />
                </g>
                <!-- Squad Group (3 Stickmen) -->
                <g id="squad-group">
                    <g transform="translate(0,0)"><use href="#stickman"/></g>
                    <g transform="translate(-15,5) scale(0.9)"><use href="#stickman"/></g>
                    <g transform="translate(15,5) scale(0.9)"><use href="#stickman"/></g>
                </g>
                <!-- Dead Stickman -->
                <g id="stickman-dead">
                    <line x1="-15" y1="25" x2="15" y2="25" stroke="#333" stroke-width="2"/>
                    <line x1="-10" y1="25" x2="-5" y2="15" stroke="#333" stroke-width="2"/> <!-- Leg -->
                    <line x1="5" y1="25" x2="10" y2="15" stroke="#333" stroke-width="2"/> <!-- Leg -->
                    <line x1="-10" y1="10" x2="10" y2="10" stroke="#333" stroke-width="2"/> <!-- Body -->
                    <circle cx="15" cy="10" r="8" fill="white" stroke="#333" stroke-width="2"/>
                    <path d="M 12 7 L 18 13 M 18 7 L 12 13" stroke="#333" stroke-width="2"/> <!-- X Eyes -->
                </g>
                <!-- Running Stickman -->
                <g id="stickman-run">
                    <circle cx="5" cy="-15" r="8" fill="white" stroke="#333" stroke-width="2"/>
                    <line x1="0" y1="-7" x2="-5" y2="10" stroke="#333" stroke-width="2"/> <!-- Body lean -->
                    <line x1="-2" y1="-2" x2="10" y2="-5" stroke="#333" stroke-width="2"/> <!-- Arm F -->
                    <line x1="-2" y1="-2" x2="-10" y2="5" stroke="#333" stroke-width="2"/> <!-- Arm B -->
                    <line x1="-5" y1="10" x2="5" y2="25" stroke="#333" stroke-width="2"/> <!-- Leg F -->
                    <line x1="-5" y1="10" x2="-15" y2="20" stroke="#333" stroke-width="2"/> <!-- Leg B -->
                </g>
                <!-- Pokemon Style Battle Icon -->
                <g id="icon-battle">
                    <path d="M-20,-10 L-5,0 L-20,10 L-10,20 L0,5 L10,20 L20,10 L5,0 L20,-10 L10,-20 L0,-5 L-10,-20 Z" fill="#ef4444" stroke="#333" stroke-width="2"/>
                </g>
                <!-- Loot Box -->
                <g id="icon-loot">
                    <rect x="-15" y="-10" width="30" height="20" fill="#f59e0b" stroke="#333" stroke-width="2" rx="2"/>
                    <rect x="-15" y="-10" width="30" height="6" fill="#fcd34d" stroke="#333" stroke-width="1" rx="2"/>
                    <circle cx="0" cy="0" r="3" fill="#333"/>
                </g>
                <!-- Boss Icon -->
                <g id="icon-boss">
                    <path d="M-20,-20 Q0,-30 20,-20 L25,10 Q0,20 -25,10 Z" fill="#7f1d1d" stroke="#333" stroke-width="2"/>
                    <circle cx="-10" cy="-5" r="4" fill="yellow"/>
                    <circle cx="10" cy="-5" r="4" fill="yellow"/>
                    <path d="M-15,5 Q0,0 15,5" stroke="white" stroke-width="2" fill="none"/>
                    <path d="M-22,-15 L-28,-25 M22,-15 L28,-25" stroke="#333" stroke-width="3"/> <!-- Horns -->
                </g>
                <!-- Map Markers -->
                <marker id="arrowSimple" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto">
                    <path d="M0,0 L0,6 L9,3 z" fill="#333" />
                </marker>
                <marker id="arrowRed" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto">
                    <path d="M0,0 L0,6 L9,3 z" fill="#ef4444" />
                </marker>
            </defs>
        `;

        // CP1 Visual - Stickman Arena
        const cp1Html = `
            <div class="scene-container scene-arena">
                <div class="scene-title">CP1: 自由搏击俱乐部</div>
                <div class="flex justify-between text-xs mb-2 text-gray-400">
                    <span class="font-bold text-green-600">SAFE ZONE</span>
                    <span class="font-bold text-red-600">ALLIANCE vs SOLOS</span>
                </div>
                <svg viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border:3px solid #333; border-radius:4px; width:100%; height:auto;">
                    ${commonDefs}
                    
                    <!-- Background Zones -->
                    <rect x="0" y="0" width="160" height="250" fill="#dcfce7" opacity="0.5"/> <!-- Safe Zone -->
                    <rect x="160" y="0" width="640" height="250" fill="#fee2e2" opacity="0.3"/> <!-- PvP Zone -->
                    <line x1="160" y1="0" x2="160" y2="250" stroke="#333" stroke-width="2" stroke-dasharray="5 5">
                        <animate attributeName="stroke-dashoffset" from="10" to="0" dur="1s" repeatCount="indefinite"/>
                    </line>
                    
                    <!-- Entry Point -->
                    <text x="80" y="30" text-anchor="middle" fill="#15803d" font-weight="bold" font-family="Comic Sans MS">ENTER</text>
                    <g transform="translate(80, 100)">
                        <use href="#stickman"/>
                        <text x="0" y="-25" text-anchor="middle" font-size="10" fill="#15803d">Solo</text>
                        <animateTransform attributeName="transform" type="translate" values="50,100; 120,100" dur="2s" repeatCount="indefinite"/>
                        <animate attributeName="opacity" values="0;1;0" dur="2s" repeatCount="indefinite"/>
                    </g>
                    
                    <!-- The Arena Fight (Alliance vs Zerg) -->
                    <g transform="translate(480, 125)">
                        <!-- Floor -->
                        <ellipse cx="0" cy="50" rx="250" ry="60" fill="#e2e8f0" stroke="#333" stroke-width="2"/>
                        
                        <!-- Center Objective: Fun/Chaos -->
                        <text x="0" y="-80" text-anchor="middle" font-size="24" fill="#ef4444">👑</text>
                        <text x="0" y="-60" text-anchor="middle" font-size="12" font-weight="bold" fill="#ef4444">CHAOS KING</text>

                        <!-- The Alliance (Blue Team) - Organized -->
                        <g transform="translate(-20, 20)">
                            <animateTransform attributeName="transform" type="translate" values="-20,20; -20,15; -20,20" dur="4s" repeatCount="indefinite"/>
                            <ellipse cx="0" cy="0" rx="60" ry="20" fill="#3b82f6" opacity="0.2">
                                <animate attributeName="rx" values="60;65;60" dur="2s" repeatCount="indefinite"/>
                                <animate attributeName="ry" values="20;25;20" dur="2s" repeatCount="indefinite"/>
                                <animate attributeName="opacity" values="0.2;0.4;0.2" dur="2s" repeatCount="indefinite"/>
                            </ellipse>
                            <ellipse cx="0" cy="0" rx="60" ry="20" fill="#bfdbfe" opacity="0.5"/>
                            <text x="0" y="-45" text-anchor="middle" font-weight="bold" fill="#1e40af" font-size="10">ALLIANCE</text>
                            <!-- Defender 1 -->
                            <g transform="translate(0, -10)">
                                <use href="#stickman"/>
                            </g>
                            <!-- Defender 2 -->
                            <g transform="translate(-30, 0)">
                                <use href="#stickman"/>
                            </g>
                            <!-- Defender 3 -->
                            <g transform="translate(30, 0)">
                                <use href="#stickman"/>
                            </g>
                        </g>

                        <!-- The Solos (Red/Green) - Chaotic Attackers -->
                        <g>
                             <!-- Attacker 1 (Left) -->
                            <g transform="translate(-100, 30)">
                                <use href="#stickman-run"/>
                                <text x="0" y="-25" text-anchor="middle" fill="#dc2626" font-size="12">Solo</text>
                            </g>
                            <!-- Attacker 2 (Right) -->
                            <g transform="translate(100, 30) scale(-1,1)">
                                <use href="#stickman-run"/>
                            </g>
                             <!-- Attacker 3 (Back Left) -->
                            <g transform="translate(-80, -20) scale(0.9)">
                                <use href="#stickman-run"/>
                            </g>
                            <!-- Attacker 4 (Front Right) -->
                            <g transform="translate(80, 50) scale(-1.1, 1.1)">
                                <use href="#stickman-run"/>
                                <text x="0" y="-25" text-anchor="middle" fill="#dc2626" font-size="12" transform="scale(-1,1)">Solo</text>
                            </g>
                        </g>
                        
                        <!-- Fight Cloud Animation -->
                        <path d="M-50,-20 Q-70,-40 -50,-60 Q0,-80 50,-60 Q70,-40 50,-20 Q0,0 -50,-20" fill="#fca5a5" stroke="#ef4444" stroke-width="2" opacity="0.5">
                             <animate attributeName="opacity" values="0.5;0.7;0.5" dur="1s" repeatCount="indefinite"/>
                             <animate attributeName="fill" values="#fca5a5;#fecaca;#fca5a5" dur="0.5s" repeatCount="indefinite"/>
                        </path>
                        
                        <text x="0" y="90" text-anchor="middle" font-size="16" font-style="italic" fill="#64748b">"Alliance Hold vs Solo Rush"</text>
                        
                        <!-- Hot Time Event Indicator -->
                        <g transform="translate(720, 30)">
                            <circle cx="0" cy="0" r="20" fill="#fbbf24" stroke="#d97706" stroke-width="2">
                                 <animate attributeName="r" values="20;22;20" dur="1s" repeatCount="indefinite"/>
                                 <animate attributeName="stroke-opacity" values="1;0.5;1" dur="1s" repeatCount="indefinite"/>
                            </circle>
                            <text x="0" y="5" text-anchor="middle" font-size="18" font-weight="bold" fill="#78350f">2X</text>
                            <text x="0" y="28" text-anchor="middle" font-size="14" font-weight="bold" fill="#d97706">EVENT</text>
                        </g>
                    </g>
                </svg>
                <div class="mt-3 p-3 bg-green-50 border-l-4 border-green-400 text-sm">
                    <div class="font-bold mb-1 text-green-800">🎯 CP1 设计定位: GVG 前置练兵场</div>
                    <ul class="list-disc list-inside text-green-700 space-y-1">
                        <li><strong>常驻开启 (Always On):</strong> 随时进场练习，磨合队伍配合。</li>
                        <li><strong>定时爆发 (Hot Hours):</strong> 每日指定时段(如20:00-21:00)开启<span class="font-bold text-red-500">双倍收益</span>，强制聚拢全服玩家进行高强度对抗。</li>
                        <li><strong>低损耗 (Low Loss):</strong> 相比 GVG 的残酷淘汰，这里仅消耗装备耐久，是公会选拔新人的最佳场所。</li>
                    </ul>
                </div>
                <div class="mt-4 flex justify-between items-center text-sm">
                    <div class="flex items-center gap-2">
                        <span class="tag tag-green">Safe Entry</span>
                        <span class="tag tag-red">Team vs Horde</span>
                    </div>
                    <div class="text-gray-400 italic">Target: Break the Alliance</div>
                </div>
            </div>
        `;

        // CP2 Visual - Stickman Battle Royale
        const cp2Html = `
            <div class="scene-container scene-pubg">
                <div class="scene-title">CP2: 幸运流星 - 趣味乱斗</div>
                <div class="flex justify-between text-xs mb-2 text-gray-400">
                    <span class="font-bold text-green-600">SAFE ZONE</span>
                    <span class="font-bold text-yellow-600">MASSIVE SOLO SCRAMBLE</span>
                </div>
                <svg viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg" style="background:#ecfdf5; border:3px solid #333; border-radius:4px; width:100%; height:auto;">
                    ${commonDefs}
                    
                    <!-- Background Zones -->
                    <rect x="0" y="0" width="120" height="250" fill="#dcfce7" opacity="0.5"/>
                    <line x1="120" y1="0" x2="120" y2="250" stroke="#333" stroke-width="2" stroke-dasharray="5 5"/>
                    
                    <!-- Safe Entry -->
                    <g transform="translate(60, 125)">
                        <use href="#stickman-run"/>
                        <animateTransform attributeName="transform" type="translate" values="20,125; 100,125" dur="1.5s" repeatCount="indefinite"/>
                        <animate attributeName="opacity" values="0;1;0" dur="1.5s" repeatCount="indefinite"/>
                    </g>

                    <!-- The Zone -->
                    <g transform="translate(460, 125)">
                        <!-- Shrinking Circle -->
                        <circle cx="0" cy="0" r="110" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="10 5" opacity="0.3">
                            <animate attributeName="r" values="110; 80; 50" dur="4s" repeatCount="indefinite"/>
                            <animate attributeName="stroke-opacity" values="0.3; 0.8; 1" dur="4s" repeatCount="indefinite"/>
                        </circle>
                        
                        <!-- The Loot (Objective) -->
                        <g>
                             <!-- Glow behind -->
                            <circle cx="0" cy="0" r="20" fill="#fcd34d" opacity="0.5">
                                <animate attributeName="opacity" values="0.2;0.6;0.2" dur="1s" repeatCount="indefinite"/>
                                <animate attributeName="r" values="20;25;20" dur="1s" repeatCount="indefinite"/>
                            </circle>
                            <use href="#icon-loot" transform="scale(1.5)"/>
                            <animateTransform attributeName="transform" type="translate" values="0,-5; 0,5; 0,-5" dur="2s" repeatCount="indefinite"/>
                        </g>
                        <text x="0" y="-30" text-anchor="middle" font-weight="bold" fill="#d97706" font-size="16">AIRDROP</text>

                        <!-- Players Rushing (The Crowd) -->
                        <!-- Left Side Mob -->
                        <g transform="translate(-80, 40)">
                            <use href="#stickman-run"/>
                            <text x="0" y="35" text-anchor="middle" font-size="10">Mine!</text>
                        </g>
                        <g transform="translate(-100, 10) scale(0.9)">
                            <use href="#stickman-run"/>
                        </g>
                        <g transform="translate(-90, 60) scale(1.1)">
                            <use href="#stickman-run"/>
                        </g>

                        <!-- Right Side Mob -->
                        <g transform="translate(80, -20) scale(-1,1)">
                            <use href="#stickman-run"/>
                        </g>
                        <g transform="translate(110, 0) scale(-0.9, 0.9)">
                            <use href="#stickman-run"/>
                        </g>
                         <g transform="translate(100, -40) scale(-1.1, 1.1)">
                            <use href="#stickman-run"/>
                        </g>
                        
                        <!-- Conflict -->
                        <path d="M -40 30 L 0 0" stroke="#ef4444" stroke-width="1" stroke-dasharray="2 2"/>
                        <path d="M 40 -10 L 0 0" stroke="#ef4444" stroke-width="1" stroke-dasharray="2 2"/>
                    </g>
                    
                    <text x="460" y="230" text-anchor="middle" fill="#ef4444" font-family="Comic Sans MS" font-size="14">"Everyone Rush Center!"</text>
                </svg>
                <div class="mt-4 flex justify-between items-center text-sm">
                    <div class="flex items-center gap-2">
                        <span class="tag tag-yellow">Dynamic Zone</span>
                        <span class="tag tag-yellow">Massive Brawl</span>
                    </div>
                    <div class="text-gray-400 italic">Objective: Rare Loot Box</div>
                </div>
            </div>
        `;

        // CP3 Visual - Stickman Extraction
        const cp3Html = `
            <div class="scene-container scene-tarkov">
                <div class="scene-title">CP3: 遗物猎杀 - 绝境撤离</div>
                <div class="flex justify-between text-xs mb-2 text-gray-400">
                    <span class="font-bold text-green-600">SAFE BASE</span>
                    <span class="font-bold text-red-600 flex-1 text-center">HIGH DANGER ZONE (SQUADS)</span>
                    <span class="font-bold text-green-600">EXTRACTION</span>
                </div>
                <svg viewBox="0 0 800 250" xmlns="http://www.w3.org/2000/svg" style="background:#f0fdf4; border:3px solid #333; border-radius:4px; width:100%; height:auto;">
                    ${commonDefs}
                    
                    <!-- Background Zones -->
                    <rect x="0" y="0" width="100" height="250" fill="#dcfce7" opacity="0.5"/> <!-- Safe -->
                    <rect x="700" y="0" width="100" height="250" fill="#dcfce7" opacity="0.5"/> <!-- Extract -->
                    
                    <!-- Step 1: Entry -->
                    <g transform="translate(50, 125)">
                        <use href="#squad-group"/>
                        <text x="0" y="45" text-anchor="middle" fill="#15803d" font-size="16" font-weight="bold">SQUAD</text>
                        <animateTransform attributeName="transform" type="translate" values="20,125; 80,125" dur="3s" repeatCount="indefinite"/>
                        <animate attributeName="opacity" values="0;1;0" dur="3s" repeatCount="indefinite"/>
                    </g>
                    
                    <!-- Path Arrow -->
                    <path d="M 120 125 L 180 125" stroke="#333" stroke-width="3" marker-end="url(#arrowSimple)" stroke-dasharray="10 5">
                        <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite"/>
                    </path>

                    <!-- Step 2: Boss Fight -->
                    <g transform="translate(250, 125)">
                        <use href="#icon-boss" transform="scale(1.5)"/>
                        <text x="0" y="-35" text-anchor="middle" fill="#dc2626" font-weight="bold" font-size="12">KILL BOSS</text>
                        <!-- Fighting Squad -->
                        <g transform="translate(-40, 30) scale(0.8)">
                            <use href="#squad-group"/>
                        </g>
                        <path d="M -20 20 L 0 0" stroke="#f59e0b" stroke-width="2"/>
                    </g>

                    <!-- Path Arrow -->
                    <path d="M 320 125 L 380 125" stroke="#333" stroke-width="3" marker-end="url(#arrowSimple)" stroke-dasharray="10 5">
                        <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite"/>
                    </path>

                    <!-- Step 3: Signal & Defend -->
                    <g transform="translate(450, 125)">
                        <!-- Signal Tower -->
                        <line x1="0" y1="20" x2="0" y2="-40" stroke="#d97706" stroke-width="4"/>
                        <circle cx="0" cy="-40" r="5" fill="#f59e0b"/>
                        <circle cx="0" cy="-40" r="30" stroke="#f59e0b" stroke-width="2" fill="none" opacity="0.5">
                            <animate attributeName="r" values="10;40" dur="1s" repeatCount="indefinite"/>
                            <animate attributeName="opacity" values="1;0" dur="1s" repeatCount="indefinite"/>
                        </circle>
                        <text x="0" y="-60" text-anchor="middle" fill="#d97706" font-weight="bold" font-size="12">SIGNAL (5m)</text>
                        
                        <!-- Defending Squad -->
                        <g transform="translate(0, 30) scale(0.8)">
                            <use href="#squad-group"/>
                            <rect x="-25" y="-15" width="50" height="40" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 3" rx="10"/>
                        </g>
                        
                        <!-- Enemy Interruption -->
                        <g transform="translate(50, 0) scale(-0.7, 0.7)">
                            <use href="#squad-group" opacity="0.7"/>
                        </g>
                        <text x="50" y="-20" text-anchor="middle" fill="#dc2626" font-size="10">Enemy Squad</text>
                    </g>

                    <!-- Path Arrow -->
                    <path d="M 520 125 L 680 125" stroke="#333" stroke-width="3" marker-end="url(#arrowSimple)" stroke-dasharray="10 5">
                        <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite"/>
                    </path>

                    <!-- Step 4: Extract -->
                    <g transform="translate(750, 125)">
                        <!-- Rotor -->
                        <line x1="-30" y1="-10" x2="30" y2="-10" stroke="#333" stroke-width="2">
                             <animateTransform attributeName="transform" type="rotate" from="0 0 -10" to="360 0 -10" dur="0.2s" repeatCount="indefinite"/>
                        </line>
                        <path d="M-20,0 L20,0 L15,15 L-15,15 Z" fill="#15803d" stroke="none"/> <!-- Heli pad -->
                        <text x="0" y="-20" text-anchor="middle" fill="#15803d" font-weight="bold" font-size="12">EXTRACT</text>
                        <g transform="translate(0, 10) scale(0.8)">
                            <use href="#squad-group"/>
                            <use href="#icon-loot" transform="translate(0, -25)"/> <!-- Carrying loot -->
                        </g>
                    </g>
                </svg>
                <div class="mt-4 flex justify-between items-center text-sm">
                    <div class="flex items-center gap-2">
                        <span class="tag tag-red">Squad vs Squad</span>
                        <span class="tag tag-red">Boss & Signal</span>
                    </div>
                    <div class="text-gray-400 italic">Objective: Relic (Full Loot)</div>
                </div>
            </div>
        `;

        // Benchmark Visuals - Stickman Style
        const benchmark1Html = `
            <div class="scene-container scene-arena">
                <div class="scene-title">Benchmark 1: 阵营对抗</div>
                <div class="text-sm text-gray-500 italic mb-4 text-center">"双方阵营在固定地图内进行大规模混战，争夺资源点或击杀数"</div>
                <svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg" style="background:#f0f9ff; border:3px solid #333; border-radius:4px; width:100%; height:auto;">
                    ${commonDefs}
                    
                    <!-- Blue Army -->
                    <g transform="translate(200, 100)">
                        <animateTransform attributeName="transform" type="translate" values="200,100; 210,100; 200,100" dur="2s" repeatCount="indefinite"/>
                        <rect x="-80" y="-60" width="160" height="120" fill="#bfdbfe" rx="10" opacity="0.5"/>
                        <g transform="translate(-40, 0)"><use href="#stickman"/></g>
                        <g transform="translate(0, 20)"><use href="#stickman"/></g>
                        <g transform="translate(40, 0)"><use href="#stickman"/></g>
                        <g transform="translate(0, -20)"><use href="#stickman"/></g>
                        <text x="0" y="-70" text-anchor="middle" fill="#1e40af" font-weight="bold" font-size="20">BLUE ARMY</text>
                    </g>
                    
                    <!-- VS -->
                    <text x="400" y="100" text-anchor="middle" font-size="40" font-weight="bold" fill="#333">
                        VS
                        <animate attributeName="font-size" values="40;48;40" dur="1s" repeatCount="indefinite"/>
                        <animate attributeName="fill" values="#333;#ef4444;#333" dur="1s" repeatCount="indefinite"/>
                    </text>
                    
                    <!-- Red Army -->
                    <g transform="translate(600, 100)">
                        <animateTransform attributeName="transform" type="translate" values="600,100; 590,100; 600,100" dur="2s" repeatCount="indefinite"/>
                        <rect x="-80" y="-60" width="160" height="120" fill="#fecaca" rx="10" opacity="0.5"/>
                        <g transform="translate(-40, 0)"><use href="#stickman"/></g>
                        <g transform="translate(0, 20)"><use href="#stickman"/></g>
                        <g transform="translate(40, 0)"><use href="#stickman"/></g>
                        <g transform="translate(0, -20)"><use href="#stickman"/></g>
                        <text x="0" y="-70" text-anchor="middle" fill="#991b1b" font-weight="bold" font-size="20">RED ARMY</text>
                    </g>
                </svg>
                <div class="mt-3 p-3 bg-blue-50 border-l-4 border-blue-400 text-sm">
                    <div class="font-bold mb-1 text-blue-800">🎮 核心定位: "带收益的实战训练场"</div>
                    <ul class="list-disc list-inside text-blue-700 space-y-1">
                        <li><strong>像训练场:</strong> 0风险，无限复活，随便试错，适合练枪/练连招。</li>
                        <li><strong>不像训练场:</strong> <span class="font-bold text-red-500">有丰厚奖励！</span> 击杀和占点会产出核心代币，是普通玩家"养家糊口"的主要途径。</li>
                    </ul>
                </div>
                <div class="mt-4 flex justify-between items-center text-sm">
                    <div class="flex items-center gap-2">
                        <span class="tag tag-green">WoW BG</span>
                        <span class="tag tag-green">Albion Yellow</span>
                    </div>
                    <div class="text-gray-400 italic">"Structured PvP"</div>
                </div>
            </div>
        `;

        const benchmark2Html = `
            <div class="scene-container scene-pubg">
                <div class="scene-title">Benchmark 2: 缩圈与争夺</div>
                <div class="text-sm text-gray-500 italic mb-4 text-center">"流程: 跳伞落地 -> 搜集物资 -> 躲避毒圈 -> 决战圈胜出"</div>
                <svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg" style="background:#fffbeb; border:3px solid #333; border-radius:4px; width:100%; height:auto;">
                    ${commonDefs}
                    
                    <!-- Plane -->
                    <g transform="translate(100, 40)">
                        <animateTransform attributeName="transform" type="translate" values="50,40; 750,40" dur="5s" repeatCount="indefinite"/>
                        <path d="M0,0 L40,-10 L50,0 L10,10 Z" fill="#64748b"/>
                        <line x1="0" y1="0" x2="-100" y2="0" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5 5"/>
                        <text x="25" y="-15" text-anchor="middle" font-size="10" fill="#64748b">Drop</text>
                    </g>

                    <!-- Zone Shrink -->
                    <g transform="translate(400, 100)">
                        <rect x="-150" y="-80" width="300" height="160" fill="none" stroke="#fcd34d" stroke-width="2" stroke-dasharray="5 5"/>
                        <circle cx="0" cy="0" r="60" fill="none" stroke="#ef4444" stroke-width="2">
                            <animate attributeName="r" values="60; 40; 20" dur="3s" repeatCount="indefinite"/>
                            <animate attributeName="stroke-opacity" values="1;0.5;1" dur="3s" repeatCount="indefinite"/>
                        </circle>
                        <text x="0" y="80" text-anchor="middle" font-size="10" fill="#ef4444">Zone Shrink</text>
                        
                        <!-- Loot Center -->
                        <use href="#icon-loot">
                            <animateTransform attributeName="transform" type="scale" values="1;1.2;1" dur="1s" repeatCount="indefinite"/>
                        </use>
                    </g>
                    
                    <!-- Running In -->
                    <g transform="translate(200, 120)">
                         <use href="#stickman-run"/>
                    </g>
                    <g transform="translate(600, 120) scale(-1,1)">
                         <use href="#stickman-run"/>
                    </g>
                </svg>
                <div class="mt-4 flex justify-between items-center text-sm">
                    <div class="flex items-center gap-2">
                        <span class="tag tag-yellow">PUBG</span>
                        <span class="tag tag-yellow">Division</span>
                    </div>
                    <div class="text-gray-400 italic">"Survival & Loot"</div>
                </div>
            </div>
        `;

        const benchmark3Html = `
            <div class="scene-container scene-tarkov">
                <div class="scene-title">Benchmark 3: 潜入与撤离</div>
                <div class="text-sm text-gray-400 italic mb-4 text-center">"核心: 带入装备 -> 潜入高危区搜刮 -> 活着撤离 (死亡全掉落)"</div>
                <svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg" style="background:#18181b; border:3px solid #333; border-radius:4px; width:100%; height:auto;">
                    ${commonDefs}
                    
                    <!-- Background Grid -->
                    <path d="M0,100 L800,100" stroke="#333" stroke-width="2"/>
                    
                    <!-- Entry -->
                    <g transform="translate(100, 100)">
                        <rect x="-40" y="-60" width="80" height="120" fill="#1f2937" stroke="#374151" stroke-width="2"/>
                        <text x="0" y="-70" text-anchor="middle" fill="#9ca3af" font-size="12">SPAWN</text>
                        <use href="#stickman" stroke="white"/>
                    </g>
                    
                    <!-- Risk Zone -->
                    <g transform="translate(400, 100)">
                        <circle cx="0" cy="0" r="80" fill="#7f1d1d" opacity="0.3">
                            <animate attributeName="r" values="80;85;80" dur="2s" repeatCount="indefinite"/>
                            <animate attributeName="opacity" values="0.3;0.5;0.3" dur="2s" repeatCount="indefinite"/>
                        </circle>
                        <use href="#icon-boss" transform="scale(1.2)"/>
                        <text x="0" y="-50" text-anchor="middle" fill="#ef4444" font-weight="bold">HIGH RISK</text>
                        <text x="0" y="50" text-anchor="middle" fill="#fcd34d" font-weight="bold">HIGH REWARD</text>
                    </g>
                    
                    <!-- Exit -->
                    <g transform="translate(700, 100)">
                        <rect x="-40" y="-60" width="80" height="120" fill="#064e3b" stroke="#059669" stroke-width="2"/>
                        <text x="0" y="-70" text-anchor="middle" fill="#34d399" font-size="12">EXTRACT</text>
                        <g transform="translate(0, 0)">
                             <use href="#stickman" stroke="white"/>
                             <use href="#icon-loot" transform="translate(0, -25) scale(0.8)"/>
                        </g>
                    </g>
                    
                    <!-- Arrows -->
                    <path d="M150,100 L300,100" stroke="#6b7280" stroke-width="2" marker-end="url(#arrowSimple)" stroke-dasharray="10 5">
                        <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite"/>
                    </path>
                    <path d="M500,100 L650,100" stroke="#6b7280" stroke-width="2" marker-end="url(#arrowSimple)" stroke-dasharray="10 5">
                        <animate attributeName="stroke-dashoffset" from="30" to="0" dur="1s" repeatCount="indefinite"/>
                    </path>
                </svg>
                <div class="mt-4 flex justify-between items-center text-sm">
                    <div class="flex items-center gap-2">
                        <span class="tag tag-red">Tarkov</span>
                        <span class="tag tag-red">Albion Black</span>
                    </div>
                    <div class="text-gray-400 italic">"Full Loot PvP"</div>
                </div>
            </div>
        `;

        const benchmark4Html = `
            <div class="scene-container scene-gvg">
                <div class="scene-title">Benchmark 4: 大型公会战</div>
                <div class="text-sm text-gray-500 italic mb-4 text-center">"核心: 以公会为单位，通过策略与指挥争夺领土/城堡控制权"</div>
                <svg viewBox="0 0 800 200" xmlns="http://www.w3.org/2000/svg" style="background:#f0fdf4; border:3px solid #333; border-radius:4px; width:100%; height:auto;">
                    ${commonDefs}
                    
                    <!-- Blue Castle -->
                    <g transform="translate(150, 120)">
                        <path d="M-60,0 L-60,-80 L-20,-80 L-20,-60 L20,-60 L20,-80 L60,-80 L60,0 Z" fill="#bfdbfe" stroke="#1e40af" stroke-width="3"/>
                        <rect x="-20" y="-40" width="40" height="40" fill="#60a5fa"/>
                        <text x="0" y="-90" text-anchor="middle" fill="#1e40af" font-weight="bold">GUILD A</text>
                        <!-- Defenders -->
                        <g transform="translate(-40, 0)"><use href="#stickman"/></g>
                        <g transform="translate(40, 0)"><use href="#stickman"/></g>
                        <!-- Arrows firing -->
                        <path d="M20,-40 Q100,-100 180,-20" fill="none" stroke="#1e40af" stroke-width="2" stroke-dasharray="5 5">
                            <animate attributeName="stroke-dashoffset" from="20" to="0" dur="1s" repeatCount="indefinite"/>
                        </path>
                    </g>
                    
                    <!-- Clash Point -->
                    <g transform="translate(400, 120)">
                        <text x="0" y="-50" text-anchor="middle" font-size="30">⚔️</text>
                        <animateTransform attributeName="transform" type="scale" values="1;1.2;1" dur="1s" repeatCount="indefinite"/>
                        <text x="0" y="-20" text-anchor="middle" fill="#d97706" font-weight="bold">TERRITORY WAR</text>
                    </g>
                    
                    <!-- Red Castle -->
                    <g transform="translate(650, 120)">
                         <path d="M-60,0 L-60,-80 L-20,-80 L-20,-60 L20,-60 L20,-80 L60,-80 L60,0 Z" fill="#fecaca" stroke="#991b1b" stroke-width="3"/>
                        <rect x="-20" y="-40" width="40" height="40" fill="#f87171"/>
                        <text x="0" y="-90" text-anchor="middle" fill="#991b1b" font-weight="bold">GUILD B</text>
                        <!-- Defenders -->
                        <g transform="translate(-40, 0)"><use href="#stickman"/></g>
                        <g transform="translate(40, 0)"><use href="#stickman"/></g>
                         <!-- Arrows firing -->
                        <path d="M-20,-40 Q-100,-100 -180,-20" fill="none" stroke="#991b1b" stroke-width="2" stroke-dasharray="5 5">
                            <animate attributeName="stroke-dashoffset" from="20" to="0" dur="1s" repeatCount="indefinite"/>
                        </path>
                    </g>
                </svg>
                <div class="mt-4 flex justify-between items-center text-sm">
                    <div class="flex items-center gap-2">
                        <span class="tag tag-yellow">ROK</span>
                        <span class="tag tag-yellow">GW2 WvW</span>
                    </div>
                    <div class="text-gray-400 italic">"Strategic Conquest"</div>
                </div>
            </div>
        `;

        // Spectrum Visual - Benchmark
        const spectrumBenchmarkHtml = `
            <div class="spectrum-container">
                <div class="spectrum-axis"></div>
                
                <div class="spectrum-label label-left">Low Risk/Reward<br><span class="text-xs font-normal opacity-70">(Safe)</span></div>
                <div class="spectrum-label label-right text-right">High Risk/Reward<br><span class="text-xs font-normal opacity-70">(Full Loot)</span></div>

                <div class="connector-line" style="left: 20%"></div>
                <div class="spectrum-item item-cp1">
                    <div class="item-title text-green-600">Benchmark 1</div>
                    <div class="item-ref font-bold">WoW / Albion Yellow</div>
                    <div class="mt-1 text-xs text-green-600">No Loot Loss</div>
                </div>

                <div class="connector-line" style="left: 50%"></div>
                <div class="spectrum-item item-cp2">
                    <div class="item-title text-yellow-600">Benchmark 2</div>
                    <div class="item-ref font-bold">PUBG / Division</div>
                    <div class="mt-1 text-xs text-yellow-600">Partial Loot</div>
                </div>

                <div class="connector-line" style="left: 80%"></div>
                <div class="spectrum-item item-cp3">
                    <div class="item-title text-red-600">Benchmark 3</div>
                    <div class="item-ref font-bold">Tarkov / Albion Black</div>
                    <div class="mt-1 text-xs text-red-600">Full Loot</div>
                </div>
            </div>
        `;

        // Spectrum Visual - CP
        const spectrumCPHtml = `
            <div class="spectrum-container">
                <div class="spectrum-axis"></div>
                
                <div class="spectrum-label label-left">Low Risk/Reward<br><span class="text-xs font-normal opacity-70">(Safe)</span></div>
                <div class="spectrum-label label-right text-right">High Risk/Reward<br><span class="text-xs font-normal opacity-70">(Full Loot)</span></div>

                <div class="connector-line" style="left: 20%"></div>
                <div class="spectrum-item item-cp1">
                    <div class="item-title text-green-500">CP1: Fight Club</div>
                    <div class="item-ref">Sport & Fun</div>
                    <div class="mt-1 text-xs text-green-600">No Loot Loss</div>
                </div>

                <div class="connector-line" style="left: 50%"></div>
                <div class="spectrum-item item-cp2">
                    <div class="item-title text-yellow-500">CP2: Hotspot</div>
                    <div class="item-ref">Adrenaline Rush</div>
                    <div class="mt-1 text-xs text-yellow-600">Partial Loot</div>
                </div>

                <div class="connector-line" style="left: 80%"></div>
                <div class="spectrum-item item-cp3">
                    <div class="item-title text-red-500">CP3: Extraction</div>
                    <div class="item-ref">High Stakes</div>
                    <div class="mt-1 text-xs text-red-600">Full Loot</div>
                </div>
            </div>
        `;

        // Pyramid Visual
        const pyramidHtml = `
            <div class="scene-container">
                <div class="scene-title">Evolution Pyramid</div>
                <div class="text-sm text-gray-500 italic mb-4 text-center">"从泛用户基础到核心硬核追求的金字塔结构"</div>
                <svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" style="background:#fff; border:3px solid #333; border-radius:4px; width:100%; height:auto;">
                    ${commonDefs}
                    
                    <!-- Axes -->
                    <!-- Left: Audience Size -->
                    <g transform="translate(50, 200)">
                         <text x="-20" y="0" transform="rotate(-90)" text-anchor="middle" font-weight="bold" fill="#64748b">Audience Size (DAU)</text>
                         <path d="M10,150 L10,-150" stroke="#64748b" stroke-width="2" marker-end="url(#arrowSimple)"/>
                         <!-- Arrow Down Custom -->
                         <path d="M10,150 L5,140 M10,150 L15,140" stroke="#64748b" stroke-width="2" fill="none"/> 
                    </g>
                    
                    <!-- Right: Risk/Reward -->
                    <g transform="translate(750, 200)">
                         <text x="20" y="0" transform="rotate(-90)" text-anchor="middle" font-weight="bold" fill="#ef4444">Risk / Complexity</text>
                         <path d="M-10,150 L-10,-150" stroke="#ef4444" stroke-width="2" marker-end="url(#arrowRed)"/>
                    </g>

                    <!-- Pyramid Levels -->
                    
                    <!-- Level 1: CP1 (Bottom) -->
                    <g transform="translate(400, 320)">
                        <path d="M-300,50 L300,50 L250,-50 L-250,-50 Z" fill="#dcfce7" stroke="#16a34a" stroke-width="3"/>
                        <text x="0" y="10" text-anchor="middle" font-size="24" font-weight="bold" fill="#15803d">CP1: 自由搏击俱乐部</text>
                        <text x="0" y="35" text-anchor="middle" font-size="14" fill="#15803d">Foundation / Safe / Always On</text>
                        
                        <!-- Crowd of Stickmen -->
                        <g transform="translate(-200, 20) scale(0.8)"><use href="#stickman"/></g>
                        <g transform="translate(-150, 20) scale(0.8)"><use href="#stickman"/></g>
                        <g transform="translate(-100, 20) scale(0.8)"><use href="#stickman"/></g>
                        <g transform="translate(100, 20) scale(0.8)"><use href="#stickman"/></g>
                        <g transform="translate(150, 20) scale(0.8)"><use href="#stickman"/></g>
                        <g transform="translate(200, 20) scale(0.8)"><use href="#stickman"/></g>
                        
                        <!-- 7-Day Tag -->
                        <g transform="translate(280, 0) rotate(-10)">
                            <rect x="-40" y="-15" width="80" height="30" fill="#2563eb" rx="5" stroke="#333" stroke-width="2"/>
                            <text x="0" y="5" text-anchor="middle" fill="white" font-weight="bold" font-size="12">7-DAY GOAL</text>
                        </g>
                    </g>
                    
                    <!-- Level 2: CP2 (Middle) -->
                    <g transform="translate(400, 210)">
                        <path d="M-240,50 L240,50 L180,-50 L-180,-50 Z" fill="#fef9c3" stroke="#ca8a04" stroke-width="3"/>
                        <text x="0" y="10" text-anchor="middle" font-size="24" font-weight="bold" fill="#854d0e">CP2: 幸运流星</text>
                        <text x="0" y="35" text-anchor="middle" font-size="14" fill="#854d0e">Aggregation / Events / Fun</text>
                        
                         <!-- Running Stickmen -->
                        <g transform="translate(-120, 20) scale(0.8)"><use href="#stickman-run"/></g>
                        <g transform="translate(120, 20) scale(-0.8, 0.8)"><use href="#stickman-run"/></g>
                    </g>
                    
                    <!-- Level 3: CP3 (Top) -->
                    <g transform="translate(400, 100)">
                        <path d="M-170,50 L170,50 L100,-50 L-100,-50 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="3"/>
                        <text x="0" y="10" text-anchor="middle" font-size="24" font-weight="bold" fill="#991b1b">CP3: 遗物猎杀</text>
                        <text x="0" y="35" text-anchor="middle" font-size="14" fill="#991b1b">Hardcore / High Risk / Economy</text>
                        
                        <!-- Boss Icon -->
                        <g transform="translate(0, -20) scale(0.8)"><use href="#icon-boss"/></g>
                        
                        <!-- Future Tag -->
                        <g transform="translate(180, 0) rotate(10)">
                            <rect x="-40" y="-15" width="80" height="30" fill="#9ca3af" rx="5" stroke="#333" stroke-width="2"/>
                            <text x="0" y="5" text-anchor="middle" fill="white" font-weight="bold" font-size="12">FUTURE</text>
                        </g>
                    </g>
                    
                </svg>
            </div>
        `;

        // Replace placeholder
        const contentDiv = document.getElementById('content');
        
        // Handle Pyramid Visual
        if (contentDiv.innerHTML.includes('&lt;!-- PYRAMID_VISUALIZATION --&gt;')) {
            contentDiv.innerHTML = contentDiv.innerHTML.replace('&lt;!-- PYRAMID_VISUALIZATION --&gt;', pyramidHtml);
        } else if (contentDiv.innerHTML.includes('<!-- PYRAMID_VISUALIZATION -->')) {
            contentDiv.innerHTML = contentDiv.innerHTML.replace('<!-- PYRAMID_VISUALIZATION -->', pyramidHtml);
        }
        
        // Handle Benchmarks Spectrum
        if (contentDiv.innerHTML.includes('&lt;!-- SPECTRUM_VISUALIZATION_BENCHMARK --&gt;')) {
            contentDiv.innerHTML = contentDiv.innerHTML.replace('&lt;!-- SPECTRUM_VISUALIZATION_BENCHMARK --&gt;', spectrumBenchmarkHtml);
        } else if (contentDiv.innerHTML.includes('<!-- SPECTRUM_VISUALIZATION_BENCHMARK -->')) {
            contentDiv.innerHTML = contentDiv.innerHTML.replace('<!-- SPECTRUM_VISUALIZATION_BENCHMARK -->', spectrumBenchmarkHtml);
        }

        // Handle CP Spectrum
        if (contentDiv.innerHTML.includes('&lt;!-- SPECTRUM_VISUALIZATION_CP --&gt;')) {
            contentDiv.innerHTML = contentDiv.innerHTML.replace('&lt;!-- SPECTRUM_VISUALIZATION_CP --&gt;', spectrumCPHtml);
        } else if (contentDiv.innerHTML.includes('<!-- SPECTRUM_VISUALIZATION_CP -->')) {
            contentDiv.innerHTML = contentDiv.innerHTML.replace('<!-- SPECTRUM_VISUALIZATION_CP -->', spectrumCPHtml);
        }

        // Handle Benchmark Visuals
        const benchmarkVisuals = {
            'BENCHMARK_VISUAL_1': benchmark1Html,
            'BENCHMARK_VISUAL_2': benchmark2Html,
            'BENCHMARK_VISUAL_3': benchmark3Html,
            'BENCHMARK_VISUAL_4': benchmark4Html
        };

        for (const [placeholder, html] of Object.entries(benchmarkVisuals)) {
            const safePlaceholder = '&lt;!-- ' + placeholder + ' --&gt;';
            const rawPlaceholder = '<!-- ' + placeholder + ' -->';
            
            if (contentDiv.innerHTML.includes(safePlaceholder)) {
                contentDiv.innerHTML = contentDiv.innerHTML.replace(safePlaceholder, html);
            } else if (contentDiv.innerHTML.includes(rawPlaceholder)) {
                contentDiv.innerHTML = contentDiv.innerHTML.replace(rawPlaceholder, html);
            }
        }
        
        // Handle Legacy/Fallback (just in case)
        if (contentDiv.innerHTML.includes('&lt;!-- SPECTRUM_VISUALIZATION --&gt;')) {
            contentDiv.innerHTML = contentDiv.innerHTML.replace('&lt;!-- SPECTRUM_VISUALIZATION --&gt;', spectrumBenchmarkHtml);
        } else if (contentDiv.innerHTML.includes('<!-- SPECTRUM_VISUALIZATION -->')) {
            contentDiv.innerHTML = contentDiv.innerHTML.replace('<!-- SPECTRUM_VISUALIZATION -->', spectrumBenchmarkHtml);
        }
        // Handle CP Visuals
        const cpVisuals = {
            'CP_VISUAL_1': cp1Html,
            'CP_VISUAL_2': cp2Html,
            'CP_VISUAL_3': cp3Html
        };

        for (const [placeholder, html] of Object.entries(cpVisuals)) {
            const safePlaceholder = '&lt;!-- ' + placeholder + ' --&gt;';
            const rawPlaceholder = '<!-- ' + placeholder + ' -->';
            
            if (contentDiv.innerHTML.includes(safePlaceholder)) {
                contentDiv.innerHTML = contentDiv.innerHTML.replace(safePlaceholder, html);
            } else if (contentDiv.innerHTML.includes(rawPlaceholder)) {
                contentDiv.innerHTML = contentDiv.innerHTML.replace(rawPlaceholder, html);
            }
        }
        
        // insertAfterHeader('CP1: 混乱荒原', cp1Html); // Removed legacy injection
        // insertAfterHeader('CP2: 信号争夺', cp2Html); // Removed legacy injection
        // insertAfterHeader('CP3: 荣耀竞技场', cp3Html); // Removed legacy injection

    </script>
</body>
</html>
"""

final_html = html_template_start + md_content_js + html_template_end

output_path = r"d:\charlie\social\docs\beagle_map_gameplay_design.html"
with io.open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Generated HTML at: " + output_path)
