# approximations for various mathematical processes

# Decided to use vim in my WSL terminal with no code
# completion to challenge myself

# Ishaan Takrani


def factorial(x):
    '''
    Calculates factorial of number iteratively

    Args:
        x (int): number to find factorial of

    Returns:
        fac (int): final factorial of number

    Time complexity:
        Worst case: O(n)
        Best case: O(1)
    '''

    fac = 1
    for i in range(1,x+1):
        fac = fac * i

    return fac


def sin(x,n=20):

    '''
    Approximates sin(x), accurate to 8 decimal places at x = 5000 using Taylor series expansion

    Args:
        x (int/float): x at which sin(x) is to be calculated
        n (int): INITIALIZED to 20, number of terms to be added to sum

    Returns:
        sinx (float): approximation of sin(x)

    Time complexity:
        Worst case: O(n^2)
        Best case: O(1)

    '''

    def factorial(x):
        fac = 1
        for i in range(1,x+1):
            fac = fac * i
        return fac

    twopi = 6.283185307179586

    # subtract (approximate) period from x, to avoid overflow
    if(x > twopi):
        while(x > twopi):
            x -= twopi

    sinx = 0
    for i in range(n):
        num = (-1)**i
        den = factorial((2*i) + 1)
        sinx += (num/den) * x**((2*i) + 1)

    return sinx

