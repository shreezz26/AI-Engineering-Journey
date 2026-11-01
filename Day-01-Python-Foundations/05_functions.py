
# DAY 1 - TOPIC 5: FUNCTIONS

# 1. Simple function
def greet():
    print("Welcome to Python")

greet()

# 2. Function with parameters
def add(a, b):
    print(a + b)

add(10, 20)

# 3. Function with return
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)

# 4. Default arguments
def welcome(name="Siri"):
    print("Welcome", name)

welcome()
welcome("Shreelekha")

# 5. Multiple return values
def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(10, 5)

print(addition)
print(subtraction)

# 6. Local and global variables
x = 100

def display():
    y = 50
    print("Global:", x)
    print("Local:", y)

display()

# 7. Function with condition
def check_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print(check_even(10))
print(check_even(7))
