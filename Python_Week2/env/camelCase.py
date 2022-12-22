import re #regular expression module

def to_camel_case(text):
    #words = re.split("-|_", text)
    #words = text.split("-") if len(text.split("-")) > 1 else text.split("_")
    words = text.split("-" if "-" in text else "_")

    finalWord = ""
    for index, item in enumerate(words):
        if(index == 0):
            finalWord += item
        else:
            finalWord += item.capitalize()

    return finalWord

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case(""))
print(to_camel_case("A-B-C"))

    