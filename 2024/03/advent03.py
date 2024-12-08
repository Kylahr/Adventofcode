import re

def part1(input):
    total = 0
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", input):
        total += int(a) * int(b)
    return total

def part2(puzzle_input):
    do = r"do\(\)"
    dont = r"don't\(\)"
    mul = r"mul\((\d+),(\d+)\)"
    total = 0
    enabled = True
    for x in re.finditer(f'{do}|{dont}|{mul}', puzzle_input):
        if re.fullmatch(do, x.group()):
            enabled = True
        elif re.fullmatch(dont, x.group()):
            enabled = False
        elif enabled:
            total += int(x.group(1)) * int(x.group(2))

    return total
with open("advent03.txt", "r") as file:
    data = file.read()
    
pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
numbers = r"\d+,\d+"
muls = re.findall(pattern, data)

muls = ["x" if i == "don't()" else i for i in muls]
muls = ["y" if i == "do()" else i for i in muls]

digits = [re.findall(numbers,i) if i.__contains__("mul") else i for i in muls]

list_ = []
for pair in digits:
    for subpair in pair:
        nums = subpair.split(",")
        list_.append([int(i) if i != 'x' and i != 'y' else i for i in nums])

no_restriction = True
sum = 0

for i, pair in enumerate(list_):
    if pair[0] == 'x':
        no_restriction = False
    elif pair[0] not in ('x', 'y') and no_restriction:
        #print(i,pair)
        sum += pair[0]*pair[1]
    elif pair[0] == 'y':
        no_restriction = True
        
print(sum)