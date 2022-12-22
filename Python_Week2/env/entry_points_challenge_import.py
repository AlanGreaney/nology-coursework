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
    print(check_palindromes("banana", "palindrome"))

if __name__ == "__main__":
    main()