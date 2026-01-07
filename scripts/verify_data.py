# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io
import re

# Mock helper functions to allow exec
def create_model_item(title, main_text, sub_text): return ""
def create_bar(label, percent, color="var(--accent-color)", desc="", height=6, opacity=""):
    return {"label": label, "percent": percent}
def create_system_item(title, color, logic_list, ux_text): return ""
def create_persona_table(personas): return ""

# Load GAMES
with io.open(r'd:\charlie\social\games_dump.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    content = u"".join([line for line in lines if not line.startswith('# -*-') and not line.startswith('from __future__')])
    # We need to handle the fact that create_bar returns a string in the real file but we want objects
    # But wait, the file concatenates strings: create_bar(...) + create_bar(...)
    # So our mock create_bar should return a list? No, + on lists works.
    # Let's make create_bar return a list of dicts.
    
def create_bar_mock(label, percent, color="var(--accent-color)", desc="", height=6, opacity=""):
    return [{"label": label, "percent": percent}]

# Replace the create_bar in the context
context = {
    "create_model_item": create_model_item,
    "create_bar": create_bar_mock,
    "create_system_item": create_system_item,
    "create_persona_table": create_persona_table,
    "True": True,
    "False": False
}

exec(content, context)
GAMES = context["GAMES"]
print("Loaded {} games.".format(len(GAMES)))

# Fixed categories
FIXED_CATS = {
    "dim_who_content": [u"生人社交", u"熟人社交", u"AI-NPC"],
    "dim_why_content": [u"效率提升", u"内容解锁（游戏内容）", u"内容解锁（现实生活）", u"情绪价值"],
    "dim_what_content": [u"玩家现实生活分享交流", u"游戏内容的二创分享交流", u"游戏玩法内容"],
    "dim_carrier_content": [u"游戏内IM", u"游戏外部平台", u"线下活动"]
}

failed = False

for game_file, data in GAMES.items():
    print(u"Checking {}...".format(data["title"]))
    
    # Check Pressure
    if "pressure_dims" not in data:
        print(u"  [FAIL] Missing pressure_dims")
        failed = True
    
    # Check Dimensions
    for dim_key, expected_cats in FIXED_CATS.items():
        if dim_key not in data:
            print(u"  [FAIL] Missing {}".format(dim_key))
            failed = True
            continue
            
        bars = data[dim_key]
        # bars is a list of dicts: [{'label': '...', 'percent': ...}, ...]
        
        current_cats = set([b['label'] for b in bars])
        total_percent = sum([b['percent'] for b in bars])
        
        # Check categories
        missing_cats = [c for c in expected_cats if c not in current_cats]
        if missing_cats:
            print(u"  [FAIL] {} missing categories: {}".format(dim_key, u", ".join(missing_cats)))
            failed = True
            
        # Check sum
        if total_percent != 100:
            print(u"  [FAIL] {} sum is {}% (expected 100%)".format(dim_key, total_percent))
            failed = True

if not failed:
    print(u"All checks passed!")
else:
    print(u"Some checks failed.")
