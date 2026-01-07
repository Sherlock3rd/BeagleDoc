# -*- coding: utf-8 -*-
import pandas as pd
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

file_path = u'Beagle——社交框架.xlsx'

try:
    xls = pd.ExcelFile(file_path)
    
    target_sheet = None
    for name in xls.sheet_names:
        if 'concept' in name.lower() or 'cp' in name.lower():
            target_sheet = name
            if 'concept' in name.lower():
                break
    
    if target_sheet:
        print "\nReading sheet: " + target_sheet
        df = pd.read_excel(file_path, sheet_name=target_sheet)
        
        # Print first 200 lines to capture Background and 4W
        count = 0
        for index, row in df.iterrows():
            if count >= 200:
                break
            
            row_content = []
            for item in row:
                if pd.notnull(item):
                    row_content.append(unicode(item))
            if row_content:
                line = " | ".join(row_content)
                try:
                    print line
                except:
                    print line.encode('gbk', 'replace')
            count += 1
    else:
        print "No sheet named 'CONCEPT' or similar found."

except Exception as e:
    print "Error:", e
