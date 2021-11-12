import math



def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    list = []
    key = int(input("Please assign a value to the key."))
    opt = str(input("Press e to encode, press d to decode, and press q to quit."))
    if opt == "e":
        encode(key)
    elif opt == "d":
        decode(key)
    elif opt=="q":
        print("Your encryption has finished. Good luck!")


def encode(key):
    for letter in word(len(word)):
        alpha[letter] = alpha.index[letter+key]
    return list



def decode (key):
    pass





if __name__ == '__main__':
    main()