import string 

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def string_with_commas(inputStr):
    newStr = ""
    sign = ""
    # input sanitization: remove spaces, if string has spaces drop spaces
    # if number has special characters return NULL string.
    # if number starts with (-) print output with sign, incase number starts with (+) drop (+)
    inputStr = inputStr.strip()
    inputStr = "".join(inputStr.split(" "))
    invalidcharacters= set(string.punctuation)
    invalidcharacters.remove('-')
    invalidcharacters.remove('+')
    if any(char in invalidcharacters for char in inputStr):
        return ""
    if inputStr.startswith('-') or inputStr.startswith('+'):
        if inputStr[0] == '-':
            sign = '-'
        inputStr = inputStr[1:]

    # input sanity checked
    strLen = len(inputStr)

    if strLen <4:
        return sign + inputStr
    reversedInput = reverse(inputStr)
    first_comma = 0
    while strLen > 2:
        if not first_comma:
            newStr = reversedInput[0:3] + ','
            strLen = strLen -3
            first_comma = 1
            reversedInput = reversedInput[3:]
        else:
            newStr = newStr + reversedInput[0:2] + ','
            strLen = strLen - 2
            reversedInput = reversedInput[2:]
    return sign + reverse(newStr + reversedInput)

if __name__ == '__main__':
    print(string_with_commas("-9"))
