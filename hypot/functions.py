#addition 
def addition(a, b):
    if isinstance(a, str):
        return "Please just use integer or float"
    elif isinstance(b, str):
        return " Please just use interger or float"
    else:
        return a + b

#squared 
def squared(a):
    return a*a

#sqroot
def sqroot(a):
    return a**0.5

#hypot
def hypot(a, b):
    sa = squared(a)
    sb = squared(b)
    sumAB = addition(sa, sb)
    return sqroot(sumAB)