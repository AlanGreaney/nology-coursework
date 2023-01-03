import sys
import math
import time

def gamePrint(text, char = "*", lastRepeated = "", width = 150, buffer = 5):
    if lastRepeated != char:
        print(char * width)
        lastRepeated = char
    print(char + (" " * (width - len(char)*2)) + char)

    currentLine = ""
    index = 0
    words = text.split()
    while index < len(words):
        if len(currentLine + " " +  words[index]) < width - (len(char)*2 + buffer*2):
            currentLine += " " +  words[index]
            index += 1
        else:
            centerPrint(currentLine, char, width, buffer)
            currentLine = ""

    if len(currentLine) > 0:
        centerPrint(currentLine, char, width, buffer)

    print(char + (" " * (width - 2)) + char)
    print(char * width)

    return lastRepeated

def centerPrint(currentLine, char, width, buffer):
    output = char + (" " * buffer)
    textWidth = len(currentLine) + len(char)*2 + buffer*2
    extraBufferLeft = math.floor((width - textWidth)/2)
    extraBufferRight = math.ceil((width - textWidth)/2)
    
    output += (" " * extraBufferLeft) + currentLine + (" " * extraBufferRight)

    output += (" " * buffer) + char
    print(output)

def displayAscii(fileName):
    f = open('ascii/' + fileName, 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

def delay(length, blanks = 1):
    sys.stdout.flush()
    time.sleep(length)
    while blanks > 0:
        print("")
        blanks -=1
    sys.stdout.flush()

def main():
    displayAscii("bridge1.txt")
    gamePrint("This is a test. Testing 123. It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
    gamePrint("The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).")
    gamePrint("you died lol", "!")
    gamePrint("you died lol", "!")
    gamePrint("The math.ceil() method rounds a number UP to the nearest integer, if necessary, and returns the result.", "?")

if __name__ == "__main__":
    main()