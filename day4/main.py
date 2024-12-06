def recursiveCheckXmas(word, matrix, i, j, di, dj) -> int:
    # Check if the word is XMAS, then keep checking the rest of the line
    if word == 'XMAS':
        return 1
    # If i or j has reached the edge, then false
    # also if the current word is within XMAS
    # All of these return false
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) or not 'XMAS'.startswith(word):
        return 0

    return recursiveCheckXmas(word + matrix[i][j], matrix, i + di, j + dj, di, dj) 

def recursiveCheckMas(word, matrix, i, j, di, dj) -> int:
    # Check if the word is XMAS, then keep checking the rest of the line
    if word == 'MAS' or word == 'SAM':
        return True
    # If i or j has reached the edge, then false
    # also if the current word is within MAS ans SAM
    # All of these return false
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]):
        return False
    if (not 'SAM'.startswith(word)) and (not 'MAS'.startswith(word)):
        return False

    return recursiveCheckMas(word + matrix[i][j], matrix, i + di, j + dj, di, dj) 
      


def part1() -> int:
    answer = 0

    matrix = [];
    with open('input.txt', 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                answer += (recursiveCheckXmas('', matrix, i, j, -1, 0) +
                            recursiveCheckXmas('', matrix, i, j, 1, 0) +
                            recursiveCheckXmas('', matrix, i, j, 0, 1) +
                            recursiveCheckXmas('', matrix, i, j, 0, -1) +
                            recursiveCheckXmas('', matrix, i, j, 1, 1) +
                            recursiveCheckXmas('', matrix, i, j, 1, -1) +
                            recursiveCheckXmas('', matrix, i, j, -1, 1) +
                            recursiveCheckXmas('', matrix, i, j, -1, -1))
                


    return answer


def part2():
    answer = 0

    matrix = [];
    with open('input.txt', 'r') as file:
        for line in file:
            matrix.append(list(line.strip()))
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'A':
                if recursiveCheckMas('', matrix, i-1, j-1, 1, 1) and recursiveCheckMas('', matrix, i-1, j+1, 1, -1):
                    answer += 1
    
    return answer


print(part1())
print(part2())