# to do 
# save in left list
# save in right list
# compare pairs for lowest distance
# sum distances

left = []
right = []
sum_distance = []

with open("advent01.txt", "r")as file:
    for rows in file:
        
        leftN, rightN = rows.split()
        leftN = int(leftN)
        rightN = int(rightN)
        left.append(leftN)
        right.append(rightN)
left = sorted(left)
right = sorted(right)

def pair(L_list,R_list):
    for i in range(len(L_list)):
        distance = L_list[i] - R_list[i]
        distance = abs(distance)
        sum_distance.append(distance)
    total = sum(sum_distance)
    print(total)            

def similarity(L_list, R_list):
    sim_score = 0
    for number in L_list:
        number_count = R_list.count(number)
        score = number * number_count
        sim_score += score
    print(sim_score)
    
pair(left,right)    
similarity(left,right)
