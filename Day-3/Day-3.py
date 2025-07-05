
# ASSIGNMENT 3

# =====================================================>>
# Question 1

t = (1, 2, 3, 4)
print("Tuple:", t)

s = {2, 3, 4, 2, 1}
print("Set (unique):", s)

d = {"name": "Alice", "age": 21}
print("Dictionary:", d)

# ========================================================>>

# Question 2

def calculate(a, b):
    print("Add:", a + b)
    print("Subtract:", a - b)
    print("Multiply:", a * b)
    print("Divide:", a / b if b != 0 else "Undefined")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
calculate(x, y)

# ========================================================>>

# Question 3

num = input("Enter a number: ")
if num == num[::-1]:
    print(num, "is a Palindrome Number")
else:
    print(num, "is NOT a Palindrome Number")


# =========================  FINISH  ========================
