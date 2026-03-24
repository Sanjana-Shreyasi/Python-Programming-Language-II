# Write a program to import following modules and perform temperature conversions based on user input. Create a packaage called
# temperature with the following modules :
# 1) celsius_to_fahrenheit.py : Conatians a function to convert Celsius to Fahrenheit
# 2) fahrenheit_to_celsius.py : Contains a function to convert Fahrenheit to Celsius
# 3) celsius_to_kelvin.py : Conatins a function to convert Celsius to Kelvin

from Temperature import Celsius_to_Fahrenheit
from Temperature import Fahrenheit_to_Celsius
from Temperature import Celsius_to_Kelvin

def main():
    I=int(input("Select Conversion\n1)Celsius to Fahrenheit\n2)Fahrenheit to Celsius\n3)Celsius to Kelvin"))
    if I==1:
        C=float(input("Enter Celsius value:"))
        print("Converted to Fahrenheit",Celsius_to_Fahrenheit.convert(C))
    elif I==2:
        F=float(input("Enter Fahrenhiet value:"))
        print("Converted to Celsius",Fahrenheit_to_Celsius.convert(F))
    elif I==3:
        C=float(input("Enter Celsius value:"))
        print(f"Converted to Kelvin {Celsius_to_Kelvin.convert(C)}")
    else:
        print("Wrong Input!")

if __name__=="__main__":
   main()