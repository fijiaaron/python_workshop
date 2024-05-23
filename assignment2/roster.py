roster = {}
person = ()
id = 1
while len(roster)<3:
    name = input("Please enter your name: ")
    if name == '':
        break
    age = input("Please enter your age: ")
    awesomeness = input("Please enter your awesomeness score: ")
    
    # try:
    #     val = float(awesomeness)
    #     while float(awesomeness) < 1 or float(awesomeness) > 100:
    #         awesomeness = input("Please enter your aswesomness score as a decimal number from 1-100: ")
    person = (name, age, awesomeness)
    roster[id]=person
    id = id + 1
print (roster)


while True:
    userID = int(input("Please enter the userID you would like to return: "))
    info = input("Please enter the information you would like to return (name, age, awesomeness)")
    name = roster[userID][0]
    age = roster[userID][1]
    awesomeness = roster[userID][2]
    if info == 'name':
        print(name)
    if info == 'age':    
        print(age)
    if info == 'awesomeness':
        print(awesomeness)
    if userID == '':
        break