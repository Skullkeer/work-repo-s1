name = str(input("Please Enter Your First Name and Age: "))

list1 = name.split(" ")

try:
    age = int(list1[1])
    name = str(list1[0])
    correct_name = name.capitalize()
    print(f"Name: {correct_name} | Age: {age}")
except ValueError:
    print("Invalid Age")

print(list1)
