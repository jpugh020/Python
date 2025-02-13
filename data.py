import pandas as pd
import numpy as np
import os
from time import sleep
import getpass
from platform import system
import re
from openpyxl import load_workbook

import sys





platform = system()
user = getpass.getuser() 
regex = r"^\s\d{2}$"
test = r"^TEST$"
clas = r"^CLAS"
docs = f"C:\\Users\\{user}\\Documents"

if platform:
    if platform == "Windows":
        path = f'C:\\Users\\{user}\\Downloads\\'
        sudo = 'C:\\'
    elif platform == "Linux":
        path = f'~/Documents'



fileName = input("Welcome to the Jenn-Tron 5000. Please enter the name of a document you would like to Reist-ify, including the filetype at the end (e.g. .csv or .xlsx): ")
filecount = 0
for root, dirs, files in os.walk(path):
    fileLen = len(files)
    if fileLen != 0:
        if fileName in files:
            print(f"Found at {root}")
            path = root + fileName
            break
        else:
            filecount += 1
            print(f"Checked {filecount} files\r", end="")



            


    

    
#print()

# for root, dir, files in os.walk('/mnt/c'):
#     if fileName in files:
#         print("Found file")

sheet = pd.read_excel(path)
sheet = sheet.dropna(axis=1, how="all")
# pd.read_excel('/mnt/c/Users/jacob.pugh/Downloads/Pugh Data.xlsx' ) or
















#data = sheet[:81]

savePath = f"C:\\Users\\{user}\\Documents\\"

start = 0
stop = 0
sheetCount = 0
periods = []
teacher = ''
for cols in sheet:
    col = sheet[cols]
    
    for i, item in enumerate(col):
        if i == len(col) - 1:
            next = col[i]
        else:
            next = col[i+1]
        if pd.notna(item):
            if col.name == "1wbgra15.p" and type(item) == str and 'Teacher' in item:
                start = i
                print(start)
            if col.name == "1wbgra15.p" and type(item) == str and re.fullmatch(regex, item) and i > start and (pd.isna(next) or i == len(col) - 1):
                stop = i
                sheetCount += 1
                temp = sheet[start:stop]
                # temp.dropna(axis=1, how='all')
                for temp_cols in temp:
                    temp_col = temp[temp_cols]
                    for temp_item in temp_col:
                        if type(temp_item) == str and "Period: " in temp_item:
                            sheetName = temp_item[:6]
                            sheetName += temp_item[7:]
                            
                            print(sheetName)
                        if type(temp_item) == str and "Teacher: " in temp_item and savePath == f"C:\\Users\\{user}\\Documents\\":
                            teacher = temp_item[9:]
                            savePath += teacher + ".xlsx"
                            for root, dirs, files in os.walk(docs):
                                fileLen = len(files)
                                if fileLen != 0:
                                    if teacher + ".xlsx" in files:
                                        exists = True
                                        break
                                    else:
                                        exists = False
                                        
                if not exists:
                    temp.to_excel(savePath, header=False, index=False, sheet_name=sheetName)
                else:
                    book = load_workbook(savePath)
                    writer = pd.ExcelWriter(savePath, engine='openpyxl')
                    writer.book = book
                    temp.to_excel(writer, header=False, index=False, sheet_name=sheetName)
                    
                    

                # Reset start and stop for the next iteration
                start = 0
                stop = 0

writer.close()

# temp = sheet.loc[2 : 31]
# print(temp)

print(pd.isna(temp.iloc[1, 1]))


# print(tests)

# new = pd.DataFrame(columns=schedule)

# print(new)





# while (i < length):
#     if period[i] != 'NaN':
#         if type(period[i]) == str and 'Period: ' in period[i]:
#             print(f"found {period[i]} at period[{i}]")
#     i += 1

students = []



# print(sheet.notna())
# print(int(col[8]))
# print(data)