
# DAY 1 - TOPIC 7: LISTS

# 1. Creating lists
numbers = [10, 20, 30, 40, 50]
print(numbers)

# 2. Accessing elements
print(numbers[0])
print(numbers[-1])

# 3. Modifying elements
numbers[0] = 100
print(numbers)

# 4. Adding elements
numbers.append(60)
numbers.insert(1, 15)
print(numbers)

# 5. Removing elements
numbers.remove(30)
numbers.pop()
print(numbers)

# 6. List length
print(len(numbers))

# 7. Sorting
values = [40, 10, 30, 20]
values.sort()
print(values)

values.reverse()
print(values)

# 8. Counting and finding
items = [10, 20, 10, 30, 10]

print(items.count(10))
print(items.index(20))

# 9. Loop through a list
for item in items:
    print(item)

# 10. List comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

# 11. Filtering even numbers
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# 12. Nested list
matrix = [
    [1, 2],
    [3, 4]
]

print(matrix[0][1])
