
# DAY 1 - TOPIC 4: LOOPS

# 1. For loop
for i in range(1, 6):
    print(i)

# 2. Range examples
for i in range(5):
    print(i)

for i in range(2, 11, 2):
    print(i)

# 3. While loop
i = 1

while i <= 5:
    print(i)
    i += 1

# 4. Break statement
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 5. Continue statement
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 6. Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# 7. Sum using a loop
total = 0

for i in range(1, 6):
    total += i

print("Total:", total)

# 8. Multiplication table
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
