
# DAY 1 - TOPIC 2: PYTHON OPERATORS

a = 10
b = 3

# 1. Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# 2. Comparison operators
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# 3. Logical operators
x = 20
print(x > 10 and x < 30)
print(x > 30 or x < 25)
print(not(x > 10))

# 4. Assignment operators
num = 10
num += 5
print(num)

num -= 2
print(num)

num *= 2
print(num)

# 5. Membership operators
language = "Python"
print("P" in language)
print("z" not in language)

# 6. Identity operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 == list3)

# 7. Operator precedence
result = 10 + 5 * 2
print(result)

result = (10 + 5) * 2
print(result)
