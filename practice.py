#list.reverse()
#list.append(50)

#print(list)

# tup = (50,50,40)
# print(tup.count(50))
# print(len(tup))
# print(tup)

# dict = {
#     "name": "Shreyan",
#     "age": "20",
#     "marks": [90,80,95,86,79]

# }

# dict["name"] = "Josheph"
# print(dict["name"])

# set = {1,2,3,"ram","sita"}
# set.update()
# set.remove(1)
# set.add(10)

# print(set)


# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}
# froset1 = frozenset(set1)
# froset2 = frozenset(set2)

# print(froset1)
# print(froset2)
# print(froset2.intersection(froset1))

# # print(set1)

# from collections import deque
# dq = deque([1,2,3,2,4,5])
# dq.append(8)
# dq.appendleft(9)
# dq.remove(2)

# print(dq)


# d = {x: x**2 for x in range(5)}
# print(d)

# marks = [60,70,80,90]
# def s_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif 90>marks>=80:
#         return "B"
#     elif 80>marks>70:
#         return "C"
#     else:
#         return "D"
# grade = map (s_grade, marks) 
# print(f"student marks {marks}")
# print("student Grade", next(grade))
# print("student Grade", next(grade))
# print("student Grade", next(grade))

# print("student Grade", next(grade))

# from functools import reduce
# num = [2,4,5,8]
# def my_sum(x, y):
#     return x + y
# sum = reduce( my_sum, num) 
# print(sum)

# try:
#     print("Trying to access an element")
#     print(num[5])
# except IndexError:
#     print("Index out of range error occurred")
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     print("This block always executes, regardless of an error")
# print("End of the program")

# rock paper scissors game
# import random

# def play_game():
#     choices = ["rock", "paper", "scissors"]
#     user_choice = input("Enter rock, paper, or scissors: ").lower()
    
#     if user_choice not in choices:
#         print("Invalid choice! Please try again.")
#         return play_game()
    
#     computer_choice = random.choice(choices)
#     print(f"Computer chose: {computer_choice}")
    
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == "rock" and computer_choice == "scissors") or \
#          (user_choice == "paper" and computer_choice == "rock") or \
#          (user_choice == "scissors" and computer_choice == "paper"):
#         print("You win!")
#     else:
#         print("You lose!")

# play_game()

# class student:
#     def data(self, name, age):
#         self.name = name
#         self.age = age

# s1 = student()
# s1.data("Shreyan", 20)

# print(f"Name: {s1.name}, Age: {s1.age}")


# class Point:
#     def __init__(self, x):  
#         self.x = x

#     def __add__(self, other):  
#         return Point(self.x + other.x)

# # Creating two point objects
# p1 = Point(3)
# p2 = Point(4)

# # Adding them using the overloaded '+' operator
# p3 = p1 + p2

# # Output the x value of the resulting point
# print(p3.x)


# Example of method overriding in Python

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# d = Dog()
# print(d.speak())  


# class User:
#     def __init__(self, role):
#         self.role = role

    
# def create_user(role):
#     return User(role)
    
# u = create_user("admin")
# print(u.role)  
        
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)


       