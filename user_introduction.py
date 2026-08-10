#personal introduction program
#the program prompts the user to procvide their personal information and then displays it collectively as an introduction
#welcome message 
print("Hello user, welcome to the introdUction program")

#name prompt
user_name = input("Please provide your name: ")

#age prompt
user_age = input("Please provide your age: ")

#occupation prompt 
user_job = input("Please provide your current occupation: ")

#goal prompt
user_goal = input("Please provide your current goal: ")

#challenge output
print(
    f'--- USER PROFILE ---\n'
    f' \n'
    f'Name: {user_name}\n'
    f'Age: {user_age}\n'
    f'Occupation: {user_job}\n'
    f'Current goal: {user_goal}\n'
    f'--------------------'

)



#closing message
print(f'Thank you {user_name} for participating. Come again soon!')


