import os

from line_profiler import profile

os.environ["LINE_PROFILE"] = "1"

@profile
def is_prime(n):
    '''
    Check if the number "n" is prime, with n > 1.
    Returns a boolean, True if n is prime.
    '''
    max_val = n ** 0.5
    stop = int(max_val + 1)
    for i in range(2, stop):
        if n % i == 0:
            return False
    return True


@profile
def find_primes(size):
    primes = []
    for n in range(size):
        flag = is_prime(n)
        if flag:
            primes.append(n)
    return primes


@profile
def main():
    print('start calculating')
    primes = find_primes(100000)
    print(f'done calculating. Found {len(primes)} primes.')


def divbyzero():
    1/0
if __name__ == '__main__':
    #main()
    import traceback
    import sys

    try:
        divbyzero()
    except Exception as e:
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb = traceback.TracebackException(exc_type, exc_value, exc_tb)
        print(''.join(tb.format_exception_only()))