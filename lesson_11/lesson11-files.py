# # code that read/write files
#
# print("its gonna be a good day")
#
# print("Reading file...")
#
# #open is a function that takes two paramaters
# # 1) path to the file
# # 2) the mode
# # 3) the mode: r - read, w - write, a - append
# with open("input.txt", "r") as f:
#  #  thetext = f.read() returns a block string
#     thetext = f.readlines()
#     for line_num, line in enumerate(thetext):
#         if "jade" in line:
#             print(f"Line #{line_num}: {line}")
#
#     if "jade" in thetext:
#         print("jade is there")
#         print(f"jade occurs {thetext.count("jade")} times")
#
#     print(f.read())
#
#
# with open("output.txt", "w") as f:
#     payload = "   Red is the COLOR of the day!   JUNK"
#     payload2 = "My favourite number is 5"
#     payload = payload.replace("JUNK", "")
#
#
#     payload = payload.strip()
#     payload = payload.capitalize()
#     print(payload)
#     f.write(payload + "\n")
#     f.write(payload2 + "\n")
#
with open("output.txt", "a") as f:
    payload2 = "jadey jadey jadey"
    f.write(payload2 + "\n")

with open("output.txt", "r") as f:
    mytextfile = f.readlines()
    print(f"this file has {len(mytextfile)} jade")








