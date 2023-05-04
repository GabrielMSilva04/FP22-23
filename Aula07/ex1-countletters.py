letters = {}

def loadFile(fname):
    with open(str(fname)) as file:
        for line in file:
            for letter in line:
                letter=letter.lower()
                if letter.isalpha():
                    if letter not in letters:
                        letters[letter] = 1
                    else:
                        letters[letter] += 1
    return letters

def printoutput(dictionary):
    sortlist = sorted(dictionary.items())
    for output in sortlist:
        print(output[0],output[1])



def main(args):
    printoutput(loadFile(args))

import sys
if __name__ == "__main__":
    main(sys.argv[1])