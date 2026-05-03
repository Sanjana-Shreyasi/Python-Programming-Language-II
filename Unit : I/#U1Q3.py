#U1Q3
#Write a Python program to perform following operations on Tuples: 
#3.1) Create and access  
#3.2) Nested Tuple
#3.3) Repetition of tuple
#3.4) Concatenation of tuples 
# 3.1 Create and access tuple
T = (10, 20, 30, 40)

print("Tuple:", T)
print("First element:", T[0])
print("Second element:", T[1])

# 3.2 Nested Tuple
NT = ("Math", ("Algebra", "Geometry"), "Science")

print("\nNested Tuple:", NT)
print("Main subject:", NT[0])
print("Subtopics:", NT[1])

# 3.3 Repetition of tuple
T2 = (1, 2, 3)
print("\nRepetition:", T2 * 3)

# 3.4 Concatenation of tuples
T3 = (4, 5)
T4 = T2 + T3

print("\nConcatenation:", T4)		