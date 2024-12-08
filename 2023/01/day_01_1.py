with open("01/day_01.txt", "r") as fd:
    data = fd.readlines()

nums = ["1","2","3","4","5","6","7","8","9","0"]
total = 0

for line  in data:
    
    chars = int("".join([char.strip() for char in line.strip() if char.strip() in nums]))
    if len(str(chars)) > 2:
        str_num = str(abs(chars))
        first = str_num[0]
        last = str_num[-1]
        chars = int(first + last)
    if len(str(chars)) == 1:
        str_num = str(chars)
        chars = int(str_num + str_num)
    total += chars
print(total)

