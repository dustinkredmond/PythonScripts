import pandas as pd
from os import access, R_OK
from os.path import isfile
import sqlite3
import sys

'''
 Simple script to convert an Excel spreadsheet into a
 SQLite3 database. This makes complex queries a breeze.
'''

excel_sheets = []
if len(sys.argv) > 1:
    sys.argv.remove(0)  # argv[0] will be program name
    for arg in sys.argv:
        excel_sheets.append(arg)

# For testing
excel_sheets.append("test.xls")

if len(excel_sheets) == 0:
    print("Please supply the path to an Excel sheet as an argument.")
    sys.exit(-1)

# Read each argument as a file path
for sheet in excel_sheets:
    # Check that arguments were files, and can read
    if not isfile(sheet) or not access(sheet, R_OK):
        print("File: {} unable to access or is not a"
              " valid file path. Skipping.".format(sheet))
        continue

    # Read excel file into pandas DataFrame
    df = pd.read_excel(sheet)
    # Get each column name as string for normalization
    columns = list(map(str, df.columns))
    # Replace each space with underscore in columns
    columns = [i.replace(" ", "_") for i in columns]
    # Make each column name uppercase
    columns = [i.upper() for i in columns]
    # Replace columns in original DataFrame with pretty column names
    df.columns = columns

    # Create SQLite database with name of excel file (sans file extension)
    conn = sqlite3.connect("{}.db".format(sheet[:sheet.rindex('.')]))
    # Use DataFrame to_sql to add data from DataFrame to SQLite table
    try:
        df.to_sql(name=sheet[:sheet.rindex('.')], con=conn)
    except ValueError:
        # to_sql raises ValueError if the table already exists
        print("SQLite database already exists. Delete {} then try again."
              .format("{}.db".format(sheet[:sheet.rindex('.')])))
