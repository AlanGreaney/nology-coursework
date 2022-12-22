from functools import reduce

def my_first_function(textInput):
    print("I love " + textInput + "!")

my_first_function("functions")

###

the_following_list = [2, 5, 7, 32, 100, 9, 56, 74, 97, 22, 13, 80]

list_but_evens = list(filter(lambda x: x % 2 == 0, the_following_list))

list_but_by_three = list(map(lambda x: x * 3, the_following_list))

list_but_summed = reduce((lambda a, b: a + b), the_following_list)

print(the_following_list)
print(list_but_evens)
print(list_but_by_three)
print(list_but_summed)

###

def is_palindrome(testWord):
    if len(testWord) <= 1:
        return True
    elif testWord[0] != testWord[-1]:
        return False
    else:
        return is_palindrome(testWord[1:-1])

def check_palindromes(*palindromeList):
    palindrome_outputs = []
    for word in palindromeList:
        palindrome_outputs.append(is_palindrome(word))

    return palindrome_outputs


print(check_palindromes("civic", "racecar", "banana", "palindrome"))

