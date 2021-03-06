import matplotlib.pyplot as plt
import numpy as np

def all_prime(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    
    ''' 
    Returns  a list of primes < n 
    '''

    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def prime_ratio(n):

  x = all_prime(n)

  y = list(range(n))

  percent = len(x)/len(y) * 100

  return "{}% of the numbers from 0 to {} are prime.".format(percent, n)

def prime_plot(n, display_numbers=False):
    '''
    Takes twos arguments: 
    
    n, which must be a number > 2 and a perfect square. 
    Produces a plot of sqrt(n) x sqrt(n) size and shows each number that is prime, 
    using its respective number.

    display_numbers, which must be True or False. 
    display_numbers will show the number on top the black cell, but this
    is not recommended to be on for very large numbers. (Too slow)
    '''
    N = int(np.sqrt(n))
    if N*N != n:
        raise ValueError("Need a square grid, but a perfect square was not given.")

    primes = np.array(all_prime(n)).astype(int)
    data = np.zeros(n)
    data[primes] = 1
    data = data.reshape(N,N)

    fig, ax = plt.subplots()
    plt.title(prime_ratio(n))
    ax.imshow(data, cmap="gray_r")

    if display_numbers:
        for p in primes:
            ax.text(p%N, p//N, p, color="w", ha="center", va="center")

    plt.show()



m = int(input("What size grid would you like to display? (Must be a perfect square number) Example: 16\n>"))
display_num = input("Display numbers over each prime? WARNING: Don't use this with large numbers. (Y/N)\n>").lower()

if display_num == 'y':
    prime_plot(m, True)

else:
    prime_plot(m)