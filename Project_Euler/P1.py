from pdb import set_trace
sum=0
for i in range(1000):
    if (i%3==0 or i%5==0):
        sum=sum+i
	print i,sum
if __debug__:
    print 'test debug mode'
