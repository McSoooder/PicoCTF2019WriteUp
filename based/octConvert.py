def GetInput():
    inputString = input("Enter oct. numbers:\n")
    octInput = inputString.strip().split(' ')
    return octInput

def ConvertOct(stringList):
    resultString = ""
    for x in stringList:
        decimal = int(x,8)
        resultString = resultString +chr(decimal)

    print("Oct. converted to characters:\n{}\n".format(resultString))

if __name__ == "__main__":
    octInputStrings = GetInput()
    ConvertOct(octInputStrings)
