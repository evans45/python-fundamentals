#program to determine if user is meeting their savings target 
#Welcome prompt
print("Hello user, welcome to the savings calculator program")

#user inputs
weekly_income = float(input("Please provide your weekly income: "))
weekly_expenses = float(input("Please provide your weekly expenses: "))
saving_target = float(input("Please provide your savings target: "))

#program calculations
#money after expenses 
post_expense_amount = (weekly_income - weekly_expenses)
savings_rate = (post_expense_amount/weekly_income)*100

#determining if savings target was hit 
saved_well = ""
if (post_expense_amount >= saving_target):
    saved_well = "Yes"
else:
    saved_well = "No"


print(f"""
EARNINGS AND SAVINGS OVERVIEW 

Earned : {weekly_income}
Spent : {weekly_expenses}
Saved : {post_expense_amount}
Save rate : {savings_rate: .2f}%
Savings target hit : {saved_well}
""")