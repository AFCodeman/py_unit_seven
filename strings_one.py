def half_slice(word):
    midpoint = len(word)//2
    half1 = word[:midpoint]
    half2 = word[midpoint:]
    return(half2+half1)


def no_first_last(str):
    return str[1:-1]


def longest(phrase):
    length = 0
    list = phrase.split(" ")
    for x in range(len(list)):
        if len(list[x]) > length:
            length = len(list[x])
    return length





def title_case(sentence):
    list = sentence.split(" ")
    for word in sentence (len(list)):

    return sentence


