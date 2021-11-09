

def main():
    word = str(input("Feed me word. "))
    printingLetters(word)

def upperLower(word):
    print(word.upper())
    print(word.lower())

def printingLetters(word):
    for x in word:
        print(x)

if __name__ == '__main__':
    main()
