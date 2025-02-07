import pandas as pd
import os
from time import sleep
import getpass
from platform import system
import re

import sys





platform = system()
user = getpass.getuser() 
regex = r"^\s\d{2}$"
category = r"^[TEST]$"

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

# pd.read_excel('/mnt/c/Users/jacob.pugh/Downloads/Pugh Data.xlsx' ) or





# writer=pd.ExcelWriter("C:\\Users\\"+user+"\\Documents\\Jenn-Tron5000", engine='xlsxwriter')



cell = sheet.iloc[0, 13]


col = sheet['1wbgra15.p']


period = sheet['Unnamed: 5']



data = sheet.columns[:81]

schedule = []


lastnames = []

firstnames = []

classSize = []

for cols in data:
    i = 0
    length = len(sheet[cols])
    col = sheet[cols]
    while (i < length):
        if col[i] != 'nan':
            if type(col[i]) == str and 'Period: ' in col[i]:
                # print(f"found {col[i]} at col[{i}]")
                schedule.append(col[i])
                #new.columns = schedule
            if (type(col[i]) == str and bool(re.fullmatch(regex, col[i]))):
                classSize.append(col[i])

            if (type(col[i]) == str and bool(re.fullmatch(category, col[i]))):
                print("found")

                
            elif type(col[i]) == str and 'Last Name' in col[i]: 
                
                lastnames.append((col[i+1]))
            elif type(col[i]) == str and 'First Name' in col[i]:
                firstnames.append(col[i+1])             
            
        i += 1
print(schedule)
print(lastnames, "\n", firstnames)
newClassSize = []
for i in range(len(classSize)):
    if classSize[i] == ' 01' and classSize[i-1] and i != 0:
        newClassSize.append(int(classSize[i- 1])) 
        print(newClassSize)
    elif i == len(classSize) - 1:
        newClassSize.append(int(classSize[i]))
print(newClassSize)

new = pd.DataFrame(columns=schedule)

print(new)





# while (i < length):
#     if period[i] != 'NaN':
#         if type(period[i]) == str and 'Period: ' in period[i]:
#             print(f"found {period[i]} at period[{i}]")
#     i += 1

students = []


# print(sheet)
# print(cell)
# print(int(col[8]))
# print(data)