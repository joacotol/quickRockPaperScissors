
def getNumber():

    import random 

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




def getResult(aiNumber):

    if isRock(aiNumber):
        return 1
    elif isPaper(aiNumber):
        return 2
    else:
        return 3

def getUserChoice(userNumber):

    if isRock(aiNumber):
        return "Rock"
    elif isPaper(aiNumber):
        return "Paper"
    else:
        return "Scissor"

aiNumber = getNumber()
score = 0
compScore = 0


while(True):
    print(getResult(aiNumber))

    print("******----------******")
    print("Computer Score: %d" % compScore)
    print("Your score: %d" % score)

    userChoice = input("Pick from the menu: \n1: Rock\n2: Paper\n3: Scissor\n")
    print("Press 'Q' to quit")
    if str(userChoice) == "Q":
        break
    else:
        int(userChoice)

    if getResult(aiNumber) == userChoice:
        print("It is a tie")
        continue
    elif getResult(aiNumber) == 1 and userChoice == 2:
        print("You win!")
        score += 1
        continue
    elif getResult(aiNumber) == 2 and userChoice == 3:
        print("You win!")
        score += 1
        continue
    elif getResult(aiNumber) == 3 and userChoice == 1:
        print("You win!")
        score += 1
        continue
    else:
        print("Computer wins!")
        compScore += 1
        continue


