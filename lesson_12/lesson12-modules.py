import math
import random
import time

random.seed(12)
print(random.random)

# def pythag():
#     print("Welcome to the Pythagoras Calculator!, Input your two leg lengths to find the hypotenuse length.")
#     a = float(input("First Length: "))
#     b = float(input("Second Length: "))
#
#     print(f"Length of hypotenuse: {(a ** 2 + b ** 2) ** 0.5}")

# pythag()

# using other people python to make our prgrams more concise

print(f"hypotenuse: {math.hypot(3,4)}")

print(f"Square root of 4 is {pow(4,2)}")
print(f"Square root of 4 is {math.pow(4,2)}")

print(f"Five factorial is {math.factorial(5)}")

print(random.random()) # returns a number in [0.0, 1.0)

print(random.randint(1,6))

students = ["Jade", "Willow", "Baden", "Drew"]
random.shuffle(students)
print(f"Random student from the list: {random.choice(students)}")

print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

print("Simulating Compute Heavy Task")
time.sleep(10)
print("Done!")
