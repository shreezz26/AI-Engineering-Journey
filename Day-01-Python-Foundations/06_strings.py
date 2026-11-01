
# DAY 1 - TOPIC 6: STRINGS

text = "Python Programming"

# 1. Accessing characters
print(text[0])
print(text[1])
print(text[-1])

# 2. String slicing
print(text[0:6])
print(text[7:])
print(text[:6])
print(text[::-1])

# 3. String length
print(len(text))

# 4. String methods
name = "  siri behara  "

print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.strip())

# 5. Replace
print(text.replace("Python", "AI"))

# 6. Find and count
print(text.find("Program"))
print(text.count("m"))

# 7. Split
sentence = "Python is easy to learn"
words = sentence.split()
print(words)

# 8. Join
joined = "-".join(words)
print(joined)

# 9. String checking
word = "Python123"

print(word.isalpha())
print(word.isdigit())
print(word.isalnum())

# 10. String formatting
name = "Siri"
age = 22

print(f"My name is {name} and my age is {age}")
