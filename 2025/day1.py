def dayOnePartOne():
    with open("inputs/day1-1.txt", "r") as f:
        score, start = 0, 50
        for line in f.read().splitlines():
            if line[0] == "L":
                start -= int(line[1:])
            if line[0] == "R":
                start += int(line[1:])
            start %= 100
            if start == 0:
                score+=1
        print(score)

def dayOnePartTwo():
    with open("inputs/day1-1.txt", "r") as f:
        score, start = 0, 50
        for line in f.read().splitlines():
            start = (100 - start) % 100 if line[0] == "L" else start
            start += int(line[1:])
            score += start // 100
            start = (100 - start) % 100 if line[0] == "L" else start % 100
        print(score)

if __name__ == "__main__":
    dayOnePartTwo()