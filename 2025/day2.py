def day2():
    with open("inputday2.txt") as f:
        count = 0
        for line in f.read().split(","):
            dic = line.split("-")
            for n in range(int(dic[0]), int(dic[1])+1):
                count += checkInvalidPt1(n)
        print(count)

def checkInvalidPt1(number):
    number = str(number)
    if len(number)%2 == 1: return 0
    for n in range(1, ((len(number)+1)//2)+1):
        if number[0:n] == number[n:]: return int(number)
    return 0

def checkInvalidPt2(number):
    number = str(number)
    stop = ((len(number)+1)//2)+1 if len(number)%2==0 else (len(number)+1)//2
    for n in range(1, stop):
        count = number.count(number[0:n])
        if count == (len(number) // n) and len(number) == count * n:
            return int(number)
    return 0

if __name__ == "__main__":
    day2()