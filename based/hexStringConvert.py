import codecs

def GetInput():
    inputString = input("Enter hex string:\n")
    return inputString

def ConvertHexStringToAscii(hexString):
    resultString = codecs.decode(hexString, "hex")
    print("Resulting string is:\n{0}\n".format(resultString))

if __name__ == "__main__":
    hexString = GetInput()
    ConvertHexStringToAscii(hexString)
