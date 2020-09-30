""" This function takes in a proth number and attempts to determine if the number is a proth prime.
This is done by applying the equation (a^((p-1)/2))
where 'a' is a random integer
      'p' is a proth number
the number is a proth prime if this equation evaluates to  '-1'.
if it doesn't, the process is repeated for different values of 'a'
if the process is repeated for up to 1000 different values of 'a' without result, the number is assumed to be composite
"""

import random

def is_proth_prime(p):
    '''
    This function only works with proth numbers
    '''
    #initialise  number of iterations
    num_of_iterations = 0
    while num_of_iterations <= 1000:
        #increment number of iterations
        num_of_iterations += 1
        #generate a random integer 'a' in range (0, 1000000)
        random_integer = random.randint(1,1000000)
        power = (p-1)/2
        
        check_proth = (random_integer ** power) + 1
        if check_proth % p == 0:
            return (p, 'is prime')
        elif num_of_iterations == 1000:
            return (p, 'is probably composite')


proth = eval(input('please enter proth number: '))

print(is_proth_prime(proth))
