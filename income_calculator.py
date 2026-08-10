#income calculator 
#asks for weekly income then calculates monthly && yearly income 

#welcome message 
print("Hello user, welcome to the income calculator program")

#weekly income prompt
user_earnings = float(input("Please provide your weekly earnings: "))

#earnings calculation
monthly_earnings = (user_earnings * 52)/12
yearly_earnings = user_earnings * 52

print(f"""
User makes {monthly_earnings: .2f} AUD every month. \n
This totals to yearly earnings of {yearly_earnings: .2f} AUD
""")
