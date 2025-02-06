import pandas as pd
import os
from time import sleep
import getpass

#fileName = input("Welcome to the Jenn-Tron 5000. Please enter the name of a document you would like to Reist-ify: ")
#print()

# for root, dir, files in os.walk('/mnt/c'):
#     if fileName in files:
#         print("Found file")

sheet = pd.read_excel('/mnt/c/Users/jacob.pugh/Downloads/Pugh Data.xlsx' )

user = getpass.getuser()

print(user)

# writer=pd.ExcelWriter("C:\\Users\\"+user+"\\Documents\\Jenn-Tron5000", engine='xlsxwriter')



cell = sheet.iloc[2, 0]


col = sheet['1wbgra15.p']


period = sheet['Unnamed: 5']



data = sheet.columns[:81]

schedule = []


for cols in data:
    i = 0
    length = len(sheet[cols])
    col = sheet[cols]
    while (i < length):
        if col[i] != 'NaN':
            if type(col[i]) == str and 'Period: ' in col[i]:
                # print(f"found {col[i]} at col[{i}]")
                schedule.append(col[i])
                #new.columns = schedule
        i += 1
print(schedule)

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