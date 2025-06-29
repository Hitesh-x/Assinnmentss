Assignment 1

# Question 1


name = input("Name: ")
student_class = input("Class: ")

# Marks input
print("Enter marks of 5 subjects:")
m1 = int(input("Subject 1: "))
m2 = int(input("Subject 2: "))
m3 = int(input("Subject 3: "))
m4 = int(input("Subject 4: "))
m5 = int(input("Subject 5: "))


total = m1 + m2 + m3 + m4 + m5
percent = total / 5

print("=================OUTPUT================>>")

print("\n---Student Result ---")
print("Name:", name)
print("Class:", student_class)
print("Total Marks:", total)
print("Percentage:", percent)

Question 2


first = input("First DatA: ")
second = input("Second DatA: ")

join = first + second


print("\nJoin string:", join)
print("Uppercase:", join.upper())
print("Lowercase:", join.lower())
print("Length:", len(join))
print("Reversed:", join[::-1])
print("Only letters?", join.isalpha())



