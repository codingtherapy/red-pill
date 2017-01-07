### Pandigital prime
### Problem 41
### We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
### What is the largest n-digit pandigital prime that exists?

import itertools
import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def biggest_pandigital_prime():
    s = '987654321'
    for i in range(9):
        seq = ''.join(s[i:])
        for c in itertools.permutations(seq):
            p = int(''.join(c))
            if is_prime(p):
                return p

def all_pandigital_primes():
    s = '987654321'
    for i in range(9):
        seq = ''.join(s[i:])
        for c in itertools.permutations(seq):
            p = int(''.join(c))
            if is_prime(p):
                print p

if __name__=='__main__':
    print biggest_pandigital_prime()
