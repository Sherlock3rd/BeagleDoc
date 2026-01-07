import io
import re

with io.open('d:/charlie/social/append_data.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the content inside data_code = u''' ... '''
match = re.search(r"data_code = u'''(.*?)'''", content, re.DOTALL)
if match:
    data_content = match.group(1)
    with io.open('d:/charlie/social/games_dump.py', 'w', encoding='utf-8') as f_out:
        f_out.write(data_content)
    print("Extracted games data to games_dump.py")
else:
    print("Could not find data_code block")
