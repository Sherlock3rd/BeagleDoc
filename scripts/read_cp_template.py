# -*- coding: utf-8 -*-
import os
import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# List files to find the correct name
files = os.listdir(u'.')
target_file = None
for f in files:
    if f.endswith('.xlsx') and u'CP' in f:
        target_file = f
        print(u"Found file: " + f)
        break

if target_file:
    try:
        # Read all sheets
        xls = pd.read_excel(target_file, sheet_name=None)
        
        for sheet_name, df in xls.items():
            print(u"\n--- SHEET: {} ---\n".format(sheet_name))
            print(u"Columns: {}\n".format(u", ".join([unicode(c) for c in df.columns])))
            print(df.to_string(index=False))
            
    except Exception as e:
        print("Error reading excel file:")
        print(e)
else:
    print("File not found")
