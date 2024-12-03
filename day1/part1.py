list1 = []
list2 = []


with open('input.txt', 'r') as file:
    for line in file:
        loc1, loc2 = line.strip().split()
        list1.append(int(loc1))
        list2.append(int(loc2))

list1.sort()
list2.sort()

answer = 0

for loc1, loc2 in zip(list1, list2):
    answer += abs(loc1-loc2)

print('DONE!!!')
print(answer)