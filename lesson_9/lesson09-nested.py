#nested data structures

#recall you can store lists within lists
l =[[1], [2,3]] #length of l = 2

print(f"Starting With: {l}")

l.append([])
print(f"after appending: {l}")

#we slice the outer list to access the nested ones

l_0 = l[0]
print(f"Zeroeth sublist: {l_0}")

l_0.append(5)
print(f"l_0 after appending: {l_0}")
print(f"l after appending: {l}")

l_2 = l[2]
print(f"second sublist: {l_2}")
l_2.append(100)
print(f"l after appending: {l}")

l[2].append(200)
print(f"l after appending: {l}")

total_elements = 0
for sublist in l:
    total_elements += len(sublist)
    print(f"{sublist} = {len(sublist)} elements")

print(f"Grand Total: {total_elements}")

#application simple 2d game

gameboard = [
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
        [".", ".", ".", ".", "."],
]

pc = "X"
gameboard[2][2] = pc

enemy = "O"
gameboard[0][0] = enemy

def locate(character, gameboard):
    current_col = 0
    current_row = 0
    for row_num, row in enumerate(gameboard):
        for col_num, col in enumerate(row):
            if col == pc:
                current_col = col_num
                current_row = row_num
                return (current_col, current_row)

def moveup(character, gameboard):
    old_pos = locate(character, gameboard)
    row_num = old_pos[0]
    col_num = old_pos[1]
    gameboard[row_num][col_num] = "."
    gameboard[row_num-1][col_num] = character


print(f"Locate PC: {locate(pc, gameboard)}")

for row in gameboard:
    print("".join(row))

print("After move up event")
moveup(pc, gameboard)
for row in gameboard:
    print("".join(row))

scores = {
        "willow": [20, 20],
        "drew": [50, 60],
        "jade": [100, 99]
}

subjects = {
        "willow": "This class",
        "drew": "Music",
        "jade": "Physics"
}

#Report card
#e.g. willow got ... in this class


for k, v in scores.items():
    print(f"Item 1: {k} got {v[0]} in {subjects[k]}")
    print(f"{k} got {v} in {subjects[k]}")
