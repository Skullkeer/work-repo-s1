# what is an iterable
# what is a generator
# what is list comprehension

list_nums = [1, 2, 3, 4, 5]
for num in list_nums:
    print(num)

#lists and strings are iterable: can be dropped into a for loop

d = {"Willow:": 98, "Jade:": 100, "Drew:": 20}

for key in d:
    print(key)

for key in d.values():
    print(key)

for key, value in d.items():
    print(f"{key} {value}")

student_list = [
    "willow",
    "jade",
    "drew",
    "baden",
    "david",
    ]

print(student_list)

# we already know we can iterate over a list
for name in student_list:
    print(name)

# we can use enumerate() to iterate and number
for number, name in enumerate(student_list, start=1):
    print(f"student_list {number}: {name}")

# generator

#count to 10 with range()
for num in range(0, 11):
    print(num, end=' ')
print()

#the sqaures
for num in range(0, 11):
    print(num*num, end=' ')
print()

#the sqaures
for num in range(0, 11):
    print(num*num*num, end=' ')
print()

#another way
for num in range(0, 11):
    print(num**3, end=' ')
print()

#here is a generator that returns all the even numbers you could want
#we use the even numbers as an example of something hard to calc

def only_evens(iterable):
    for x in iterable:
        if x % 2 == 0:
            yield x

#here is a generator that returns all the squares you could want
#we use the even numbers as an example of something hard to calc

def only_squares(iterable):
    for x in iterable:
        yield x ** 2

def counter(start, stop):
    i = start
    while i <= stop:
        yield i
        i += 1

print("generator")
gen = counter(3, 7)
for v in gen:
    print(v, end=' ')
print("\n\n")

pipeline = only_squares(only_evens(counter(1, 10)))
for v in pipeline:
    print(v, end=' ')
print()

# list comprehension
list_squares = [i * i for i in range(5)]
print(list_squares)

list_doubles = [i * 2 for i in range(5, 11)]
print(list_doubles)

#even numbers 0-20
list_evens = [i for i in range(0, 21) if i % 2 == 0]
print(list_evens)

#old fasion way (for more complex stuff)
list_evenss = []
for i in range(0, 21):
    if i % 2 == 0:
        list_evenss.append(i)

print(f"Old fashioned way: {list_evenss}")
