#U4Q11
# Write a program to demonstrate fundamental file handling operations including opening a file, 
# reading its contents, writing data to it, appending additional content and ensuring proper 
# closing of the file. 

#Writing data to the file
F=open("Sample Txt.txt","w")
F.write("Python is a programming language.\n")
F.write("Python is used for many purposes.\n")
F.close()
print("Data written successfully.\n")

#Reading file data
F=open("Sample Txt.txt")
C=F.read
print("Reading file contents :",C)
F.close()

#Appending data to the file
F=open("Sample Txt.txt","a")
F.write("Python is used in Artificial Intelligence.")
F.close()
print("Data appended to the file successfully.")

#Reading final data from file
F=open("Sample Txt.txt","r")
UC=F.read
print("Updated file contents :",UC)
F.close()