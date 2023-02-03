import random 

def getNumber():
    """ Gets a random number between 1 - 3
    >>> getNumber() -> 1
    """
    choice = random.randint(1,3)
    return choice


def isRock(choice):
    if choice == 1:
        return True

def isPaper(choice):
    if choice == 2:
        return True

def isScissor(choice):
    if choice == 3:
        return True


def getNumberResult(aiNumber):

    if isRock(aiNumber):
        return 1
    elif isPaper(aiNumber):
        return 2
    else:
        return 3

def getStringResult(aiNumber):
    if isRock(aiNumber):
        return "Rock"
    elif isPaper(aiNumber):
        return "Paper"
    else:
        return "Scissor"
    

def getUserChoice(userNumber):

    if isRock(userNumber):
        return "Rock"
    elif isPaper(userNumber):
        return "Paper"
    else:
        return "Scissor"

def __init__(self, score = 0):
    self._score = score
def getScore(self):
    return self._score

def setScore( self, initialScore ):
    self._score = initialScore

def getFinalResult( compChoice, userChoice):
    if compChoice == userChoice:
        print("It is a tie\n\n")
        print( "-----------------")
    elif compChoice == 1 and userChoice == 2:
        print("%s beats %s" % (getUserChoice(userChoice), getStringResult(compChoice)))
        print("You win!\n\n")
        print( "-----------------")
    elif compChoice == 2 and userChoice == 3:
        print("%s beats %s" % (getUserChoice(userChoice), getStringResult(compChoice)))
        print("You win!\n\n")
        print( "-----------------")
    elif compChoice == 3 and userChoice == 1:
        print("%s beats %s" % (getUserChoice(userChoice), getStringResult(compChoice)))
        print("You win!\n\n")
        print( "-----------------")
    else:
        print("%s beats %s" % ( getStringResult(compChoice),getUserChoice(userChoice)))
        print("Computer wins!\n\n")
        print( "-----------------")
    

aiNumber = getNumber()
score = 0
compScore = 0

##numberOfPlays = int(input("How many rounds do you want to play?"))
##
##for n in range (numberOfPlays):
play=""
while play != "q":
    aiNumber = getNumber()

    print("******----------******")
    print("Computer Score: %d" % compScore)
    print("Your score: %d" % score)

    userChoice = input("Pick from the menu: \n1: Rock\n2: Paper\n3: Scissor\n\n")
    userChoice = int(userChoice)

    print( "-----------------")
    print( "\n\nYou chose %s " % getUserChoice(userChoice))
    print( "The computer chose %s" % getStringResult(aiNumber))
    getFinalResult(aiNumber, userChoice)
    
    if getNumberResult(aiNumber) == userChoice:
        score = score
        #continue
    if getNumberResult(aiNumber) == 1 and userChoice == 2:
        score += 1
        #continue
    elif getNumberResult(aiNumber) == 2 and userChoice == 3:
        score += 1
        #continue
    elif getNumberResult(aiNumber) == 3 and userChoice == 1:
        score += 1
        #continue
    else:
        compScore += 1
        #continue

    play = input("Do you want to play again? Press q to quit: ")


print("******----------******")
print("\n\n\nComputer Score: %d" % compScore)
print("Your score: %d" % score)
print("\n\n\n******----------******")
