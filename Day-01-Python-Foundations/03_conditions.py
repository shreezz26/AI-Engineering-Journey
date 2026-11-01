
# DAY 1 - TOPIC 3: CONDITIONAL STATEMENTS

# 1. Simple if
age = 20

if age >= 18:
    print("Eligible to vote")

# 2. if-else
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. if-elif-else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# 4. Nested if
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not eligible")

# 5. Multiple conditions
username = "Siri"
password = "python123"

if username == "Siri" and password == "python123":
    print("Login successful")
else:
    print("Invalid credentials")

# 6. Conditional expression
num = 8
result = "Even" if num % 2 == 0 else "Odd"
print(result)
