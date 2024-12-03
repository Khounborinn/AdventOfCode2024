def checkList(numList):
    increase = 0
    decrease = 0
    for i in range(len(numList)-1):
        diff = numList[i] - numList[i+1]
        if diff > 0:
            decrease += 1
        else:
            increase += 1

        if (abs(diff) < 1 or abs(diff) > 3) or (decrease and increase):
            return False
    
    return True

numSafe = 0

with open('input.txt', 'r') as file:
    for line in file:
        numList = list(map(int, line.split()))
        if checkList(numList):
            numSafe += 1
        else:
            for i in range(len(numList)):
                newList = numList[:i]
                newList.extend(numList[i+1:])
                if checkList(newList):
                    numSafe += 1
                    break
    

print("DONE!!!")
print(numSafe)