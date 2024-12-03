numSafe = 0

with open('input.txt', 'r') as file:
    for line in file:
        checkSafe = True
        increase = 0
        decrease = 0
        numList = list(map(int, line.split()))
        for i in range(len(numList)-1):
            diff = numList[i] - numList[i+1]
            if diff > 0:
                decrease += 1
            else:
                increase += 1

            if (abs(diff) < 1 or abs(diff) > 3) or (decrease and increase):
                checkSafe = False
                break

        if checkSafe:
            numSafe += 1


print("DONE!!!")
print(numSafe)