def day4pt1():
    with open("inputs/day4.txt") as f:
        matrix = f.read().splitlines()
        score = 0
        for colIndex, row in enumerate(matrix):
            for rowIndex, element in enumerate(row):
                count = 0
                if element == "@":
                    for tries in range(1, len(row)-1):
                        if tries == 1 and colIndex -1 >= 0 and rowIndex -1 >= 0 and matrix[colIndex-1][rowIndex-1] == "@":
                            count += 1
                        elif tries == 2 and colIndex -1 >= 0 and matrix[colIndex-1][rowIndex] == "@":
                            count += 1
                        elif tries == 3 and colIndex -1 >= 0 and rowIndex +1 <= len(row)-1 and matrix[colIndex-1][rowIndex+1] == "@":
                            count += 1
                        elif tries == 4 and rowIndex -1 >= 0 and matrix[colIndex][rowIndex-1] == "@":
                            count += 1
                        elif tries == 5 and rowIndex +1 <= len(row)-1 and matrix[colIndex][rowIndex+1] == "@":
                            count += 1
                        elif tries == 6 and colIndex +1 <= len(matrix)-1 and rowIndex -1 >= 0 and matrix[colIndex+1][rowIndex-1] == "@":
                            count += 1
                        elif tries == 7 and colIndex +1 <= len(matrix)-1 and matrix[colIndex+1][rowIndex] == "@":
                            count += 1
                        elif tries == 8 and colIndex +1 <= len(matrix)-1 and rowIndex +1 <= len(row)-1 and matrix[colIndex+1][rowIndex+1] == "@":
                            count += 1
                        if tries == 8 and count < 4:
                            score +=1
                            break
                        if count >= 4:
                            break
        print(score)

def day4pt2():
    with open("inputs/day4.txt") as f:
        matrix = f.read().splitlines()
        score = 0
        checkRolls = True
        while checkRolls:
            tempScore = 0
            for colIndex, row in enumerate(matrix):
                for rowIndex, element in enumerate(row):
                    count = 0
                    if element == "@":
                        for tries in range(1, len(row)-1):
                            if tries == 1 and colIndex -1 >= 0 and rowIndex -1 >= 0 and matrix[colIndex-1][rowIndex-1] == "@":
                                count += 1
                            elif tries == 2 and colIndex -1 >= 0 and matrix[colIndex-1][rowIndex] == "@":
                                count += 1
                            elif tries == 3 and colIndex -1 >= 0 and rowIndex +1 <= len(row)-1 and matrix[colIndex-1][rowIndex+1] == "@":
                                count += 1
                            elif tries == 4 and rowIndex -1 >= 0 and matrix[colIndex][rowIndex-1] == "@":
                                count += 1
                            elif tries == 5 and rowIndex +1 <= len(row)-1 and matrix[colIndex][rowIndex+1] == "@":
                                count += 1
                            elif tries == 6 and colIndex +1 <= len(matrix)-1 and rowIndex -1 >= 0 and matrix[colIndex+1][rowIndex-1] == "@":
                                count += 1
                            elif tries == 7 and colIndex +1 <= len(matrix)-1 and matrix[colIndex+1][rowIndex] == "@":
                                count += 1
                            elif tries == 8 and colIndex +1 <= len(matrix)-1 and rowIndex +1 <= len(row)-1 and matrix[colIndex+1][rowIndex+1] == "@":
                                count += 1
                            if tries == 8 and count < 4:
                                matrix[colIndex] = matrix[colIndex][:rowIndex]+"."+matrix[colIndex][rowIndex+1:]
                                tempScore +=1
                                break
                            if count >= 4:
                                break
            if tempScore > 0:
                score += tempScore
            else:
                checkRolls = not checkRolls
        print(score)



if __name__ == "__main__":
    day4pt2()