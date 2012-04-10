import scipy 

def Gt_Million_comb(n):
    for i in range(1,n/2+1,1):
	if scipy.comb(n,i)>1000000:
	    return n-2*i+1
    return 0

if __name__=="__main__":
    num=0
    for n in range(23,101,1):
	num=num+Gt_Million_comb(n)
    print num
    
