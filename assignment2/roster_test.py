#test fixture (already created data)
roster = {1: ['Kevin', '52', '100.0'], 2: ['Aaron', '48', '34.3'], 3: ['Dorkus ', '13', '0.1']}

print(roster)


print("1. Get the age of the first user: ", roster[1][1])

print("2. Get the awesomeness of the second user: ", roster[2][2])
	  
print("3. Get the name, age, and awesomeness of the third user: Name" + str(roster[3][0]) + " Age: " + str(roster[3][1]) + " Awesomeness:" + str(roster[3][2]))

print("4. Change the awesomeness of the first user: ")
roster[1][2] = 90.9
print(roster[1][2]) 
	  
# 5. Change the age of the second user
# 6. Add a fourth user
# 7. Remove the third user 
# 8. Calculate the coolness of each user

# while True:
#     userID = int(input("Please enter the userID you would like to return: "))
#     info = input("Please enter the information you would like to return (name, age, awesomeness)")
#     name = roster[userID][0]
#     age = roster[userID][1]
#     awesomeness = roster[userID][2]
#     if info == 'name':
#         print(name)
#     if info == 'age':    
#         print(age)
#     if info == 'awesomeness':
#         print(awesomeness)
#     if userID == '':
#         break