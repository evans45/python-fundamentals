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

#the function below applies a takes in a number and returns a bool if the criteria aligns 

def apply(criteria, n):
    count = 0
    for i in range(n+1):
        if criteria(i):
            count += 1 
    return count


def is_even(x): #criteria to be checked against
    y = (x%2 == 0)
    return y


#calculator functions
def calculate(a, b, operation):
    return operation(a,b)

def add(x,y):
    #function tp perform addition operation on 2 integers
    return x+y

def subtract(x,y):
    #function tp perform subtraction operation on 2 integers
    return x-y

def multiply(x,y):
    #function tp perform multiplication operation on 2 integers
    return x*y

#apply function repeatedly
def apply_b_times(func, value, n):
    count = 0
    while count<n:
        count +=1
        x=func(value)
        value = x
    return x

def double(x):
    return x*2

def add_five(x):
    return x+5

#function that creates another function
def make_multiplier(multiplier):
    def multiplied(x):
        return(x *  multiplier)
    
    return multiplied
    

double = make_multiplier(2)
triple = make_multiplier(3)
ten_times = make_multiplier(10)

times_three = make_multiplier(3)

result = apply_b_times(times_three, 2, 3)

print(result)