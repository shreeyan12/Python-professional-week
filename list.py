# 1. List – Ordered, Mutable, Duplicates Allowed
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")       # Add
fruits.insert(1, "mango")     # Add at position
fruits.remove("banana")       # Remove by value
fruits.pop()                  # Remove last
fruits[0] = "grape"           # Modify
print(fruits)

#list functions

print(len(fruits), fruits.index("cherry"), fruits.count("apple"))
fruits.sort()
fruits.reverse()

#list loop

for fruit in fruits:
    print(fruit)



