def day5():
    with open("inputs/day5.txt") as f:
        list = f.read().split("\n")
        keys = [c.split("-") for c in list]
        resultKeys = []
        resultValues = []
        flip = False
        for inner_list in keys:
            if flip:
                resultValues.append(inner_list)
            if inner_list[0] != "" and not flip:
                resultKeys.append(inner_list)
            else:
                flip = True

        score = 0
        for value in resultValues:
            for key in resultKeys:
                if int(key[0]) <= int(value[0]) <= int(key[1]):
                    score+=1
                    break
        # score += 1 if resultKeys[n+1][0] > value > resultKeys[n][1] for value in resultValues
        print(score)

def day5pt2():
    with open("inputs/day5.txt") as f:
        list = f.read().split("\n")
        keys = [c.split("-") for c in list]
        resultKeys = []
        flip = False
        for inner_list in keys:
            if inner_list[0] != "" and not flip:
                resultKeys.append(inner_list)
            else:
                flip = True
                break

        score = 0
        for key in resultKeys:
            score += int(key[0]) + int(key[1])
        # score += 1 if resultKeys[n+1][0] > value > resultKeys[n][1] for value in resultValues
        print(score)



if __name__ == "__main__":
    day5pt2()