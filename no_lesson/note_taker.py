name = input("Input File Name: ")
path = f"/home/s0654313/work/notes/{name}"
while True:
    inp = input("Notes: ")

    if inp == "q":
        print("Exiting...")
        exit()

    if inp == "del":
        with open(path, "r", encoding="utf-8") as f:


    with open(path, "a", encoding="utf-8") as f:
        f.write(inp + "\n")
