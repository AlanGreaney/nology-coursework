import entry_points_challenge_import

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

def main():
    print(check_palindromes("civic", "racecar", "banana", "palindrome"))

    testWord1 = "not a palindrome"
    testWord2 = "racecar"
    testWord3 = "civic"
    testWord4 = "banana"
    print(is_palindrome(testWord1))
    print(is_palindrome(testWord2))
    print(entry_points_challenge_import.is_palindrome(testWord3))
    print(entry_points_challenge_import.is_palindrome(testWord4))

if __name__ == "__main__":
    main()