import math
def Fraction_Series_Generator(n):
    a=int(math.sqrt(n))
    c,b=a,n-a*a
    while True:
	c=a*b
        b=n-c*c
        if b>c:
	    c=b-c
	    a=1
        else:
	    b,c=b/gcd(b,c),c/gcd(b,c)
	    a=c+c
	print (a,b,c)
    	yield (a,b,c)

def gcd(a,b):
    if a<b:
	a,b=b,a
    while(a%b!=0):
	a,b=b,a%b
    return b

