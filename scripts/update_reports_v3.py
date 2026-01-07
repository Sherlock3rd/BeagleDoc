# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import io
import math

# ---------------------------------------------------------
# HTML TEMPLATE
# ---------------------------------------------------------
TEMPLATE = u"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>社交竞品拆解: {title}</title>
    <style>
        :root {{
            --primary-bg: #f0f2f5;
            --card-bg: #ffffff;
            --text-main: #2c3e50;
            --text-secondary: #7f8c8d;
            --accent-color: {accent_color};
            --accent-secondary: {accent_secondary};
            --danger-color: #e74c3c;
            --warning-color: #f39c12;
            --border-radius: 12px;
            --shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--primary-bg);
            color: var(--text-main);
            line-height: 1.6;
            margin: 0;
            padding: 40px 20px;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}

        /* Header Section */
        header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        
        .game-logo-placeholder {{
            width: 80px;
            height: 80px;
            background: var(--accent-color);
            border-radius: 20px;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            font-size: 32px;
            box-shadow: var(--shadow);
        }}

        h1 {{ margin: 0; font-size: 2.5em; color: var(--text-main); }}
        .subtitle {{ color: var(--text-secondary); font-size: 1.1em; margin-top: 10px; }}
        
        .tag-container {{
            margin-top: 15px;
            display: flex;
            justify-content: center;
            gap: 10px;
        }}
        
        .tag {{
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.9em;
            font-weight: 600;
        }}
        
        .tag-model {{ background: #e8f8f5; color: var(--accent-color); border: 1px solid var(--accent-color); }}
        .tag-type {{ background: #eaf2f8; color: var(--accent-secondary); border: 1px solid var(--accent-secondary); }}

        /* Grid Layout */
        .grid-2 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 30px;
        }}

        .grid-3 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}

        /* Cards */
        .card {{
            background: var(--card-bg);
            border-radius: var(--border-radius);
            padding: 25px;
            box-shadow: var(--shadow);
            transition: transform 0.2s;
            margin-bottom: 30px;
        }}
        
        .card:hover {{
            transform: translateY(-2px);
        }}

        h2 {{
            border-left: 4px solid var(--accent-color);
            padding-left: 15px;
            margin-top: 0;
            color: var(--text-main);
            font-size: 1.4em;
        }}

        h3 {{
            color: var(--accent-secondary);
            margin-top: 0;
            font-size: 1.1em;
            border-bottom: 1px dashed #eee;
            padding-bottom: 10px;
        }}

        /* Chart Components */
        .bar-group {{
            margin-bottom: 15px;
        }}
        
        .bar-label {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 5px;
            font-size: 0.9em;
            font-weight: 600;
        }}
        
        .bar-track {{
            height: 10px;
            background: #f0f2f5;
            border-radius: 5px;
            overflow: hidden;
        }}
        
        .bar-fill {{
            height: 100%;
            border-radius: 5px;
            background: var(--accent-color);
            width: 0;
            transition: width 1s ease-out;
        }}
        
        .icon-check {{ color: var(--accent-color); margin-right: 8px; }}
        .icon-cross {{ color: var(--danger-color); margin-right: 8px; }}

        /* Analysis Box */
        .analysis-box {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-size: 0.9em;
            color: #666;
            border-left: 3px solid #ddd;
        }}
        .analysis-title {{
            font-weight: bold;
            color: #555;
            margin-bottom: 5px;
            display: block;
        }}

        /* Persona Table */
        .persona-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9em;
        }}
        .persona-table th {{
            text-align: left;
            padding: 10px;
            background: #f0f2f5;
            color: #2c3e50;
        }}
        .persona-table td {{
            padding: 10px;
            border-bottom: 1px solid #eee;
        }}
        .focus-badge {{
            background: var(--accent-color);
            color: white;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.8em;
            margin-left: 5px;
        }}

        /* Takeaways */
        .takeaway-section {{
            display: flex;
            gap: 20px;
        }}
        
        .takeaway-col {{
            flex: 1;
            padding: 20px;
            border-radius: var(--border-radius);
        }}
        
        .col-do {{ background: #e8f8f5; border: 1px solid var(--accent-color); }}
        .col-dont {{ background: #fdedec; border: 1px solid var(--danger-color); }}
        
        .col-title {{
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }}
        
        ul {{ margin: 0; padding-left: 20px; }}
        li {{ margin-bottom: 8px; }}

        /* Responsive */
        @media (max-width: 768px) {{
            .grid-2, .grid-3, .takeaway-section {{
                grid-template-columns: 1fr;
                flex-direction: column;
            }}
        }}
    </style>
</head>
<body>

    <div class="container">
        <!-- Navigation -->
        <nav style="margin-bottom: 20px;">
            <a href="../social_analysis_index.html" style="text-decoration: none; color: #7f8c8d; font-weight: bold; font-size: 0.9em;">
                ← 返回竞品分析汇总 (Back to Index)
            </a>
        </nav>

        <!-- Header -->
        <header>
            <div class="game-logo-placeholder">{logo_text}</div>
            <h1>{title}</h1>
            <div class="subtitle">{subtitle}</div>
            <div class="tag-container">
                {tags_html}
            </div>
        </header>

        <!-- 0. Context -->
        <section style="margin-bottom: 30px; background: #fff8e1; padding: 20px; border-radius: 12px; border-left: 4px solid #f1c40f;">
            <h3 style="color: #d35400; margin-top: 0; border: none;">🎯 为什么选择 {title} 作为 Beagle 的参考？</h3>
            <p style="margin: 0; color: #5d4037; font-size: 0.95em;">
                Beagle 面临着与 {title} 极其相似的挑战：<strong>{context_challenge}</strong>
                <br><br>
                本报告将沿着以下脉络展开：
                <br>1. <strong>定性：</strong> 社交模型概览 (Model)；
                <br>2. <strong>定量：</strong> 社交维度权重分析 (Dimensions)；
                <br>3. <strong>落地：</strong> 核心系统与体验还原 (Systems)；
                <br>4. <strong>评估：</strong> 压力模型 (Pressure)；
                <br>5. <strong>画像：</strong> 用户分层 (Persona)；
                <br>6. <strong>结论：</strong> 对 Beagle 的关键启示 (Takeaways)。
            </p>
        </section>

        <!-- 1. Model Overview -->
        <section class="card" style="margin-bottom: 30px;">
            <h2>1. 社交模型概览 (Model Overview)</h2>
            <div class="grid-3" style="margin-bottom: 0; margin-top: 20px;">
                <!-- Basic 3 -->
                {model_basic_3}
                
                <!-- Interaction Nature -->
                <div>
                    <strong style="color: var(--text-secondary);">交互性质 (合作 vs 竞争)</strong>
                    <div style="margin-top: 8px;">
                        <div style="display:flex; justify-content:space-between; font-size:0.8em; color:#666; margin-bottom:4px;">
                            <span>竞争</span>
                            <strong style="color:var(--accent-color);">{inter_text}</strong>
                            <span>合作</span>
                        </div>
                        <div style="height:8px; background:#eee; border-radius:4px; position:relative;">
                            <div style="width:100%; height:100%; background:linear-gradient(90deg, #eee 0%, #eee {inter_pos_start}%, var(--accent-color) {inter_pos_end}%); border-radius:4px;"></div>
                            <div style="position:absolute; top:-3px; left:{inter_percent}%; width:14px; height:14px; background:#fff; border:2px solid var(--accent-color); border-radius:50%; transform:translateX(-50%);"></div>
                        </div>
                    </div>
                    <p style="font-size: 0.85em; color: #666; margin-top: 8px;">{inter_desc}</p>
                </div>

                <!-- Social Necessity -->
                <div>
                    <strong style="color: var(--text-secondary);">社交必要性 (可选 vs 强制)</strong>
                    <div style="margin-top: 8px;">
                        <div style="display:flex; justify-content:space-between; font-size:0.8em; color:#666; margin-bottom:4px;">
                            <span>可选</span>
                            <strong style="color:var(--warning-color);">{nece_text}</strong>
                            <span>强制</span>
                        </div>
                        <div style="height:8px; background:#eee; border-radius:4px; position:relative;">
                            <div style="width:100%; height:100%; background:linear-gradient(90deg, #eee 0%, var(--warning-color) {nece_percent}%, #eee 100%); border-radius:4px;"></div>
                            <div style="position:absolute; top:-3px; left:{nece_percent}%; width:14px; height:14px; background:#fff; border:2px solid var(--warning-color); border-radius:50%; transform:translateX(-50%);"></div>
                        </div>
                    </div>
                    <p style="font-size: 0.85em; color: #666; margin-top: 8px;">{nece_desc}</p>
                </div>
            </div>
        </section>

        <!-- Context Connector 1 -->
        <div style="margin: -20px 0 20px 0; text-align: center; color: #7f8c8d; font-size: 0.9em; font-style: italic;">
            ⬇ 为了实现这种“{model_keyword}”的顶层设计，资源和注意力是如何在各个维度上分配的？
        </div>

        <!-- 2. Dimensions -->
        <section class="card" style="margin-bottom: 30px;">
            <h2>2. 社交维度权重分析 (4 Dimensions & Weights)</h2>
            <div class="grid-2" style="margin-bottom: 0;">
                <!-- Who -->
                <div style="background: #f8f9fa; padding: 20px; border-radius: 8px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                        <h3 style="border:none; margin:0; padding:0; color:#3498db;">👥 社交对象 (Who)</h3>
                        <span style="background:#d6eaf8; color:#2980b9; font-size:0.75em; padding:2px 8px; border-radius:10px; font-weight:bold;">{dim_who_tag}</span>
                    </div>
                    <!-- Fixed Categories: Stranger, Acquaintance, AI-NPC -->
                    {dim_who_content}
                    <div class="analysis-box">
                        <span class="analysis-title">🧐 逻辑与权衡：</span>
                        {dim_who_reasoning}
                    </div>
                </div>

                <!-- Why -->
                <div style="background: #f8f9fa; padding: 20px; border-radius: 8px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                        <h3 style="border:none; margin:0; padding:0; color:#9b59b6;">🔥 社交动机 (Why)</h3>
                        <span style="background:#f4ecf7; color:#8e44ad; font-size:0.75em; padding:2px 8px; border-radius:10px; font-weight:bold;">{dim_why_tag}</span>
                    </div>
                    <!-- Fixed Categories: Efficiency, Content Unlock (Game), Content Unlock (Real), Emotional -->
                    {dim_why_content}
                    <div class="analysis-box">
                        <span class="analysis-title">🧐 逻辑与权衡：</span>
                        {dim_why_reasoning}
                    </div>
                </div>

                <!-- What -->
                <div style="background: #f8f9fa; padding: 20px; border-radius: 8px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                        <h3 style="border:none; margin:0; padding:0; color:#e67e22;">💬 社交内容 (What)</h3>
                        <span style="background:#fcf3cf; color:#d35400; font-size:0.75em; padding:2px 8px; border-radius:10px; font-weight:bold;">{dim_what_tag}</span>
                    </div>
                    <!-- Fixed Categories: Real Life Share, Game UGC, Game Gameplay -->
                    {dim_what_content}
                    <div class="analysis-box">
                        <span class="analysis-title">🧐 逻辑与权衡：</span>
                        {dim_what_reasoning}
                    </div>
                </div>

                <!-- Carrier -->
                <div style="background: #f8f9fa; padding: 20px; border-radius: 8px;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                        <h3 style="border:none; margin:0; padding:0; color:#16a085;">📱 社交载体 (Carrier)</h3>
                        <span style="background:#e8f8f5; color:#16a085; font-size:0.75em; padding:2px 8px; border-radius:10px; font-weight:bold;">{dim_carrier_tag}</span>
                    </div>
                    <!-- Fixed Categories: In-Game IM, External Platform, Offline -->
                    {dim_carrier_content}
                    <div class="analysis-box">
                        <span class="analysis-title">🧐 逻辑与权衡：</span>
                        {dim_carrier_reasoning}
                    </div>
                </div>
            </div>
        </section>

        <!-- Context Connector 2 -->
        <div style="margin: -20px 0 20px 0; text-align: center; color: #7f8c8d; font-size: 0.9em; font-style: italic;">
            ⬇ 这些抽象的权重分配，具体是通过哪些系统机制强制落地的？
        </div>

        <!-- 3. Systems -->
        <section class="card" style="margin-bottom: 30px;">
            <h2>3. 核心系统与体验还原 (Systems & UX)</h2>
            <div class="grid-2">
                {systems_content}
            </div>
        </section>

        <!-- Context Connector 3 -->
        <div style="margin: -20px 0 20px 0; text-align: center; color: #7f8c8d; font-size: 0.9em; font-style: italic;">
            ⬇ 当系统强制玩家进行高频互利时，如何防止社交压力爆表？
        </div>

        <!-- 4. Pressure & 5. Persona -->
        <div class="grid-2">
            <!-- 4. Pressure -->
            <section class="card">
                <h2>4. 压力模型 (Pressure Model)</h2>
                
                <div style="background: #f0f3f4; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-size: 0.9em; color: #555;">
                    <strong style="display:block; margin-bottom:10px; color:#2c3e50;">🤔 什么是社交压力？ (What is Social Pressure?)</strong>
                    <p style="margin:0 0 10px 0;">
                        社交压力是玩家为了获得社交体验而必须付出的<strong>“心理成本”</strong>或<strong>“门槛”</strong>。作为设计师，我们通过调整这五个维度的参数，来筛选目标用户并塑造社交氛围。
                    </p>
                    <details>
                        <summary style="cursor:pointer; color:#3498db; font-weight:bold;">点击查看维度定义 (Definitions)</summary>
                        <ul style="margin-top:10px; padding-left:20px; line-height:1.6;">
                            <li><strong>表现 (Performance):</strong> 对玩家操作水平/数值强度的要求。<i>(太菜了会被喷吗？)</i></li>
                            <li><strong>义务 (Obligation):</strong> 对上线时间/频率/准点率的要求。<i>(不按时上线会坑队友吗？)</i></li>
                            <li><strong>沟通 (Communication):</strong> 对语言交流/语音沟通的强制性。<i>(社恐能玩吗？)</i></li>
                            <li><strong>惩罚 (Penalty):</strong> 社交互动失败后的挫败感/损失。<i>(灭团了会掉装备/掉经验吗？)</i></li>
                            <li><strong>环境 (Environment):</strong> 社区整体的竞争性与戾气程度。<i>(新人会被歧视吗？)</i></li>
                        </ul>
                    </details>
                </div>

                <div class="chart-container">
                    {pressure_content}
                </div>
            </section>
            
            <!-- 5. Persona -->
            <section class="card">
                <h2>5. 用户画像 (Persona)</h2>
                {persona_table}
            </section>
        </div>

        <!-- 6. Takeaways -->
        <section class="card">
            <h2>6. 对 Beagle 的关键启示 (Key Takeaways)</h2>
            
             <div style="margin-bottom: 25px; padding: 15px; background: #eafaf1; border-radius: 8px; border-left: 4px solid var(--accent-color);">
                <strong style="color: var(--accent-color); display: block; margin-bottom: 10px; font-size: 1.1em;">核心设计原则 (Core Principles)</strong>
                {takeaway_principles}
            </div>

            <div class="takeaway-section">
                <div class="takeaway-col col-do">
                    <div class="col-title" style="color: var(--accent-color);">
                        <span class="icon-check">✔</span> 建议复用 (Copy)
                    </div>
                    {takeaway_do}
                </div>
                <div class="takeaway-col col-dont">
                    <div class="col-title" style="color: var(--danger-color);">
                        <span class="icon-cross">✘</span> 需要警惕 (Avoid)
                    </div>
                    {takeaway_dont}
                </div>
            </div>
        </section>
    </div>
</body>
</html>
"""

# ---------------------------------------------------------
# HELPER FUNCTIONS
# ---------------------------------------------------------
def create_model_item(title, main_text, sub_text):
    return u'''
    <div>
        <strong style="color: var(--text-secondary);">{title}</strong>
        <div style="font-size: 1.1em; font-weight: bold; margin-top: 5px;">{main_text}</div>
        <p style="font-size: 0.9em; color: #666;">{sub_text}</p>
    </div>
    '''.format(title=title, main_text=main_text, sub_text=sub_text)

def create_radar_chart(dims):
    # Dimensions config
    labels = {
        "perf": u"表现 (Perf)",
        "obli": u"义务 (Obli)",
        "comm": u"沟通 (Comm)",
        "pen": u"惩罚 (Penalty)",
        "env": u"环境 (Env)"
    }
    # Order of axes
    keys = ["perf", "obli", "comm", "pen", "env"]
    
    num_vars = len(keys)
    center_x = 200
    center_y = 150
    radius = 100
    
    # Calculate points
    angle_slice = 2 * math.pi / num_vars
    
    # Background polygons (levels: 20%, 40%, 60%, 80%, 100%)
    bg_svg = ""
    for level in [0.2, 0.4, 0.6, 0.8, 1.0]:
        poly_points = []
        for i in range(num_vars):
            angle = i * angle_slice - math.pi / 2 # Start from top
            r = radius * level
            x = center_x + r * math.cos(angle)
            y = center_y + r * math.sin(angle)
            poly_points.append(u"{},{}".format(x, y))
        bg_svg += u'<polygon points="{}" fill="none" stroke="#ddd" stroke-width="1" />'.format(" ".join(poly_points))
        
    # Axis lines and labels
    axis_svg = ""
    label_svg = ""
    for i, key in enumerate(keys):
        angle = i * angle_slice - math.pi / 2
        x_outer = center_x + radius * math.cos(angle)
        y_outer = center_y + radius * math.sin(angle)
        
        # Axis line
        axis_svg += u'<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#eee" stroke-width="1" />'.format(center_x, center_y, x_outer, y_outer)
        
        # Label position (slightly further out)
        label_r = radius + 25
        x_label = center_x + label_r * math.cos(angle)
        y_label = center_y + label_r * math.sin(angle)
        
        # Adjust alignment based on position
        anchor = "middle"
        if x_label > center_x + 10: anchor = "start"
        elif x_label < center_x - 10: anchor = "end"
        
        baseline = "middle"
        if y_label > center_y + 10: baseline = "hanging"
        elif y_label < center_y - 10: baseline = "baseline"
        
        label_svg += u'<text x="{}" y="{}" text-anchor="{}" dominant-baseline="{}" font-size="12" fill="#7f8c8d">{}</text>'.format(x_label, y_label, anchor, baseline, labels[key])

    # Data polygon
    data_points = []
    for i, key in enumerate(keys):
        val = dims.get(key, 0)
        # Normalize 0-100 to 0-1
        normalized_val = val / 100.0
        angle = i * angle_slice - math.pi / 2
        r = radius * normalized_val
        x = center_x + r * math.cos(angle)
        y = center_y + r * math.sin(angle)
        data_points.append(u"{},{}".format(x, y))
        
    data_svg = u'<polygon points="{}" fill="rgba(231, 76, 60, 0.2)" stroke="#e74c3c" stroke-width="2" />'.format(" ".join(data_points))
    
    # Data dots
    dots_svg = ""
    for pt in data_points:
        cx, cy = pt.split(',')
        dots_svg += u'<circle cx="{}" cy="{}" r="4" fill="#e74c3c" />'.format(cx, cy)

    svg = u'''
    <div style="width: 100%; display: flex; justify-content: center; margin-bottom: 20px;">
        <svg width="400" height="320" viewBox="0 0 400 320">
            {bg_svg}
            {axis_svg}
            {data_svg}
            {dots_svg}
            {label_svg}
        </svg>
    </div>
    '''.format(bg_svg=bg_svg, axis_svg=axis_svg, data_svg=data_svg, dots_svg=dots_svg, label_svg=label_svg)
    
    return svg

def create_bar(label, percent, color="var(--accent-color)", desc="", height=6, opacity=""):
    style_desc = ""
    if opacity:
        style_desc = opacity
    return u'''
    <div style="margin-bottom: 12px;">
        <div style="display:flex; justify-content:space-between; font-size:0.85em; margin-bottom:4px;">
            <span>{label}</span>
            <strong>{percent}%</strong>
        </div>
        <div style="height:{height}px; background:#eee; border-radius:3px;"><div style="width:{percent}%; height:100%; background:{color}; border-radius:3px;"></div></div>
        <div style="font-size:0.8em; color:#999; margin-top:2px; {style_desc}">{desc}</div>
    </div>
    '''.format(label=label, percent=percent, color=color, desc=desc, height=height, style_desc=style_desc)

def create_system_item(title, color, logic_list, ux_text):
    logic_html = u""
    for item in logic_list:
        logic_html += u"<li>" + item + u"</li>"
    
    return u'''
    <div style="background: #f8f9fa; padding: 20px; border-radius: 8px;">
        <h3 style="color: {color}; border-bottom: 2px solid {color}; margin-bottom: 10px;">{title}</h3>
        <div style="margin-bottom:15px; font-size:0.9em; line-height:1.5;">
            <strong style="display:block; margin-bottom:5px;">运行逻辑：</strong>
            <ul style="margin:0; padding-left:18px; color:#555;">
                {logic_html}
            </ul>
        </div>
        <div style="background:#fff; padding:10px; border-left:3px solid {color}; font-size:0.9em; color:#666;">
            <strong>体验还原：</strong> 
            <br>{ux_text}
        </div>
    </div>
    '''.format(title=title, color=color, logic_html=logic_html, ux_text=ux_text)

def create_persona_table(personas):
    rows_html = u""
    # Determine table mode based on first item
    is_new_format = False
    if len(personas) > 0 and 'ratio' in personas[0]:
        is_new_format = True
        
    for p in personas:
        focus_badge = u""
        if p.get('is_focus'):
            focus_badge = u'<span class="focus-badge">Core</span>'
            
        if is_new_format:
            ratio = p.get('ratio', 0)
            content_ratio = p.get('content_ratio', 0)
            trait = p.get('trait', '')
            content_desc = p.get('content_desc', '')
            
            rows_html += u'''
            <tr>
                <td style="vertical-align: top;"><strong>{type}</strong>{focus_badge}</td>
                <td style="vertical-align: top;">
                    <div style="font-weight:bold; font-size:1.1em; color:#2c3e50;">{ratio}%</div>
                    <div style="width:100%; height:4px; background:#eee; margin-top:5px; border-radius:2px;">
                        <div style="width:{ratio}%; height:100%; background:#95a5a6; border-radius:2px;"></div>
                    </div>
                </td>
                <td style="vertical-align: top;">
                     <div style="font-weight:bold; font-size:1.1em; color:#2c3e50;">{content_ratio}%</div>
                     <div style="width:100%; height:4px; background:#eee; margin-top:5px; border-radius:2px;">
                        <div style="width:{content_ratio}%; height:100%; background:#3498db; border-radius:2px;"></div>
                    </div>
                     <div style="font-size:0.85em; color:#7f8c8d; margin-top:5px; line-height:1.4;">{content_desc}</div>
                </td>
                <td style="vertical-align: top; font-size: 0.9em; line-height:1.5; color:#555;">
                    {trait}
                </td>
            </tr>
            '''.format(type=p['type'], focus_badge=focus_badge, ratio=ratio, content_ratio=content_ratio, content_desc=content_desc, trait=trait)
        else:
            # Fallback for old format
            rows_html += u'''
            <tr>
                <td><strong>{type}</strong>{focus_badge}</td>
                <td>{coverage}%</td>
                <td>{desc}</td>
            </tr>
            '''.format(type=p['type'], focus_badge=focus_badge, coverage=p.get('coverage', 0), desc=p.get('desc', ''))
        
    if is_new_format:
        return u'''
        <table class="persona-table">
            <thead>
                <tr>
                    <th style="width: 20%;">用户类型 (Type)</th>
                    <th style="width: 15%;">占比 (Ratio)</th>
                    <th style="width: 25%;">内容深度 (Content)</th>
                    <th>画像特征 (Traits)</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
        '''.format(rows_html=rows_html)
    else:
        return u'''
        <table class="persona-table">
            <thead>
                <tr>
                    <th style="width: 20%;">用户类型 (Type)</th>
                    <th style="width: 15%;">覆盖率</th>
                    <th>特征描述</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
        '''.format(rows_html=rows_html)


# ---------------------------------------------------------
# DATA DEFINITIONS
# ---------------------------------------------------------
# Load GAMES data from games_dump.py
import io

# We execute games_dump.py to populate GAMES
# create_bar and other helpers are defined above and will be available to the exec'd code
with io.open(os.path.join(os.path.dirname(__file__), 'games_dump.py'), 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # Skip encoding declaration and future import if present
    content = u"".join([line for line in lines if not line.startswith('# -*-') and not line.startswith('from __future__')])
    exec(content)

# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------
def main():
    base_dir = r"d:\charlie\social\analysis_Social"
    
    for filename, data in GAMES.items():
        filepath = os.path.join(base_dir, filename)
        print("Generating " + filename + "...")
        
        # Fill template
        try:
            # Prepare pressure content
            pressure_combined = u""
            if "pressure_dims" in data:
                pressure_combined += create_radar_chart(data["pressure_dims"])
            
            pressure_combined += u'<div style="margin-top: 20px;">' + data.get("pressure_content", "") + u'</div>'
            
            if "pressure_note" in data:
                pressure_combined += u'<div style="margin-top: 15px; padding: 15px; background: #f8f9fa; border-left: 3px solid #bdc3c7; color: #555; font-size: 0.95em;">' + data["pressure_note"] + u'</div>'

            html_content = TEMPLATE.format(
                title=data["title"],
                logo_text=data["logo_text"],
                subtitle=data["subtitle"],
                accent_color=data["accent_color"],
                accent_secondary=data["accent_secondary"],
                tags_html=data["tags_html"],
                context_challenge=data["context_challenge"],
                
                model_basic_3=data["model_basic_3"],
                inter_text=data["inter_text"],
                inter_percent=data["inter_percent"],
                inter_pos_start=data["inter_pos_start"],
                inter_pos_end=data["inter_pos_end"],
                inter_desc=data["inter_desc"],
                nece_text=data["nece_text"],
                nece_percent=data["nece_percent"],
                nece_desc=data["nece_desc"],
                model_keyword=data["model_keyword"],
                
                dim_who_tag=data["dim_who_tag"],
                dim_who_content=data["dim_who_content"],
                dim_who_reasoning=data["dim_who_reasoning"],
                
                dim_why_tag=data["dim_why_tag"],
                dim_why_content=data["dim_why_content"],
                dim_why_reasoning=data["dim_why_reasoning"],
                
                dim_what_tag=data["dim_what_tag"],
                dim_what_content=data["dim_what_content"],
                dim_what_reasoning=data["dim_what_reasoning"],
                
                dim_carrier_tag=data["dim_carrier_tag"],
                dim_carrier_content=data["dim_carrier_content"],
                dim_carrier_reasoning=data["dim_carrier_reasoning"],
                
                systems_content=data["systems_content"],
                pressure_content=pressure_combined,
                persona_table=data["persona_table"],
                
                takeaway_principles=data["takeaway_principles"],
                takeaway_do=data["takeaway_do"],
                takeaway_dont=data["takeaway_dont"]
            )
            
            # Write file
            with io.open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
        except Exception as e:
            print("Error generating " + filename + ": " + str(e))
        
    print("All reports updated successfully!")

if __name__ == "__main__":
    main()
