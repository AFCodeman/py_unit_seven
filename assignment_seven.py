import math

alpha = str("abcdefghijklmnopqrstuvwxyz")
list = []

def main():
    opt = str(input("Press e to encode, press d to decode, and press q to quit."))
    word= str(input("Enter text to be encoded or decoded: "))
    key = int(input("Assign a value to the key:"))
    if opt == "e":
        print(encode(key, word))
    elif opt == "d":
        print(decode(key, word))
    elif opt=="q":
        print("Your encryption has finished. Good luck!")


def encode(key, word):
    long = len(word.index())
    for letter in word(len(long)):
        new = int(alpha.index([letter+key])
        list.append(alpha[new])
    return list



def decode (key, word):
    pass





if __name__ == '__main__':
    main()