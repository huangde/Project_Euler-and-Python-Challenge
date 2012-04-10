def gcd(a,b):
    """ a greatest common divisor function"""
    if a<b:
	a,b=b,a
    while a%b!=0:
	a,b=b,a%b
    return b
