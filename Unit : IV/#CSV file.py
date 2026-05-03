#U4Q12
#Write a Python program to count the total number of rows in a CSV file.
import csv
RowCounter=0
with open("Data.csv","r") as F:
    Reader=csv.reader(F)
    for I in Reader:
       RowCounter+=1
print("Total number of rows:",RowCounter)
