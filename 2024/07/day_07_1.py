def can_compute(vars, result, current_value, index):
    if index == len(vars):
        return current_value == result
    num = vars[index]
    if can_compute(vars, result, current_value + num, index + 1):
        return True
    if can_compute(vars, result, current_value * num, index + 1):
        return True

    return False

with open("day_07.txt", "r") as fd:
    data = [line.strip() for line in fd.readlines()]

approved = []

for line in data:
    if line != "":
        result, vars = int(line.split(":")[0]), [int(x) for x in line.split(":")[1].split()]
        if can_compute(vars, result, vars[0], 1):
            approved.append(result)

print(sum(approved))
