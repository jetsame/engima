# coding=utf-8
import random

# positions of rotors
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# main alphabet
characters = [[4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9],  # R1
              [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4],  # R2
              [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14],  # R3
              [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]]  # REF

# letters for each rotor
random1, random2, random3 = random.randrange(0, 25), random.randrange(0, 25), random.randrange(0, 25)
print(random1, '    ', random2, '    ', random3)
global newed


def limit(x):
    """
    :param x: some value
    :return: right value of x
    """
    if x > 25:
        while x > 25:
            x -= 26
    else:
        while x < 0:
            x += 26
    return x


# function that helps with going beyond

def encryptndecrypt(letters, word):
    """
    :param letters: letter of alphabet in massive
    :param word: input word
    :return: coded word
    """

    newed = []
    attlist = [x for x in letters]

    offset1 = [attlist[c1] for c1 in characters[0]]
    offset2 = [attlist[c2] for c2 in characters[1]]
    offset3 = [attlist[c3] for c3 in characters[2]]
    reflector = [attlist[c4] for c4 in characters[3]]

    for i in word:

        def need(x1, x2):
            """
            :param x1: first value
            :param x2: second value
            :return: depending on the sign of the number
            """
            if x1 - x2 < 0:
                return 26 + (x1 - x2)
            return 26 - (x1 - x2)

        if i != ' ':
            idofletter = alphabet.index(i)
            operation1 = limit(random1 + idofletter)

            operation2 = limit(attlist.index(offset1[operation1]) + (random2 - random1))

            operation3 = limit(attlist.index(offset2[operation2]) + need(random2, random3))

            reflectoralph = limit(attlist.index(offset3[operation3]) - random3)
            transition = reflector[reflectoralph]
            backward = attlist.index(transition)

            operation11 = limit(backward + random3)
            bwoperation1 = offset3.index(attlist[operation11])

            operation21 = limit(bwoperation1 - need(random2, random3))
            bwoperation2 = offset2.index(attlist[operation21])

            operation31 = limit(bwoperation2 - (random2 - random1))
            bwoperation3 = offset1.index(attlist[operation31])

            operation01 = limit(bwoperation3 - random1)
            bwoperation0 = attlist[operation01]
            newed.append(bwoperation0)

        else:
            print('')
            newed.append(' ')
    print(''.join(newed))


# main function/brain of program

encryptndecrypt(alphabet, 'GITHUB')
