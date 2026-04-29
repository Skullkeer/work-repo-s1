import sys

# Ak the user to input number
# If/else chain - check if the number is greater than 0 (print greater than 0)
# Otherwise print 'not greater than 0'
# a = input("Quotient: ")
# b = input("Divisor: ")
#
# # if a > 0:
# #    print("Larger Than Zero")
# # else:
# #    print("Smaller than zero")
#
# try:
#     a = int(a)
#     b = int(b)
#     floor_quotient = a / b
# except ZeroDivisionError as e:
#     print(f"Error: {e}")
#     exit(1)
# except ValueError as e:
#     print(f"Error: {e}")
#     exit(1)
# else: #executes when everything is good
#     print(f"finally you got it right user, heres the answer: {floor_quotient}")
# finally:
#     print("This happens no matter what")

# handling errors
# lvl 0 programmer: if else
# lvl 1 programmer: try except
# lvl 2 programmer: validate input (after optional normalizing)

# user must enter valid number (0, 100) inclusive

inp = input("Enter a number betweenb 0-100: ")

#validate number thow a custom exeption
def validate_number_in_range(user_number):
    if user_number < 0 or user_number > 100:
        raise ValueError(f"Your number {user_number} is not is [0, 100]")

try:
    inp = int(inp)
    validate_number_in_range(inp)
except ValueError as e:
    print("wrong")
    print(f"Specific error: {e}")
    exit(1)


try:
    pass
except Exception as e: #super exception
    pass
