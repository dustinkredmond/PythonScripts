import pandas as pd
import sqlite3
import sys
'''
 Simple script to convert an Excel spreadsheet into a
 SQLite3 database. This makes complex queries a breeze.
 
 Expects one or more paths to Excel workbooks as command line arguments
 Requires pandas libary, you must run:
     $ pip install pandas
'''

excel_sheets = []
if len(sys.argv) > 1:
    sys.argv.remove(0)
    for arg in sys.argv:
        excel_sheets.append(arg)

if len(excel_sheets) > 0:
    for sheet in excel_sheets:
        df = pd.read_excel(sheet)
        conn = sqlite3.connect("{}.db".format(sheet[:sheet.rindex('.')]))
        df.to_sql(name=sheet[:sheet.rindex('.')], con=conn)
else:
    print("Please supply the path to an Excel sheet as an argument")
