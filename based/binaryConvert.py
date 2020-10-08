def GetInput():
    inputStr = input("Enter a binary string:\n")
    binaryList = inputStr.strip().split(' ')
    return binaryList

def convertBinary(stringList):
    asciiResult = ""
    for x in stringList:
        decimal = int(x,2)
        asciiResult = asciiResult+chr(decimal)

    print("Resulting string: \n{0}\n".format(asciiResult))


if __name__ == "__main__":
    binaryInputString = GetInput()
    convertBinary(binaryInputString)

