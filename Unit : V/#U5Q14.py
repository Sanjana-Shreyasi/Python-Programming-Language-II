#U5Q14
#Create a program that takes a filename from the user and tries to open the file for reading and handle these exceptions and provide appropriate error messages for following cases.
#1.1) FileNotFoundError: If the file does not exist.
#2.2) PermissionError: If the program lacks permissions to read the file.		
filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("\nFile contents:\n", content)

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied. Cannot read the file.")