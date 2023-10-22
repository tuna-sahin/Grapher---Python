# -*- coding: utf-8 -*-
"""
Created on Mon Sept 29 08:16:11 2022

@author: Sahin
"""

import math as m
import cmath as cm
m.exp(cm.e)

# to do list(gamma,error)
# optimised sortlist

# %% list of functions                                       Incomplete
# ======================================================
# exponential and logarithm functions
#
# exp(x)
# ln(x)
# log(base,x)
# w(x) -> productLog(x)
# ======================================================
# alternative logarithm functions
#
# alternateLn(x)
# alternateLog(base,x)
# ======================================================
# factorials and number theory part 1
#
# lcm(x,y) -> least common multiple
# gcd(x,y) -> greates common divisor
# x!! -> double factorial
# x!
# comb(x,y) -> combination of x of y
# perm(x,y) -> permutation of x of y
# ======================================================
# number theory part 2
#
# sign(x)
# absoloute(x)
# floor(x)
# ceil(x)
# round(x)
# modf(x)
# nextAfter(x,increasing)
# ======================================================
# trigonometric functions
# sin(x)
# cos(x)
# tan(x)
# cot(x)
# sec(x)
# csc(x)
# ======================================================
# inverse trigonometric functions
#
# ======================================================
# conversion and simplification functions
#
# degrees(x) -> converts a radian input to degrees
# radians(x) -> converts a degree input to radians
# isqrt(x) -> seperates the rational and irrational factors of a sqrt
# fraction(x) -> converts a decimal to fraction
# ======================================================
# hyperbolic functions
#
# sinh(x)
# cosh(x)
# tanh(x)
# coth(x)
# sech(x)
# csch(x)
# ======================================================
# inverse hyperbolic functions
#
# arcsinh(x)
# arccosh(x)
# arctanh(x)
# ======================================================

# %% exponential and logarithm functions                     Documented


def exp(n):
    """
    the exponential function

    Parameters
    ----------
    n(Supports Float) : the argument inside the e^x function

    Returns
    -------
    e**x

    """
    return(e**n)


def exp2(n):

    temp = 0
    for i in range(20):
        temp += (n**i)/factorial(i)
    return(temp)


def ln(n):
    if type(n) != complex:
        if n>0:
            return(cm.log(n).real)
    else:
        return(cm.log(n))
    
    if n>0:
        return(m.log(n))
    if n<0:
        return(ln(-1*n)+pi*1j)
    if type(n) == complex:
        if n.imag != 0:
            return(complexLn(n))
    
    if n > 0:
        return(alternateLn(n),50)
    elif n == 0:
        return(0)
    elif n < 0:
        return(complexLn(n))
    print("here")
    """
    the logarithm operator base e(euler's number)

    Parameters
    ----------
    n(Supports Float) : the argument inside the ln(x) function

    Returns
    -------
    ln(x)

    """
    
    temp = 1
    temp2 = 2
    modifier = 1
    lastIncrease = None
    revlimiter = 0
    while temp != temp2 and revlimiter < 200:
        revlimiter += 1
        print("here ln" , revlimiter)
        temp2 = temp

        if e**temp - n > 0:
            temp -= modifier
            if lastIncrease:
                modifier /= 2
            lastIncrease = False

        elif e**temp - n < 0:
            temp += modifier
            if not lastIncrease:
                modifier /= 2
            lastIncrease = True

        else:
            return(temp)
    return(temp)


def log(base, *n):
    """
    the logarithm operator with custom base number

    Parameters
    ----------
    base(Supports Float) : the base of the logarithm operator

    n(Supports Float) : the argument inside the log(base)(x) function 


    Returns
    -------
    log(base)(n)

    """
    if isinstance(base, list):
        n = base[1]
        base = base[0]

    temp = 1
    temp2 = 2
    modifier = 1
    lastIncrease = None
    while temp != temp2:
        temp2 = temp

        if base**temp - n > 0:
            temp -= modifier
            if lastIncrease:
                modifier /= 2
            lastIncrease = False

        elif base**temp - n < 0:
            temp += modifier
            if not lastIncrease:
                modifier /= 2
            lastIncrease = True

        else:
            return(temp)
    return(temp)


def w(n):
    """
    the Product log function
    inverse of x*e^x

    Parameters
    ----------
    n(supports float) : the argument inside the w(x) function
    must be greater than -1 because of the functions domain

    Returns
    -------
    w(x)

    """

    if n < -1:
        return(None)
    temp = 0
    for i in range(100):
        temp -= ((temp * (e**temp)) - n)/((e**temp)*(temp+1))
    return(temp)



# %% alternative logarithm functions                         Documented
def alternateLn(n,revlimit):
    """
    the logarithm operator with base e(euler's number)
    is not accurate for values close to 0

    Parameters
    ----------
    n(Supports Float) : the argument inside the ln(x) function 


    Returns
    -------
    ln(x)

    """
    temp = 2
    revlimiter = 0
    while temp != temp - (exp(temp) - n) / (exp(temp)) and revlimiter < revlimit:
        revlimiter += 1
        temp -= (exp(temp) - n) / (exp(temp))
    return (temp)

def ln2(x):
    if x>0:    
        temp = 0
        while x>2:
            x /= 2
            temp += 1
        while x<1:
            x *= 2
            temp -= 1
        
        x = alternateLn(x,10)
        return(x + temp*0.6931471805599453)
    else:
        return(complexLn(x))




def alternateLog(base, n):
    """
    the logarithm operator with a custom base
    is not accurate for values close to 0

    Parameters
    ----------
    n(Supports Float) : the argument inside the log(base)(x) function 
    base(Supports Float) : the base for the log(base)(x)

    Returns
    -------
    log(base)(n)

    """

    temp = 2
    while temp != temp - (base**temp - n)/(base**temp):
        temp -= ((base**temp) - n) / (base**temp)
    return (temp)


# %% factorials and number theory part 1                     Documented

def gcd2(n):
    for i in range(len(n)):
        n[0] = gcd(n[0], n[i])
    return(n[0])


def lcm2(n):
    for i in range(len(n)):
        n[0] = lcm(n[0], n[i])
    return(n[0])


def gsb(x):  # greatest square below x
    temp = 0
    for i in range(1, x+1):
        if sqrt(i) % 1 == 0:
            temp = i
    return(sqrt(temp))


def lcm(x, y):
    """
    Least Common Multiple
    (okek)

    Parameters
    ----------
    x(integer)
    y(integer)

    Returns
    -------
    lcm(x,y)(integer)

    """
    return ((x*y)/gcd(x, y))


def gcd(x, y):
    """
    Greatest Common Divisor
    (obeb)

    Parameters
    ----------
    x(integer) 
    y(integer) 


    Returns
    -------
    gcd(x,y)(integer)

    """

    temp = 0
    x, y = int(max(x, y)), int(min(x, y))
    for i in range(1, y+1):
        if x % i == 0 and y % i == 0:
            temp = i
    return(int(temp))


def doubleFactorial(x):
    """
    The double factorial function
    Ex: 5!! = 5*3*1
        4!! = 4*2

    Parameters
    ----------
    x : the argument inside the function x!!
    the parameter "x" supports float but it is not defined normally

    Returns
    -------
    result : returns x!! with the same type as the imput.

    """

    result = 1
    if x % 2 == 0:  # even
        for i in range(2, x+2, 2):
            result *= i
    else:
        for i in range(1, x+2, 2):
            result *= i
    return result


def factorial(n):
    """
    the Factorial function

    Parameters
    ----------
    n : the argument inside the x! function
    the parameter "n" supports float but is not defined normally

    Returns
    -------
    n!

    """
    n = int(n)
    result = 1
    for i in range(1, n+1):
        result *= i
    return(result)



def combination(n,r):
    """
    Number of ways to choose r items from n items without
    repetition and without order.


    Parameters
    ----------
    n : |n| is the top argument
    r : |r| is the bottom argument


    Returns
    -------
    |n|
    |r|
    """
    topResult = 1
    bottomResult = 1
    for i in range(1, r+1):
        topResult *= (n-i+1)
    for i in range(1, r+1):
        bottomResult *= i
    return(topResult/bottomResult)
comb = combination

def permutation(n, r):
    """
    Number of ways to order r items from n items without repetition.


    Parameters
    ----------
    n : the first argument 
    r : the second argument

    Returns
    -------
    (n,r)

    """
    result = 1
    for i in range(1, r+1):
        result *= (n-i+1)
    return(result)
perm = permutation

# %% number theory functions part 2                          Documented


def sign(x):
    """
    Returns the sign of the argument given
    |x|/x = sign(x)
    is not defined at 0

    Parameters
    ----------
    x(Supports Float) : Argument inside sign(x) function


    Returns
    -------
    1 for positive numbers and -1 for negative numbers
    undefined for input 0

    """

    if x > 0:
        return(1)
    elif x < 0:
        return(-1)
    else:
        return(None)


def absolute(x):
    """
    The absolute value function
    |x|

    Parameters
    ----------
    x(Supports Float) : the argument inside |x| function


    Returns
    -------
    |x| with the same type as the input

    """

    if x != 0:
        return x * sign(x)
    else:
        return x


def floor(n):
    """
    the function will return the greatest integer less than or equal to n

    Parameters
    ----------
    n(Supports Float) : the argument inside ⌊n⌋ function

    Returns
    -------
    ⌊n⌋ 

    """

    return(int(n))


def ceil(n):
    """

    the function will return the greatest integer less than or equal to n

    Parameters
    ----------
    n(Supports Float) : the argument inside ⌈n⌉ function

    Returns
    -------
    ⌈n⌉

    """

    if n % 1 == 0:
        return n
    return(int(n+1))


def modf(n):
    """
    Finds the characteristics and the mantissa of a given float.

    Parameters
    ----------
    n(Supports Float) : Returns the the integer part and the decimal parts
    as an array 0 being the characteristics, 1 being the mantissa


    Returns
    -------
    [characteristics,mantissa]

    """

    partsOfN = [n//1, n % 1]
    return(partsOfN)


def nextAfter(x, increasing):
    """


    Parameters
    ----------
    x(Supports Float) : the value for we will give the closest number
    increasing(Boolean Input) : if you want the result to be greater than
    the input set to true and vice versa.


    Returns
    -------
    the cloeset number to x available in python
    """

    h = 1e-16  # limit h -> 0
    if x == 0:
        return (5e-324)
    else:
        if increasing:
            return ((h*x)+x)
        else:
            return (x-(h*x))


# %% trigonometric functions (supports complex)              Documented


def sin(x):
    """
    the trigonometric sine function
    Uses the Taylor expansion of sin(x) at 0 to calculate
    x % tau is used for calculation

    Parameters
    ----------
    x(Supports Float) : The argument inside the sin(x) function.

    Returns
    -------
    sin(x % tau)

    """
    if type(x) != complex:
        x = x % tau

    temp = 0
    n = 0
    while temp != temp + ((x**(2*n + 1)) / (factorial(2*n + 1))) * (-1)**n:
        temp += ((x**(2*n + 1)) / (factorial(2*n + 1))) * (-1)**n
        n += 1
    return(temp)


def cos(x):
    """
    the trigonometric cosine function
    Uses the Taylor expansion of cos(x) at 0 to calculate
    x % tau is used for calculation

    Parameters
    ----------
    x(Supports Float) : The argument inside the cos(x) function.

    Returns
    -------
    cos(x % tau)

    """

    if type(x) != complex:
        x = x % tau

    temp = 0
    n = 0
    while temp != temp + ((x**(2*n) / (factorial(2*n)) * (-1)**n)):
        temp += ((x**(2*n) / (factorial(2*n)) * (-1)**n))
        n += 1
    return (temp)


def tan(x):
    """
    trigonometric tangent function
    calculated using sin(x)/cos(x)

    Parameters
    ----------
    x(Supports Float) : the argument inside the function tan(x) 

    Returns
    -------
    tan(x)

    """

    return (sin(x)/cos(x))


def cot(x):
    """
    the trigonometric cotangent function
    calculated using cos(x)/sin(x)

    Parameters
    ----------
    x(Supports Float) : the argument inside the cot(x) function 

    Returns
    -------
    cot(x)

    """

    return (cos(x)/sin(x))


def sec(x):
    """
    the trigonometric secant function
    calcuated using 1/cos(x)

    Parameters
    ----------
    x(Supports Float) : the argument inside the function sec(x)

    Returns
    -------
    sec(x)
    """

    return (1/cos(x))


def csc(x):
    """
    the trigonometric cosecant function
    calculated using 1/sin(x)

    Parameters
    ----------
    x(Supports Float) : the argument inside the function csc(x)

    Returns
    -------
    csc(x)

    """

    return (1/sin(x))

# %% inverse trigonometric functions                         Undocumented


def arctan2(x):
    """
    #[-1,1] is the convergence interval


    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    temp = 0
    for i in range(0, 100):
        temp += (x ** (2*i+1)) * ((-1)**i) / (2 * i + 1)
    return(temp)


def arctan(x):
    temp = 1
    temp2 = 2
    modifier = 1
    lastIncrease = None
    while temp != temp2:
        temp2 = temp

        if tan(temp) - x > 0:
            temp -= modifier
            if lastIncrease:
                modifier /= 2
            lastIncrease = False

        elif tan(temp) - x < 0:
            temp += modifier
            if not lastIncrease:
                modifier /= 2
            lastIncrease = True

        else:
            if (temp % pi) > (pi/2):
                return (temp % pi - pi)
            else:
                return(temp % pi)
    if (temp % pi) > (pi/2):
        return (temp % pi - pi)
    else:
        return(temp % pi)


def arcsin(x):
    if x < -1 or x > 1:
        return(0)
    temp = 1
    temp2 = 2
    modifier = 1
    lastIncrease = None
    counter = 0
    while temp != temp2 and counter < 200:
        temp2 = temp

        if sin(temp) - x > 0:
            temp -= modifier
            if lastIncrease:
                modifier /= 2
            lastIncrease = False

        elif sin(temp) - x < 0:
            temp += modifier
            if not lastIncrease:
                modifier /= 2
            lastIncrease = True

        else:
            if (temp % pi) > (pi/2):
                return (temp % pi - pi)
            else:
                return(temp % pi)
    
    if counter == 200:
        return(temp)
            
    if (temp % pi) > (pi/2):
        return (temp % pi - pi)
    else:
        return(temp % pi)


def arccos(x):
    if x < -1 or x > 1:
        return(0)
    if x == 1:
        return(0)
    if x == -1:
        return(pi)
    temp = 1
    temp2 = 2
    modifier = 1
    lastIncrease = None
    while temp != temp2:
        temp2 = temp

        if cos(temp) - x > 0:
            temp -= modifier
            if lastIncrease:
                modifier /= 2
            lastIncrease = False

        elif cos(temp) - x < 0:
            temp += modifier
            if not lastIncrease:
                modifier /= 2
            lastIncrease = True

        else:
            return(pi - temp % pi)
    return(pi - temp % pi)


def arccot(x):
    return(arctan(1/x))


def arcsec(x):
    return(arccos(1/x))


def arccsc(x):
    return(arcsin(1/x))


# %% conversion and simplification functions                 Undocumented

def isCloseTo0(x):
    """
    rounds really small numbers to 0
    if x is less than 1e-8
    Parameters
    ----------
    x : number thats rounded

    Returns
    -------
    x if not close to 0
    0 if close to 0

    """

    if x < 1e-7:
        return(0)
    else:
        return(x)


def degrees(x):
    """
    Converts a input of radians to degrees

    Parameters
    ----------
    x(Supports Float) : the input of radians that will be converted to degrees

    Returns
    -------
    x/pi * 180

    """
    return (x/pi*180)


def radians(x):
    """
    Converts a input of degrees to radians

    Parameters
    ----------
    x(Supports Float) : the input of degrees that will be converted to radians

    Returns
    -------
    x/180*pi

    """
    return(x/180*pi)


def isqrt(x):
    """
    simplifes a number given inside the sqrt

    Parameters
    ----------
    x(integer) : the argument given inside the sqrt

    Returns
    -------
    [a,b] as     a * sqrt(b)

    """

    temp = 1
    for i in range(1, x+1):
        if x % i == 0 and i**(1/2) % 1 == 0.0:
            temp = i
    result = [temp**(1/2), x/temp]
    return(result)


def fraction(x):
    """
    Converts a float to a fractional display
    outputs as a string or an array consisting
    of the nominator and the denominator


    Parameters
    ----------
    x(Supports Float) : the input to be converted
    Returns
    -------
    a/b = x

    """
    a = int(x*1e5)
    b = 1e5
    c = gcd(int(a), int(b))
    a /= c
    b /= c
    return([a, b])


def isqrtString(x):
    return(f"{int(isqrt(x)[0])}√{int(isqrt(x)[1])}")


def fractionString(x):
    return(f"{int(fraction(x)[0])}/{int(fraction(x)[1])}")


def sqrt(x):
    return(x**(1/2))


# %% hyperbolic functions (supports complex)                 Documented

def cosh(n):
    """
    the hyperbolic cosine function
    calculated using (e^x + e^-x)/2

    Parameters
    ----------
    n(Supports Float) : the argument inside the cosh(x) function

    Returns
    -------
    cosh(x)

    """

    n = ((e**n)+(e**(-n)))
    return(n/2)


def sinh(n):
    """
    the hyperbolic sine function
    calculated using (e^x - e^-x)/2

    Parameters
    ----------
    n(Supports Float) : the argument inside the sinh(x) function

    Returns
    -------
    sinh(x)

    """

    n = ((e**n)-(e**(-n)))
    return(n/2)


def tanh(n):
    """
    the hyperbolic tangent function
    calculated using sinh(x)/cosh(x)

    Parameters
    ----------
    n(Supports Float) : the argument inside the tanh(x) function 

    Returns
    -------
    tanh(x)


    """

    return (sinh(n)/cosh(n))


def coth(n):
    """
    the hyperbolic cotangent function
    calculated using cosh(x)/sinh(x)

    Parameters
    ----------
    n(Supports Float) :the argument inside the coth(x) function

    Returns
    -------
    coth(x)
    """

    return (cosh(n)/sinh(n))


def sech(n):
    """
    the hyperbolic secant function
    calculated using 1/cosh(x)

    Parameters
    ----------
    n(Supports Float) : the argument inside the sech(x) function

    Returns
    -------
    sech(x)

    """

    return (1/cosh(n))


def csch(n):
    """
    the hyperbolic cosecant function 
    calculated using 1/sinh(x)

    Parameters
    ----------
    n(Supports Float) : the argument inside the csch(x) function

    Returns
    -------
    csch(x)


    """

    return (1/sinh(n))

# %% inverse hyperbolic functions                            Undocumented


def arcsinh(n):
    n = ln(n+(1+n**2)**(1/2))
    return(n)


def arccosh(n):
    n = ln(n+(n**2-1)**(1/2))
    return(n)


def arctanh(n):
    n = ln((n+1)/(1-n))/2
    return (n)


def arccoth(n):
    return(arctanh(1/n))


def arcsech(n):
    return(arccosh(1/n))


def arccsch(n):
    return(arcsinh(1/n))

# %% constant calculation                                    Documented


pi = 2
e = 0

# defines e as eulers number
for i in range(18):
    e += 1/factorial(i)

# calculates pi as the mathematical constant
for i in range(1, 50):
    pi += (factorial(i)/doubleFactorial(2*i + 1)) * 2

# tau = 2pi
tau = pi*2

# i is set as the imaginary unit
j = 1j


# %% list of complex supportive functions                    Incomplete

# %% complex essentials                                      Undocumented

def complexConjugate(z):
    return(z.real - (z.imag * 1j))


def arg(z):

    r = abs(z)
    z /= r  # z now equals e ^i *theta
    sintheta = z . imag
    costheta = z . real
    theta = arctan(sintheta/costheta)
    return (theta)


def polar(z):
    x, y = z.real, z.imag
    theta = arctan(x/y)
    r = abs(z)
    return(r, theta)


def cord(r, theta):
    z = r * (e**(i * theta))
    x = z.real
    y = z.imag
    return([x, y])


# %% Complex exponentials and logarithm functions            Documented

def complexLn(z):
    if type(z) == complex:
        # ln(z) = ln|z| + i * arg(z)
        # arg(z) = angle theta for [r * e^(i*theta) = z]
        if z.real != 0:
            return(ln(abs(z)) + 1j * arg(z))
        elif z.real == 0:
            return(ln(abs(z)) + 1j*pi/2)

    else:
        if z < 0:
            temp = 0
            temp = ln((-1) * z) + pi*1j
            return(temp)

        elif z > 0:
            temp = 1
            temp2 = 2
            modifier = 1
            lastIncrease = None
            while temp != temp2:
                temp2 = temp

                if e**temp - z > 0:
                    temp -= modifier
                    if lastIncrease:
                        modifier /= 2
                    lastIncrease = False

                elif e**temp - z < 0:
                    temp += modifier
                    if not lastIncrease:
                        modifier /= 2
                    lastIncrease = True

                else:
                    return(temp)
            return(temp)


def complexLog(base, z):  # supports real bases only
    if type(z) == complex:
        # ln(z) = ln|z| + i * arg(z)
        # arg(z) = angle theta for [r * e^(i*theta) = z]
        if z.real != 0:
            return(ln(abs(z)) + 1j * arg(z))
        else:
            return(ln(abs(z) + 1j*pi/2))
        pass

    else:
        if z < 0:
            temp = 0
            temp = ln((-1) * z) + pi*1j
            return(temp)

        elif z > 0:
            temp = 1
            temp2 = 2
            modifier = 1
            lastIncrease = None
            while temp != temp2:
                temp2 = temp

                if base**temp - z > 0:
                    temp -= modifier
                    if lastIncrease:
                        modifier /= 2
                    lastIncrease = False

                elif base**temp - z < 0:
                    temp += modifier
                    if not lastIncrease:
                        modifier /= 2
                    lastIncrease = True

                else:
                    return(temp)
            return(temp)


# %% Sorting Algorithms                                      Incomplete


def sortList2(n): #bubble sort
    if len(n) == 1:
        return(n)
    for i in range(len(n)):
        for i2 in range(len(n)-1):
            if n[i2] > n[i2+1]:
                n[i2], n[i2+1] = n[i2+1], n[i2]
    return(n)

def sortList1(n):
    return(sorted(n))

# %% List Operations                                         Incomplete


class ListOperations:
    def __init__(self, n):
        self.n = n

    def multiplyList(self):
        temp = 1
        for i in self.n:
            temp *= i
        return(temp)

    def sumList(self):
        temp = 0
        for i in self.n:
            temp += i
        return(temp)

    def toString_List(self):
        result = ""
        for i in self.n:
            result += str(i)
        return(result)

    def toString_List2(self):
        result = ""
        for i in self.n:
            result += str(i) + "|"
        return(result)

    def addLists(self, y):
        result = []
        if type(self.n) == list and type(y) == list:
            if len(self.n) > len(y):
                for i in range(len(y)):
                    result.append(self.n[i]+y[i])
            else:
                for i in range(len(self.n)):
                    result.append(self.n[i]+y[i])
        return(result)

    def multiplyLists(self, y):
        result = []
        if type(self.n) == list and type(y) == list:
            if len(self.n) > len(y):
                for i in range(len(y)):
                    result.append(self.n[i]*y[i])
            else:
                for i in range(len(self.n)):
                    result.append(self.n[i]*y[i])
        return(result)

# %% Unsorteds


def power(base, exponent):
    return(exp(exponent*complexLn(base)))

def cbrt(x):
    return((abs(x) ** (1/3))*sign(x))

def roundIfClose(a):
    if isCloseTo0(a-round(a)) == 0:
        a = (round(a))
    return(a)


def SmallRound(a):
    if not roundIfClose(a) % 1:
        return(roundIfClose(a))
    tolerance = 1e-7
    lastDigit = ((a % tolerance)//(tolerance/10))
    if lastDigit >= 5.0:
        result = (a//tolerance + tolerance) * tolerance
        return(result)


def smallRound(x):
    x *= 1e3
    x = round(x)
    x /= 1e3
    return(round(x*1e8)/(1e8))


def smallerRound(x):
    x *= 1e7
    x = round(x)
    x /= 1e7
    return(round(x*1e8)/(1e8))


def smallestRound(x):
    x *= 1e14
    x = round(x)
    x /= 1e14
    return(round(x*1e14)/(1e14))


def identity(x):
    """
    identity function

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """

    return(x)

def logten(x):
    return(log(10,x))

def ordReset():
    text = open("factorialOrd.txt","w")
    text.write("0")
    text.close()

def randinteger(*x):
    text = open("fact50k.txt", "r")
    text2 = text.read()
    text.close()
    
    order = open("factorialOrd.txt", "r")
    temp = order.read()
    temp = int(temp)
    order.close()
    
    order = open("factorialOrd.txt", "w")
    order.write(str(temp+1))
    order.close()
    
    return(int(text2[temp]))

def random(*x):
    text = open("fact50k.txt", "r")
    text2 = text.read()
    text.close()
    
    order = open("factorialOrd.txt", "r")
    temp = order.read()
    temp = int(temp)
    order.close()
    
    order = open("factorialOrd.txt", "w")
    order.write(str(temp+15))
    order.close()
    
    num = text2[temp:temp+15]
    num = "0." + num    
    num = float(num)
    return(num)


def temp(x):
    return(abs(x)*sqrt(sin(x))*sign(x))

def imag(x):
    x = complex(x)
    return(x.real * 1j + x.imag * 1j)

def real(x):
    x = complex(x)
    return(x.imag + x.real)

def abs(x):
    return(x * sign(x))

def i(x):
    return(x)

def integrate(func,upper,detail = 1000,lower = 0):
    x = []
    for i in range(int(lower*detail),int(upper*detail)):
        x.append(i/detail + 1/(2*detail))  
    dx = 1/detail
    area = 0
    for i in x:
        area += dx * func(i)
    return(area)  


def map(t1,t2,v1):    
    """
    maps a number v1 that is in an interval t1 to another interval t2
    t1 = (lower,upper)

    Parameters
    ----------
    t1(tuple) : the first interval 
    t2(tuple) : the second interval (the one being mapped to)
    v1(int or float) :the number in the first interval

    Returns
    -------
    None.

    """
    
    if type(t1) == int or type(t1) == float:
        t1 = (0,t1)
    
    if type(t2) == int or type(t2) == float:
        t2 = (0,t2)    
    """    
    diff = t1[0] - t2[0]
    
    t2 = t2[0] + diff , t2[1] + diff
    
    r = t2[1] / t1[1]
    
    
    return(v1 * r - diff)
    """
    v1 -= t1[0]
    
    t1 = 0,t1[1]-t1[0]
    
    diff = t2[0]
    
    t2 = 0,t2[1]-t2[0]
    
    r = v1/t1[1]
    
    return(t2[1] * r + diff)








if __name__ == "__main__":
    
    print(map((-1,1),(0,1279),1))        
        

        
        
        
        
        
        
        
        
        
        