def day3pt1():
    with open("input3.txt") as f:
        score = 0
        for line in f.read().splitlines():
            one, two = "0", "0"
            for index,num in enumerate(line):
                if num > one and len(line)-1 != index:
                    one = num
                    two = "0"
                elif num > two:
                    two = num
                # elif num > one: one = num
            score += int(one+two)
            print(int(one+two))
        print(score)

def day3pt2():
    with open("input3.txt") as f:
        score = 0
        for line in f.read().splitlines():
            battery = "000000000000"
            empty = "000000000000"
            for index,num in enumerate(line):
                if num > battery[0] and index+12 <= len(line):
                    battery = num+empty[1:]
                elif num > battery[1] and index+11 <= len(line):
                    battery = battery[0]+num+empty[2:]
                elif num > battery[2] and index+10 <= len(line):
                    battery = battery[:2]+num+empty[3:]
                elif num > battery[3] and index+9 <= len(line):
                    battery = battery[:3]+num+empty[4:]
                elif num > battery[4] and index+8 <= len(line):
                    battery = battery[:4]+num+empty[5:]
                elif num > battery[5] and index+7 <= len(line):
                    battery = battery[:5]+num+empty[6:]
                elif num > battery[6] and index+6 <= len(line):
                    battery = battery[:6]+num+empty[7:]
                elif num > battery[7] and index+5 <= len(line):
                    battery = battery[:7]+num+empty[8:]
                elif num > battery[8] and index+4 <= len(line):
                    battery = battery[:8]+num+empty[9:]
                elif num > battery[9] and index+3 <= len(line):
                    battery = battery[:9]+num+empty[10:]
                elif num > battery[10] and index+2 <= len(line):
                    battery = battery[:10]+num+empty[11]
                elif num > battery[11] and index+1 <= len(line):
                    battery = battery[:11]+num
            score+=int(battery)

        print(score)

if __name__ == "__main__":
    day3pt2()