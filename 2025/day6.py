def day6pt1():
    with open("inputs/day6.txt") as f:
        lines = f.read().split("\n")
        res = []
        for line in lines:
            res.append(" ".join(line.split()).split())
        operations = res.pop()
        final = 0
        i = 0
        while i < len(res[0]):
            math = 0
            for i2 in range(len(res)):
                if i2 == 0:
                    math = int(res[i2][i])
                    continue
                elif operations[i] == "*":
                    math *= int(res[i2][i])
                elif operations[i] == "+":
                    math += int(res[i2][i])
            final += math
            i += 1
        print(final)

def day6pt2():
    with open("inputs/day6test.txt") as f:
        lines = f.read().split("\n")


if __name__ == "__main__":
    day6pt1()