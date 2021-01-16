keys = ['RED', 'WHITE', 'PURPLE', 'GREEN', 'YELLOW', 'BLUE']

def getNextKey(key):
    index = keys.index(key)
    return keys[(index + 1) % len(keys)]

dictRed = {'O': 'T', 'T': 'O', 'P': 'Y', 'Y': 'P', 'R': 'S', 'S': 'R'}
dictWhite = {'O': 'R', 'T': 'Y', 'P': 'S', 'Y': 'T', 'R': 'O', 'S': 'P'}
dictPurple = {'O': 'Y', 'T': 'S', 'P': 'R', 'Y': 'O', 'R': 'P', 'S': 'T'}
dictGreen = {'O': 'S', 'T': 'Y', 'P': 'R', 'Y': 'T', 'R': 'P', 'S': 'O'}
dictYellow = {'O': 'S', 'T': 'P', 'P': 'T', 'Y': 'R', 'R': 'Y', 'S': 'O'}
dictBlue = {'O': 'R', 'T': 'P', 'P': 'T', 'Y': 'S', 'R': 'O', 'S': 'Y'}

masterDict = {'RED': dictRed, 'WHITE': dictWhite, 'PURPLE':dictPurple,
              'GREEN':dictGreen, 'YELLOW':dictYellow, 'BLUE':dictBlue}

def generateMessages(message):

    resultDict = {}
    for key in keys:
        currentKey = key
        result=''
        for letter in message:
            result+=(masterDict[currentKey][letter])
            currentKey = getNextKey(currentKey)
        resultDict[key]=result
    return resultDict

message =  'TRRYSSPRYRYROYTOPTOPTSPSPRS'
resultDict = generateMessages(message)
print(resultDict)

