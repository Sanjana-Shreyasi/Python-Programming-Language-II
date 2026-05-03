#U1 Q2
#Write a Python program to perform following operations on set: 
#2.1) Create and access set elements
#2.2) Union of the elements  
#2.3) Intersection of the elements
#2.4) Difference of the elements		

# 2.1 Create and access set elements
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Set A:", A)
print("Set B:", B)

print("\nAccessing elements of Set A:")
for i in A:
    print(i)

# 2.2 Union
print("\nUnion of A and B:", A.union(B))

# 2.3 Intersection
print("Intersection of A and B:", A.intersection(B))

# 2.4 Difference
print("Difference A - B:", A.difference(B))
print("Difference B - A:", B.difference(A))