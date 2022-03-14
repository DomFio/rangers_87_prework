# Prework questions and solutions

#Question 1: Write a function that prints "Hello USERNAME"

from multiprocessing.dummy import current_process


def hello_name(user_name):
    print("Hello " + user_name.upper() + "!")
    
hello_name('Dominic')

# Question 2: Print first odd numbers between 1-100
def first_odds():
    """
        Print all odd numbers between 1 and 100.
    """

    current_number = 0

    while current_number < 100:
        current_number += 1
        if current_number % 2 == 1:
            print(current_number)

#first_odds()

# Question 3: Write a function that returns the max number in a given list
def max_num_in_list(a_list):
    """
        returns largest number in a list.
    """

    max_number = max(a_list)
    return max_number

number_list = [12, 470, 73, 88, 65, 49]

def max_num2(a_list):
    return max(a_list)

print(max_num_in_list(number_list))
#print(max_num_2(number_list))

#Question 4: Write a function that returns True if the given year is a leap year.
def is_leap_year(a_year):
    num = a_year
    if num % 400 == 0:
        print(True)
    elif num % 4 == 0 and num % 100 != 0:
        print(True)
    else:
        print(False)

def leap_year_2(a_year):
    """Returns a given year a leap year or not"""
    return(a_year % 400 == 0 or a_year % 4 == 0 and a_year % 100 != 0)

#is_leap_year(2024)
#print(leap_year_2(2000))

# Question 5: Write a function to check if all numbers ina  given list are consecutive

def is_consecutive(a_list):
    status = True
    if len(a_list) > 1:
        for number in range(len(a_list)-1):
            if a_list[number] == a_list[number + 1] - 1:
                continue
            else:
                status = False
            return status
    
print('Is this consecutive: ', is_consecutive([1,2,3,5,6,7]))

def consecutive_2(a_list):
    return a_list == list(range(min(a_list),max(a_list)+1))

print(consecutive_2([1,2,3,4,6,7]))