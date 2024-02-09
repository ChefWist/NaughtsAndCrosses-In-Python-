from random import randint
screen = []
for i in range(3):
    for j in range(3):
        screen.append("-")
        
def displayIdx():
    idx = 0
    for i in range(3):
        for x in range(3):
            idx+=1
            print(idx,end=" ")
        print("")
        
def display():
    idx = 0
    for i in range(3):
        for x in range(3):
            idx+=1
            print(screen[idx-1],end=" ")
        print("")
        
def placeAtIdx(index,player):
    try:
        if screen[index-1] == "-":
            screen[index-1] = player
            return True
        else:
            return False
    except IndexError:
        print("Choose a number in the range(1-9)!")
        return False
        
def UserInput():
    try:
        User = int(input("Which index: "))
        OutPut = placeAtIdx(User,"X")
    except ValueError:
        print("Use a Number!")
        UserInput()
    if OutPut == False:
        UserInput()
        
def RobotInput():
    Robot = randint(1,9)
    OutPut = placeAtIdx(Robot,"O")
    if OutPut == False:
        RobotInput()
    
def CheckWin():
    if screen[0] == "X" and screen[1] == "X" and screen[2] == "X":
        print("You Win!")
        return False
    if screen[3] == "X" and screen[4] == "X" and screen[5] == "X":
        print("You Win!")
        return False
    if screen[6] == "X" and screen[7] == "X" and screen[8] == "X":
        print("You Win!")
        return False
    if screen[0] == "O" and screen[1] == "O" and screen[2] == "O":
        print("You Lose!")
        return False
    if screen[3] == "O" and screen[4] == "O" and screen[5] == "O":
        print("You Lose!")
        return False
    if screen[6] == "O" and screen[7] == "O" and screen[8] == "O":
        print("You Lose!")
        return False
    if screen[0] == "O" and screen[3] == "O" and screen[6] == "O":
        print("You Lose!")
        return False
    if screen[1] == "O" and screen[4] == "O" and screen[7] == "O":
        print("You Lose!")
        return False
    if screen[2] == "O" and screen[5] == "O" and screen[8] == "O":
        print("You Lose!")
        return False
    if screen[0] == "X" and screen[3] == "X" and screen[6] == "X":
        print("You Win!")
        return False
    if screen[2] == "X" and screen[4] == "X" and screen[7] == "X":
        print("You Win!")
        return False
    if screen[3] == "X" and screen[5] == "X" and screen[8] == "X":
        print("You Win!")
        return False
    if screen[0] == "X" and screen[4] == "X" and screen[8] == "X":
        print("You Win!")
        return False
    if screen[2] == "X" and screen[4] == "X" and screen[6] == "X":
        print("You Win!")
        return False
    if screen[0] == "O" and screen[4] == "O" and screen[8] == "O":
        print("You Lose!")
        return False
    if screen[2] == "O" and screen[4] == "O" and screen[6] == "O":
        print("You Lose!")
        return False
    return True

win = True     
while win:
    print("-------------")
    displayIdx()
    UserInput()
    win = CheckWin()
    if win == False:
        break
    if not("-" in screen):
        print("Draw!")
        break
    RobotInput()
    win = CheckWin()
    if win == False:
        break
    display()