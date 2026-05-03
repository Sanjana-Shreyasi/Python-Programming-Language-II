#U3Q9P2
#Create a module called shapes.py with functions to calculate the area of a circle (with radius), rectangle (with length and width) and 
#triangle (with length and width). Based on user input, determine and show the area of shapes using the user-defined module.		
import shapes

print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of Circle:", shapes.circle(r))

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle:", shapes.rectangle(l, w))

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print("Area of Triangle:", shapes.triangle(b, h))

else:
    print("Invalid choice")