# Cultural influences
# on digital assets

# Culture:
#     History
#     Language
#     Beliefs/Traditions/Customs
#
#
# Why do we care abt this?:
#     Respectful
#     Inclusion
#     Sustainable

date_str = input("Input Date: ").strip()
region = input("Input Region: ").strip().upper()

def normalize(date_str, region):
    parts = date_str.split("/")
    if len(parts) != 3:
        return "Invalid"
    a, b, c = parts

    if not (a.isdigit() and b.isdigit() and c.isdigit()):
        return "Invalid"

    if region == "AU":
        day, month, year = a, b, c
    elif region == "US":
        month, day, year = a, b, c
    else:
        return "Invalid"

    if len(year) != 4:
        return "Invalid"

    return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

print(normalize(date_str, region))


Another consideration of culture when it comes to digital assets
    Symbols, Colors, Numbers





