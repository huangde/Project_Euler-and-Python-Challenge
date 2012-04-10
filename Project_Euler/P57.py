def FractionExpansion():
    numerator=3
    denominator=2
    while True:
	numerator  +=2*denominator
	denominator =numerator-denominator
    	yield numerator,denominator

if __name__=="__main__":
    counter=0
    list=FractionExpansion()
    for i in range(1000):
	numerator,denominator=list.next()
	if len(str(numerator))>len(str(denominator)):
	    counter=counter+1
    print counter	
