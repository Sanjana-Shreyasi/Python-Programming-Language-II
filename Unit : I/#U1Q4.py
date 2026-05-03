#U1Q4
#Write a Python program to perform following operations on Dictionaries: 
#4.1) Create and access dictionary elements  
#4.2) Update Dictionary 
#4.3) Removing Elements 
#4.4) Merging dictionaries
# 4.1 Create and access dictionary
D = {"Name": "Sanjana", "Age": 18, "Course": "Engineering"}

print("Dictionary:", D)
print("Name:", D["Name"])
print("Age:", D["Age"])

# 4.2 Update dictionary
D["Age"] = 19          # update value
D["City"] = "Nashik"   # add new key-value
print("\nAfter updating:", D)

# 4.3 Removing elements
D.pop("Course")        # remove specific key
print("After removing 'Course':", D)

# 4.4 Merging dictionaries
D2 = {"Marks": 90, "Grade": "A"}
D.update(D2)

print("\nAfter merging:", D)		