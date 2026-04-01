# -*- coding: utf-8 -*-
import os
import datetime
import time
import io

# Configuration
PROJECT_ROOT = r"d:\charlie\social"
DOCS_ROOT = os.path.join(PROJECT_ROOT, "docs")
PUBLISH_ROOT = os.path.join(PROJECT_ROOT, "publish")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "index.html")

DOCUMENTS = [
    {
        "title": u"⚔️ 副本匹配规则详细方案",
        "desc": u"深度对标 WoW/Albion/仗剑传说，确立了“本服优先 -> 进度门槛 -> 全服扩展”的 Beagle 匹配算法。",
        "html_name": "matchmaking_rules_analysis.html",
        "source_name": "matchmaking_rules_analysis.html",
        "href": "docs/matchmaking_rules_analysis.html",
        "tag": "Core",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🤝 7日版本社交生态框架",
        "desc": u"深度解析 CP1/CP2/CP3 三种社交形态（仗剑/蜂巢/CoD），包含小队与联盟的共生关系及数值压力模型。",
        "html_name": "concept_economic_symbiosis_squad.html",
        "source_name": "concept_economic_symbiosis_squad.html",
        "href": "docs/concept_economic_symbiosis_squad.html",
        "tag": "Hot",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🗺️ 七日社交渐进与地图玩法 CP",
        "desc": u"CP-A/CP-B/CP-C 时间轴与环状 GVE 结构示意，强调“熟人/生人、渗透/隔离”的体验主轴。",
        "html_name": "sevenday_social_progression.html",
        "source_name": "map/sevenday_social_progression.md",
        "tag": "Published",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🐲 GVE 联盟 Boss 设计 v2.0",
        "desc": u"定义了“分层实时预约”机制 (Phased Real-Time Booking)，解决在线率与公平性矛盾。",
        "html_name": "GVE_Alliance_Boss_Design_v2.html",
        "source_name": "GVE_Alliance_Boss_Design_v2.html",
        "href": "docs/GVE_Alliance_Boss_Design_v2.html",
        "tag": "v2.0",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"📊 社交框架整体汇报",
        "desc": u"社交方案的综合汇报，包含可视化图表与决策矩阵。",
        "html_name": "social_framework_report.html",
        "source_name": "social_framework_report.html",
        "href": "docs/social_framework_report.html",
        "tag": "Report",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🏕️ 城镇布局与迁城系统设计",
        "desc": u"定义了 7日版本的城镇/野外双层空间结构，以及全域抢占式（Scramble）车位迁城机制。",
        "html_name": "town_relocation_design.html",
        "source_name": "town_relocation_design.md",
        "tag": "New",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"⚔️ PVP 地块玩法详细设计",
        "desc": u"定义了 7日版本的 PVP 地块分级体系（L1/L2）、搜打拿核心循环与地图落位原则。",
        "html_name": "pvp_tile_detailed_design.html",
        "source_name": "pvp_tile_detailed_design.md",
        "tag": "New",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🗺️ 大地图pvp地块战斗玩法cp",
        "desc": u"包含 PVP/PVE 核心循环、CP1/CP2/CP3 玩法分层及演进路线规划。",
        "html_name": "beagle_map_gameplay_design.html",
        "source_name": "beagle_map_gameplay_design.md",
        "tag": "Core",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🏗️ 合线详细方案",
        "desc": u"新老玩家分流机制、地图区域划分及服务器合并规则详解。",
        "html_name": "scheme2_detailed_design.html",
        "source_name": "scheme2_detailed_design.md",
        "tag": "Tech",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🌿 合线方案CP",
        "desc": u"文档版本控制、分支管理流程及协作规范说明。",
        "html_name": "branching_design_spec.html",
        "source_name": "branching_design_spec.html",
        "tag": "Meta",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🎈 轻度社交设计",
        "desc": u"针对泛用户的非数值社交互动模块，增强游戏氛围与留存。",
        "html_name": "light_social_design.html",
        "source_name": "light_social_design.md",
        "tag": "Casual",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🛡️ 联盟系统设计",
        "desc": u"联盟组织架构、管理权限、福利体系及核心功能完整设计。",
        "html_name": "design_alliance.html",
        "source_name": "Alliance_System_Design.md",
        "tag": "System",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"📊 社交分析报告总览",
        "desc": u"深度拆解 ROK、逆水寒等竞品社交系统，提供设计参考依据。",
        "html_name": "Beagle_Social_Analysis_Report.html",
        "source_name": None,
        "tag": "Analysis",
        "btn_text": u"🚀 进入文档"
    },
    {
        "title": u"🔐 登录流程设计",
        "desc": u"梳理登录入口、账号态与异常分支，统一新手首日转化前的关键触点。",
        "html_name": "login_flow_design.html",
        "source_name": "login_flow_design.md",
        "tag": "Flow",
        "btn_text": u"🚀 进入文档"
    }
]

HTML_TEMPLATE = u"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Beagle社交设计策划案合集</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

        :root {{
            --primary-color: #2c3e50;
            --accent-color: #3498db;
            --bg-color: #fdfbf7;
            --text-color: #333;
            --border-color: #333;
            --comic-font: 'Patrick Hand', cursive, sans-serif;
        }}

        body {{
            font-family: 'Patrick Hand', -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            font-size: 18px;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 20px;
            background-image: radial-gradient(#e5e5e5 1px, transparent 1px);
            background-size: 20px 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 2px;
            border: 3px solid #333;
            box-shadow: 10px 10px 0px rgba(0,0,0,0.8);
        }}

        h1 {{
            font-family: var(--comic-font);
            border-bottom: 4px solid var(--primary-color);
            padding-bottom: 10px;
            color: var(--primary-color);
            margin-top: 0;
            font-size: 3.5em !important;
            text-align: center;
        }}

        .author-tag {{
            text-align: center;
            font-size: 1.2em;
            color: #666;
            margin-bottom: 40px;
            font-style: italic;
        }}

        .doc-card {{
            background: #fff;
            border: 3px solid #333;
            border-radius: 255px 15px 225px 15px / 15px 225px 15px 255px;
            padding: 25px;
            transition: all 0.2s ease;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
        }}

        .doc-card:hover {{
            transform: translateY(-5px) rotate(1deg);
            box-shadow: 8px 8px 0px rgba(0,0,0,1);
            background-color: #fffef0;
            z-index: 10;
        }}

        .doc-title {{
            font-size: 1.8em;
            font-weight: bold;
            color: var(--primary-color);
            margin-bottom: 10px;
            line-height: 1.2;
        }}

        .doc-meta {{
            font-size: 0.9em;
            color: #666;
            margin-top: 15px;
            border-top: 2px dashed #ccc;
            padding-top: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .btn-jump {{
            display: inline-block;
            background: var(--accent-color);
            color: white;
            padding: 8px 20px;
            border: 2px solid #333;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1em;
            box-shadow: 3px 3px 0px rgba(0,0,0,1);
            transition: all 0.1s;
            margin-top: 15px;
            text-align: center;
        }}

        .btn-jump:hover {{
            transform: translate(1px, 1px);
            box-shadow: 2px 2px 0px rgba(0,0,0,1);
            background: #2980b9;
        }}

        .grid-container {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 30px;
            padding: 20px;
        }}
        
        .badge {{
            display: inline-block;
            padding: 2px 8px;
            border: 2px solid #333;
            border-radius: 12px;
            font-size: 0.8em;
            font-weight: bold;
            background: #ffeaa7;
            transform: rotate(-2deg);
        }}

        .footer-note {{
            text-align: center;
            margin-top: 50px;
            padding-top: 20px;
            border-top: 2px solid #eee;
            color: #888;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>

<div class="container">
    <h1>🎨 Beagle 社交设计策划案合集</h1>
    <div class="author-tag">Designed by <span style="font-weight:bold; color:#e74c3c;">Charlie</span> 🦊</div>

    <div class="grid-container">
        {cards_html}
    </div>

    <div class="footer-note">
        <p>💡 本文档合集由 Python 脚本自动生成，最后更新于 {gen_date}。新增文档请更新 <code>scripts/update_hub.py</code></p>
    </div>
</div>

</body>
</html>
"""

CARD_TEMPLATE = u"""
        <!-- Document Card -->
        <div class="doc-card">
            <div>
                <div class="doc-title">{title}</div>
                <p class="text-gray-600">{desc}</p>
            </div>
            <div>
                <a href="{href}" class="btn-jump">{btn_text}</a>
                <div class="doc-meta">
                    <span>📅 更新: {date}</span>
                    <span class="badge">{tag}</span>
                </div>
            </div>
        </div>
"""

def get_last_modified(doc_config):
    # Try source first
    if doc_config["source_name"]:
        source_path = os.path.join(DOCS_ROOT, doc_config["source_name"])
        if os.path.exists(source_path):
            return os.path.getmtime(source_path)
    
    # Fallback to published file
    html_path = os.path.join(PUBLISH_ROOT, doc_config["html_name"])
    if os.path.exists(html_path):
        return os.path.getmtime(html_path)
    
    return time.time()

def format_date(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d")

def main():
    # Pre-calculate mtime for sorting
    doc_list = []
    for doc in DOCUMENTS:
        mtime = get_last_modified(doc)
        doc_data = doc.copy()
        doc_data['mtime'] = mtime
        doc_list.append(doc_data)

    # Sort by mtime descending (newest first)
    doc_list.sort(key=lambda x: x['mtime'], reverse=True)

    cards_html = ""
    for doc in doc_list:
        date_str = format_date(doc['mtime'])
        
        # Manually constructing string to avoid encoding issues in mixed environment
        # But using format is safer for placeholders
        card = CARD_TEMPLATE.format(
            title=doc["title"],
            desc=doc["desc"],
            href=doc.get("href", "publish/{}".format(doc["html_name"])),
            btn_text=doc["btn_text"],
            date=date_str,
            tag=doc["tag"]
        )
        cards_html += card

    final_html = HTML_TEMPLATE.format(
        cards_html=cards_html,
        gen_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    with io.open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print("Successfully generated {} with updated timestamps and sorted order.".format(OUTPUT_FILE))

if __name__ == "__main__":
    main()
