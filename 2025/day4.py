import array


def day4pt1():
    with open("inputs/day4test.txt") as f:
        l = f.read()
        col = l.split('\n')
        columns = [c.split() for c in col]
        colIndex = 0
        score = 0
        for column in columns:
            rowIndex = 0
            for element in column:
                count = 0
                if element == "@":
                    try:
                        if count >= 4:
                            count = 0
                            continue
                        if columns[colIndex-1][rowIndex-1] == "@":
                            count += 1
                        if columns[colIndex-1][rowIndex] == "@":
                            count += 1
                        if columns[colIndex-1][rowIndex+1] == "@":
                            count += 1
                        if columns[colIndex][rowIndex-1] == "@":
                            count += 1
                        if columns[colIndex][rowIndex+1] == "@":
                            count += 1
                        if columns[colIndex+1][rowIndex-1] == "@":
                            count += 1
                        if columns[colIndex+1][rowIndex] == "@":
                            count += 1
                        if columns[colIndex+1][rowIndex+1] == "@":
                            count += 1
                    except:

                rowIndex+=1
            colIndex+=1



if __name__ == "__main__":
    day4pt1()