import pandas as pd
import numpy as np
import os
from time import sleep
import getpass
from platform import system
import re
import openpyxl

import sys





platform = system()
user = getpass.getuser() 
regex = r"^\s\d{2}$"
test = r"^TEST$"
clas = r"^CLAS"

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






writer=pd.ExcelWriter("C:\\Users\\"+user+"\\Documents\\output.xlsx", engine='openpyxl')









#data = sheet[:81]



start = 0
stop = 0
sheetCount = 0
periods = []
for cols in sheet:
    col = sheet[cols]
    
    for i, item in enumerate(col):
        if i == len(col) - 1:
            next = col[i]
        else:
            next = col[i+1]
        if pd.notna(item):
            if col.name=="1wbgra15.p" and type(item) == str and r'Teacher' in item:
                start = i
                print(start)
            if col.name=="1wbgra15.p" and type(item) == str and re.fullmatch(regex, item) and i > start and (pd.isna(next) or i == len(col) - 1 ):
                stop = i
                sheetCount += 1
                temp = sheet[start:stop]
                temp.dropna(axis=1, how='all')
                for cols in temp:
                    col = temp[cols]
                    for item in col:
                        if re.fullmatch(r"^CLAS", item) and type(item) == str:
                            temp.drop(cols)
                temp.to_excel(f"C:\\Users\\{user}\\Documents\\output.xlsx", header=False, index=False)
                
        
                
                

           
            
                
                 
            
        i += 1

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