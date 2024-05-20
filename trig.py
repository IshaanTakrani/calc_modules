# approximations for sin(x)
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


def taylor_sin(x,n=20, mode="rad"):

    '''
    Approximates sin(x), accurate to 8 decimal places at x = 5000 using a Taylor series expansion

    Args:
        x (float): x at which sin(x) is to be calculated
        n (int): INITIALIZED to 20, number of terms to be added to sum
        mode (string): INITIALIZED to rad, for radians, can be set to "deg" for degrees

    Returns:
        sinx (float): approximation of sin(x)
        

    Time complexity:
        Worst case: O(n^2)
        Best case: O(1)

    '''

    if(mode == "deg"):
        x = x/(180/3.141592653589793)

    def factorial(x):
        fac = 1
        for i in range(1,x+1):
            fac = fac * i
        return fac

 
    # subtract (approximate) period from x, to avoid overflow
    if(x > 6.283185307179586):
        while(x > 6.283185307179586):
            x -= 6.283185307179586

    sinx = 0
    for i in range(n):
        num = (-1)**i
        den = factorial((2*i) + 1)
        sinx += (num/den) * x**((2*i) + 1)

    return sinx
    


    

print(taylor_sin(0.78, mode="deg"))