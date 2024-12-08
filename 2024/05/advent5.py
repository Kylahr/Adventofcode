#dict rules
rules = {}
# list to save middle pages
sumMiddle = []

# to do 
# get list
# take each value and check for rule[value]
# if value in dict, check if element in list 
# compare index key < value == True
# if True take middle page and save in sum list
# sum of sum list

def check(list, dict):
    correct = True
    for index_key, key in enumerate(list):
        #check if item in dict as key
        if key in dict:
            #get index of key in list
            for index_page, pages in enumerate(list):
                if pages in dict[key]:
                    if index_key > index_page:
                        correct = False
                        break
    if correct == True:
        print("correct", list)
        #get middle page
        index_middlePage = len(list) // 2
        middle_Page = list[index_middlePage]
        sumMiddle.append(int(middle_Page))

# saves keys and values in dict rules
with open("advent5.txt", "r", encoding="utf-8") as file:
    for row in file:
        if "|" in row:
            key, value = row.split("|")
            key = key.strip()
            value = value.strip()
            
            if key in rules:
                rules[key].append(value)
            else:
                rules[key] = [value]
        #save pages in list
        else:
            pages = row.split(",")
            pages = [page.strip() for page in pages]
            #call function to check if rules are applied
            check(pages, rules)
            
#sum of middle pages        
total = sum(sumMiddle)
print(total)