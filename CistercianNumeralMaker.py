import sys
from PIL import Image
from PIL import ImageOps

# Limits determined by the Cistercian numeral system
LOWER_LIMIT = 0
UPPER_LIMIT = 9999

def inputIsValid (inputString):
    if (not(inputString.isnumeric())):
        return False
    inputInteger = int(inputString)
    if (not(isinstance(inputInteger, int))):
        return False
    if (inputInteger < LOWER_LIMIT):
        return False
    if (inputInteger > UPPER_LIMIT):
        return False
    return True

def getInput():
    print("\nWelcome to Cistercian Numeral Maker")

    inputString = "-1"
    while (not(inputIsValid(inputString))):
        phrase = "Please enter a integer number on the range [{}, {}]"
        print(phrase.format(LOWER_LIMIT, UPPER_LIMIT))
        inputString = input()

    print("Introduced number is {}".format(inputString))

    return inputString

def getNumberDecomposition(numberString):
    number = int(numberString)

    # Decompose the number in its units, tens, hundreds and thousands
    decomposition = [numberString[len(numberString) - 1]]

    for i in range(1, 4):
        if (number >= pow(10, i)):
            decomposition.append(numberString[len(numberString) - (i + 1)])
    return decomposition

def numberString2Integers(list):
    integerList = []
    for element in list:
        integerList.append(int(element))
    return integerList

def composeNumeralImage(decomposition):
    background = Image.open('test_bg.png')
    # Background image needs conversion to RGBA mode
    background = background.convert('RGBA')
    base = Image.open('test_0.png')
    unitsImages = []

    for i in range(1,10):
        filename = "test_{}.png".format(i)
        unitsImages.append(Image.open(filename))

    out = Image.alpha_composite(background, base)

    if (decomposition[0] > 0):
        out = Image.alpha_composite(out, unitsImages[(decomposition[0])-1])

    if (len(decomposition) > 1 and decomposition[1] > 0):
        out = Image.alpha_composite(out, ImageOps.mirror(unitsImages[(decomposition[1])-1]))

    if (len(decomposition) > 2 and decomposition[2] > 0):
        out = Image.alpha_composite(out, ImageOps.flip(unitsImages[(decomposition[2])-1]))

    if (len(decomposition) > 3 and decomposition[3] > 0):
        out = Image.alpha_composite(out, ImageOps.mirror(ImageOps.flip(unitsImages[(decomposition[3])-1])))

    out.show()

def main():
    inputString = getInput()
    decomposition = getNumberDecomposition(inputString)
    composeNumeralImage(numberString2Integers(decomposition))

if __name__ == "__main__":
    main()
