import pandas as pd
import numpy as np
import os
from time import sleep
import getpass
from platform import system
import re

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






# writer=pd.ExcelWriter("C:\\Users\\"+user+"\\Documents\\Jenn-Tron5000", engine='xlsxwriter')



cell = sheet.iloc[0, 13]


col = sheet['1wbgra15.p']



#data = sheet[:81]


tests = []
classes={}

catRows = {}

grades = {}

lastnames = []

firstnames = []

classSize = []

start = 0
stop = 0

for cols in sheet:
    col = sheet[cols]
    for i, item in enumerate(col):
        if item != 'nan':
            if col.name=="1wbgra15.p" and type(item) == str and r'Teacher' in item:
                start = i
                print(start)
            if col.name=="1wbgra15.p" and type(item) == str and r"^\s\d{2}" in item and col[i+1] == np.nan and i > start:
                stop = i
                print(stop)

                
                

           
            
                
                 
            
        i += 1
print(lastnames, "\n", firstnames)
temp = sheet.loc[2 : 31]
print(temp)

print(temp.iloc[1, 1])


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