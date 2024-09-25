ProjectName = "PasswordGenerator"
import random 
characterType =  (1,2,3,4)
firstList = ("1","2","3","4","5","6","7","8","9","0")
secondList = ("!","@","#","$","%","^","&","*","(",")","<",">","]","[")
ThirdList = ("q","w","e","r","t","y","u","i","o","p","a","s","d","f","g")
fourthList = ("Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G")
password = list()

passwordLength = random.randrange(14,15)
def makingPas(passwordLength1):  
 password = list()
 while passwordLength1 != 0:
        x = random.randrange(1,5)
        if x == 1:
            rndN = random.randrange(0, len(firstList))
            password.append(firstList[rndN])
        if x == 2:
            rndN = random.randrange(0, len(secondList))
            password.append(secondList[rndN])
        if x == 3: 
            rndN = random.randrange(0, len(ThirdList))
            password.append(ThirdList[rndN])
        if x == 4:
            rndN = random.randrange(0, len(fourthList))
            password.append(fourthList[rndN])

        passwordLength1 -= 1
 return password
def checkPassword(password):
    x1 = 0
    x2 = 0
    x3 = 0
    x4 = 0
    for x in password:
        if x in firstList:
            x1 += 1
    for x in password:
        if x in secondList:
            x2 += 1
    for x in password:
        if x in ThirdList:
            x3 += 1
    for x in password:
        if x in fourthList:
            x4 += 1
    if x1 == 0 or x2 == 0 or x3 == 0 or x4 == 0:
        return 0
    else:
        return 1
def start():
 global password
 passwordGood = 0
 while passwordGood != 1:
    password = makingPas(passwordLength)
    x = checkPassword(password)
    if x == 1:
        break
start()
readyToUsePassword = str()
readyToUsePassword = "".join(password)
print(readyToUsePassword)


    





    