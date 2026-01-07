import io

# Read games_dump.py
with io.open('d:/charlie/social/games_dump.py', 'r', encoding='utf-8') as f:
    games_content = f.read()

header = u'''# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import io
import os

# Define the helper functions locally just for the data construction if needed, 
# but we are writing raw python code string to the file.
# We need to write the `GAMES` dictionary definition to the file.

data_code = u\'\'\'
'''

footer = u'''\'\'\'
'''

new_content = header + games_content + footer

with io.open('d:/charlie/social/append_data.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully updated append_data.py")
