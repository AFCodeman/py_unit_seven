import math

alpha = str("abcdefghijklmnopqrstuvwxyz")

def main():
    opt = str(input("Press e to encode, press d to decode, and press q to quit."))
    word= str(input("Enter text to be encoded or decoded: "))
    key = int(input("Assign a value to the key:"))
    if opt == "e":
        print(encode(key,word))
    elif opt == "d":
        print(decode(key,word))
    elif opt=="q":
        print("Your encryption has finished. Good luck!")


def encode(key, word):
    alpha = str("abcdefghijklmnopqrstuvwxyz")
    blank = ""
    for letter in word:
        numb = alpha.index(letter)
        newNumb = (numb + key)%26
        blank += alpha[newNumb]
    return blank




def decode (key, word):
    alpha = str("abcdefghijklmnopqrstuvwxyz")
    blank = ""
    for letter in word:
        numb = alpha.index(letter)
        newNumb = (numb - key) % 26
        blank += alpha[newNumb]
    return blank





if __name__ == '__main__':
    main()