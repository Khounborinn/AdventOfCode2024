list1 = []
list2 = []


with open('input.txt', 'r') as file:
    for line in file:
        loc1, loc2 = line.strip().split()
        list1.append(int(loc1))
        list2.append(int(loc2))

answer = 0

for loc1 in list1:
    answer += (loc1 * list2.count(loc1))

print('DONE!!!')
print(answer)