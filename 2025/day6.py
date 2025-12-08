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
    with open("inputs/day6.txt") as f:
        lines = f.read().split("\n")
        *number_lines, op_line = lines
        width = max(len(line) for line in lines)
        number_lines = [line.ljust(width) for line in number_lines]
        print(number_lines)
        op_line = op_line.ljust(width)
        op_positions = [i for i, c in enumerate(op_line) if c in '*+']
        total = 0
        prev_pos = -1
        for op_pos in op_positions:
            op = op_line[op_pos]
            numbers = []
            for row in number_lines:
                segment = row[prev_pos + 1 : op_pos + 1]
                digits = [c for c in segment if c.isdigit()]
                if digits:
                    numbers.append(int(''.join(reversed(digits))))
            result = numbers[0]
            for n in numbers[1:]:
                result = result * n if op == '*' else result + n
            total += result
            prev_pos = op_pos
        print(total)

if __name__ == "__main__":
    day6pt2()