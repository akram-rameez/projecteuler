from random import randrange


def main():

    # We can figure out that the largest pandigital prime will be 7 digits long, so limit our search starting with that.
    for n in range (7, 0, -1):
        # This will give us the lowest N digit number
        lower = 10 ** (n - 1)
        
        # This will give us the largest N digit number
        upper = (10 ** (n))

        for i in range(upper, lower, -1):
            if is_prime(i) and is_pandigital(i, n):
                return i
    return -1

## Copied from https://stackoverflow.com/a/17298131/5133104
## This uses a fast primality check
def is_prime(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def is_pandigital(num, n):
    n_digits = list(range(1, n+1))

    num_digits = [int(x) for x in str(num)]

    return n_digits == sorted(num_digits)

print(main())