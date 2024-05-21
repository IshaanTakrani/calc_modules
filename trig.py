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


def taylor_sin(x, mode,n=20):
    '''
    Approximates sin(x), accurate to 8 decimal places at x = 5000 using a Taylor series expansion
    IDEAL range: 0-2pi radians (0-360 degrees)

    Args:
        x (float): x at which sin(x) is to be calculated
        mode (string): mode, "deg" for degrees or "rad" for radians
        n (int): INITIALIZED to 20, number of terms to be added to sum

    Returns:
        sinx (float): approximation of sin(x)
        

    Time complexity:
        Worst case: O(n^2)
        Best case: O(1)

    '''

    if (mode not in ['deg','rad']):
        return ValueError("Mode must be either 'deg' for degrees or 'rad' for radians")

    if(mode == "deg"):
        x = x/(180/3.141592653589793)

    def factorial(x):
        fac = 1
        for i in range(1,x+1):
            fac = fac * i
        return fac

 
    # subtract (approximate) period from x, to avoid overflow
    # if(x > 6.283185307179586):
    #     while(x > 6.283185307179586):
    #         x -= 6.283185307179586
    x = x % 6.283185307179586

    sinx = 0
    for i in range(n):
        num = (-1)**i
        den = factorial((2*i) + 1)
        sinx += (num/den) * x**((2*i) + 1)

    return sinx


def bhaskara_sin(x, mode):
    '''
    Approximates sin(x) using Bhaskara's approximation for sin(x)
    Ideal range: 0-360 degrees (0-2pi radians)

    Args:
        x (float): x at which sin(x) is to be calculated
        mode (string): mode, "deg" for degrees or "rad" for radians

    Returns:
        sinx (float): approximation of sin(x)
        
    Time complexity:
        Worst case: O(1)
        Best case: O(1)
    '''

    if (mode not in ['deg', 'rad']):
        return ValueError("Mode must be either 'deg' for degrees or 'rad' for radians")

    if mode == "rad":
        x = x*(180/3.141592653589793238)

    x = x % 360

    if (0 <= x <= 180):
        sinx = (4 * x * (180 - x)) / (40500 - x * (180 - x))
    elif (180 < x <= 360):
        x = 360 - x
        sinx = -(4 * x * (180 - x)) / (40500 - x * (180 - x))
    
    return sinx


x = -200
mode = "deg"
print(taylor_sin(x, mode))
print(bhaskara_sin(x, mode))



