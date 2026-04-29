text = input("Input Text: ")
data_type = input("Input Data Type: ")

def convert(txt, data):
    if data == "int":
        try:
            return int(txt)
        except ValueError:
            return "Cannot convert to integer"

    elif data == "str":
        try:
            return str(txt)
        except:
            return "Error"


print(convert(text, data_type))




