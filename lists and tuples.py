def char_counts(s):
    """s is a string of lowercase chars
    Return a tuple where the first element is the 
    number of vowels in s and the second element
    is the number of consonants in s"""

    v_count = 0
    c_count = 0

    for char in s:
        if char in ("a","e","i","o","u"):#vowel count
            v_count +=1
        else:#consonant count
            c_count +=1

    return (v_count,c_count)

def sum_and_prod(L):
    """L is a list of numbers
    Return a tuple where the first value is the 
    sum of all elements in L and the second value
    is the products of all elements in L"""
    tot_sum = 0
    tot_prod =1

    for i in L:
        tot_sum += i
        tot_prod = tot_prod *i 

    return (tot_sum, tot_prod)

x = [1,2,3,4,5]

def make_ordered_list(n):
    """n is a positive int
    Returns a list containing all ints in order 
    from 0 to n inclusive"""
    num_list = [] # creating an empty list 

    #iterating through a range of values  to get all ints in order
    for i in range(n+1):
        num_list.append(i)#adding values to the list 

    return num_list

def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L
    but without any elements equal to e. 
    """
    new_list = []
    for i in L:
        if i != e:
            new_list.append(i)

    return new_list
L = [1,2,2,2,2]


def count_words(sen):
    """sen is a string representing a sentence
    Returns how many words are in s (i.e a word is 
    a sequence of characters between spaces.)"""
    wordset = [sen.split(" ")]#creating a list of words
    size = len(wordset)
    return size
    

print(count_words("Hello its me"))
