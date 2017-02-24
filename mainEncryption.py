rawUserInput = input("enter text: ")
userInput = rawUserInput

def makeUpperCase():
    global userInput
    userInput = userInput.upper()




def splitInput():
    global userInput
    userInput = list(userInput)

def testChars():
    print("test")

testChars()
makeUpperCase()
splitInput()
print(userInput)