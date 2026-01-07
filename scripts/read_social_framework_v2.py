# -*- coding: utf-8 -*-
import pandas as pd
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

file_path = os.path.join(os.path.dirname(__file__), '..', 'xls', 'Beagle——社交框架.xlsx')

if os.path.exists(file_path):
    try:
        # Read all sheets
        xls = pd.read_excel(file_path, sheet_name=None, header=None)
        
        for sheet_name, df in xls.items():
            print(u"\n--- SHEET: {} ---\n".format(sheet_name))
            
            # Iterate over all cells and print non-null values
            for index, row in df.iterrows():
                row_content = []
                for item in row:
                    if pd.notnull(item):
                        row_content.append(unicode(item))
                
                if row_content:
                    line = " | ".join(row_content)
                    try:
                        print(line)
                    except:
                        print(line.encode('gbk', 'replace'))
            
    except Exception as e:
        print("Error reading excel file:")
        print(e)
else:
    print("File not found: " + file_path)
