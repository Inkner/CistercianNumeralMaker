import os
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
    # Convert images on load to RGBA to make sure all image modes are the same
    out = Image.open('img/digit0.png').convert('RGBA')
    unitsImages = []

    for i in range(1,10):
        filename = "img/digit{}.png".format(i)
        unitsImages.append(Image.open(filename).convert('RGBA'))

    position = 0
    for element in decomposition:
        if (element > 0):
            digitImage = unitsImages[(decomposition[position])-1]
            if (position == 1):
                digitImage = ImageOps.mirror(digitImage)
            elif (position == 2):
                digitImage = ImageOps.flip(digitImage)
            elif (position == 3):
                digitImage = ImageOps.mirror(ImageOps.flip(digitImage))
            out = Image.alpha_composite(out, digitImage)
        position += 1

    out.show()
    return out

def saveImage(image, name):
    outputFolderName = "output"
    if not os.path.exists(outputFolderName):
        os.mkdir(outputFolderName)
    image.save("{}/{}.png".format(outputFolderName, name))

def main():
    inputString = getInput()
    decomposition = getNumberDecomposition(inputString)
    result = composeNumeralImage(numberString2Integers(decomposition))
    saveImage(result, inputString)

if __name__ == "__main__":
    main()
