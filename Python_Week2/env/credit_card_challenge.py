#1.  Write a function in Python that accepts a credit card number. 
#It should return a string where all the characters are hidden with an asterisk 
#except the last four. For example, if the function gets sent "4444444444444444", 
#then it should return "***********4444"

def convertCc(num):
    stringVersion = str(num)
    for index, item in enumerate(stringVersion):
        if index < len(stringVersion) - amt:
            stringVersion = stringVersion.replace(item, "*", 1)

    return stringVersion


def convertCcSmall(num):
    amt = 4
    return ((len(str(num))-amt) * "*") + str(num)[-amt:] #[start_index_pos : end_index_pos : step_size]

amt = 4 #how many to leave unhidden

print(convertCc(4444444444444444))
print(convertCc(6455435435435433))
print(convertCc(7393894938274832))
print(convertCcSmall(4444444444444444))
print(convertCcSmall(6455435435435433))
print(convertCcSmall(7393894938274832))
