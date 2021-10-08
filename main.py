'''

To be a good problem solver, it is important to be able to break problems down. One way to go about this is to write out 
the steps it will take to solve the problem. These steps are written down in English in a manner that are easily 
explainable to someone who may not be technical. The idea is that in order to code something out, you first need to 
have a good understanding of what it is you are attempting to solve.

For each of the three problem solving problems below, write out the steps it will take to go about solving the problem. 
For example, once you are done writing out the steps for the “happy numbers” problem, you would then write out the code 
to solve the problem. You would then repeat the process for each ensuing problem. Ideally, this will be a good habit 
that you will develop and carry forward with you for all problems you encounter at devCodeCamp and beyond.

1. Happy Numbers a. https://en.wikipedia.org/wiki/Happy_number

    b. A happy number is a number defined by the following process: starting with any positive integer, replace the number 
        by the sum of the squares of its digits, and repeat the process until the number equals 1. An example of a happy number is 19

    c. Write a method that determines if a number is happy or sad

2. Prime Numbers

    a. A prime number is a number that is only divisible by one and itself.

    b. Write a method that prints out all prime numbers between 1 and 100

3. Fibonacci

    a. A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. The simplest is the 
        series 1, 1, 2, 3, 5, 8, etc.

    b. Write a method that does the Fibonacci sequence starting at 1

    c. HARDER VERSION: Write a method that does the Fibonacci sequence starting at a number that a user inputs

'''

# 1.---------Happy Numbers---------------


# 2.----------Prinme Numbers-------------

'''
write a range(101)

Function for determining prime numbers (range)
    prime list
    for number in range100:
        for division in range:
            if number / division != int and number != number:
                add number to prime list

'''
#----------created a non_prime list, because that is all I could figure out-----------
number_range = range(2,101,1)

def non_prime_numbers (number_range):
    non_prime_list = []
    for number in number_range:
        for divisor in number_range:
            if number % divisor == 0 and number != divisor:
                non_prime_list.append(number)
                continue
    return non_prime_list
#-----------created function to remove duplicates from my non prime list----------------------------
def remove_duplicates (duplicate_list):
    single_list = []
    for duplicate in duplicate_list:
        if duplicate in single_list: pass
        else: single_list.append(duplicate)
    return single_list

#-------------create list that removes non prime numbers, leaving prime numbers--------------------


def remove_numbers (non_prime_list):
    prime_list = []
    for prime in range(0,101,1):
        if prime in non_prime_list: pass
        else: prime_list.append(prime)
    return prime_list


non_prime_number_100 = non_prime_numbers (number_range)


single_non_prime = remove_duplicates (non_prime_number_100) 

prime_list = remove_numbers (non_prime_number_100)
# print prime number list-----------------------------
print(f'Prime number list up to 100 {prime_list}') 


# 3.------------fibonacci scale--------------
'''
The fibonacci scale starting at one going up. Since it could go on forever, I will set a max to it, 100

fibonacci list

function that takes a + b = c
c will be added to the list
a will be index[-2] and b will be inde[-1] from fibonacci list
I will cheat and have 1 on the list already

'''

def fibonacci_list_100 ():
    fibonacci_list = [1,1,]
    while fibonacci_list[-1] <= 100:
        fib_sum = fibonacci_list[-2] + fibonacci_list [-1]
        fibonacci_list.append(fib_sum)
    return fibonacci_list

fibonacci_to_100 = fibonacci_list_100()
print(f'Limited Fibonacci starting at 1 {fibonacci_to_100}')