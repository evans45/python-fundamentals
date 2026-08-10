#publishing welcome message
#print("Hello Evans welcome to your first python coding session")

#requesting user for details
#text = input("What is your name ")
#print(text)

#interractive program exercise
#objective - accept user input and add it to a string. display the provided user input 5 times
#requesting input at initial interraction
#user_input = input("Hello user please provide a verb to proceed: ")
#print("I can " + user_input + " better than you!")
#print(f'{user_input *5} ') # find a way to get rid of the final space

#interractive program to check if users guess is true or false
secret = 5
user_guess = int(input("please provide a guess for the value "))

if (user_guess > secret):
    print("guess is too high")
elif (user_guess < secret):
    print("guess is too low")
else:
    print("correct!")
