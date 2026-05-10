int1 = int(input("Enter first integer: "))

int2 = int(input("Enter second integer: "))

print(f"You entered {int1} and {int2}")

if int1 > 0:
    print("first number: positive")

elif int1 == 0:
    print("first number: zero")

else:
    print("first number: negative")

if int2 > 0:
    print("second number: positive")

elif int2 == 0:
    print("second number: zero")

else:
    print("second number: negative")

if int1 % 2 == 0:
    print("first number: even")

else:
    print("first number: odd")

if int2 % 2 == 0:
    print("second number: even")

else:
    print("second number: odd")

if int1 > int2:
    print("the first number is greater than the second")

elif int1 == int2:
    print("the numbers are equal")

else:
    print("the first number is smaller than the second")

print(f"Sum: {int1 + int2}")

print(f"Difference: {int1 - int2}")

print(f"Product: {int1 * int2}")

if int2 != 0:
    if int1 % int2 == 0:
        print("First number is divisible by second number")
        print(int1 / int2)
else:
    print("error")

