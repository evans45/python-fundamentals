#working with while loops 
#where = input("Go left or right? ")
#counter = 0
#while where == 'right':#why were single quotes used in equating ?
 #   counter = counter + 1
  #  if (counter > 2):
   #     print("\U0001F614")
    #where = input("Go left or right? ")
#print("You got out!")

#code for identifying number of even numbers in a given range 
#count = 0
#for i in range(5):
    #i is 0,1,2,3,4 
#    if i>0 and i%2==0:
#        count += 1
#print(count)

#code to provide number of unique letters in a string 
#learning how to execute break
#s = "seen"
#y = ""
#for i in s:
#    if i not in y:
#       y = y+i 
#       
#print(len(y))
#print(y)

#guess and check algorithm(exhaustive enumeration)
#secret = 4
#for i in range(1,11):
#    if secret == i :
#        print(secret)
#        break
#    else:
#        print("not found")

#num = 1507 
#result = ''
#if num == 0: 
#    result = '0'

#while num >0:
#    result = str(num%2) + result
#    num = num//2 #performing division and only keeping the interger value(values to the left of the decimal )

#print(result)

#bisection search for cube root
#cube = 27
#epsilon = 0.01
#low = 0 
#high = cube
#guess = (high+low)/2 # setting the first guess value to be the midpoint

#while abs((guess**3)-cube) > epsilon:
#    if guess**3 > cube: #condition if the guess is too high 
#        high = guess
#        print(f'current guess is {guess} and difference is {(guess**3)-cube} high is {high} low is {low}')
#    else:
#        low = guess    
#        print(f'current guess is {guess} and difference is {guess**3-cube} high is {high} low is {low}')
#    guess = (high+low)/2

#bisection search exercise 1
#n = 637 
#low = 0 
#high = 1000
#guess = (high + low)//2
#counter = 0

#while guess != n :
#    counter +=1
#    if guess-n > 0:
#        high = guess
#    else:
#        low = guess
 
#    guess=(high+low)//2

#print(f'{counter} is the number of attempts and the answer is {guess}')

#bisection exercise 2 
"""low = 0
cube = 150 
epsilon = 0.01
high = cube
guess = (high+low)/2
counter =0
while abs((guess**3)- cube) > epsilon:  
    counter += 1
    if guess**3 > cube:
        high = guess
    else:
        low = guess
    guess = (high+low)/2
print(f'the cube root of {cube} is {guess} number of guess is {counter}')"""

#functions in python
"""def div_by(n,d):
    n and d are ints > 0 
        Returns true if d divides n evenly and false otherwise

    if n > 0 and d > 0:
        return n%d == 0
    else:
        y = "please provide positive integers"
        return y

print(div_by(195,13))"""

def sum_odds(a,b):
    sum_of_odds = 0
    for i in range(a,b+1):
        if i%2 == 1:
            sum_of_odds = i + sum_of_odds
    return sum_of_odds

#print(sum_odds(2,7))


def is_triangular(n):
    total = 0
    x = False
    for i in range(n+1):
        total += i
        if total == n:
            x = True
    return(x)

#print(is_triangular(1))       

def count_nums_with_sqrt_close_to (n, epsilon):
    """n is an int > 2
    epsilon is a positive number < 1
    returns how many integers have a squareroot within the epsilon of n"""   

    return None

"""n = 10 
epsilon = 0.1
x = (n**2)
y = (n**2) - 1
counter = 0

while abs((x**0.5)-n) <= epsilon:
    counter += 1
    print(x)
    x += 1

while abs((y**0.5)-n) <= epsilon:
    counter += 1
    print(y)
    y -= 1
"""
x = "nana" 
print(len("nana"))