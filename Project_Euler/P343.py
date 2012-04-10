import gcd
def factional_sequen(N,div):
    while(N!=1):
	N,div=N-1,div+1
	if gcd.gcd(N,div)!=1:
	    tmp=gcd.gcd(N,div)
	    N,div=N/tmp,div/tmp
	    #factional_sequen(N,div)
	    N,div=N-1,div+1
    return div
	
