#this code will be used to determine number of days between cleaning duties
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

participants = ["sam","kay","sim","evans","cynthia"]
day_1 = date(2026,8,17)
freq = timedelta(days=7)
target = day_1 + relativedelta(months=6)


#to do -> create loop for a 6 month duty roster
counter = 0
progress = True
'''while progress == True :
        for i in participants:  
            duty_date = day_1 + freq  * counter         
            if duty_date >= target:
                progress = False
                break
            print(f"{i} is cleaning on {duty_date}")       
            counter += 1
'''

#counting number of times each participant cleans in the period
duty_list = []
while progress == True:
    cleaner = counter % len(participants)
    duty_date = day_1 + freq  * counter           
    if duty_date >= target:
        progress = False
        break
    duty_list.append(participants[cleaner])
    #print(f'{participants[cleaner]} is cleaning on {duty_date}')        
    counter += 1

for i in participants:
    x = duty_list.count(i)
    print(f'{i} has cleaned {x} times')
       


#to do -> create loop to identify whose date it is based on the users input 