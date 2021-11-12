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
    list1 = []
    for word in list:
        cap = word[:1].upper()
        rest = word[1:]
        list1.append(cap+rest)
    space = " ".join(list1)
    return space