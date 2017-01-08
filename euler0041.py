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

def pandigital_primes_generator():
    # perm(12), perm(123), perm(12345), perm(123456), perm(123456789)
    # are divisible by 3
    for seq in ['87654321', '7654321', '4321']:
        for c in itertools.permutations(seq):
            if c[-1] not in ['2','4','5','6','8']:
                p = int(''.join(c))
                if is_prime(p):
                    yield p

if __name__=='__main__':
    print pandigital_primes_generator().next()
    for p in pandigital_primes_generator():
        print p
