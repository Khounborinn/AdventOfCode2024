import re

def part1() -> int:
    answer = 0

    with open('input.txt', 'r') as file:
        corruptedData = file.read()

    mulList = re.findall("mul\(\d*,\d*\)", corruptedData)
    answer = multiply(mulList)
    return answer


def part2() -> int:
    with open('input.txt', 'r') as file:
        corruptedData = file.read()
    mulList = re.findall("do\(\)|mul\(\d*,\d*\)|don\'t\(\)", corruptedData)
    answer = multiply(mulList)
    return answer

def multiply(mulList) -> int:
    answer = 0
    checkMultiply = True
    for mul in mulList:
        if mul == "do()":
            checkMultiply = True
        elif mul == "don't()":
            checkMultiply = False
        elif checkMultiply:
            numbers = re.findall("\d+", mul)
            x, y = [int(num) for num in numbers]
            answer += (x*y)

    return answer


print(part1())
print(part2())