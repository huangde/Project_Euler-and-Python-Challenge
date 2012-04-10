def listproduct(list):
    product=1
    for i in list:
	product=product*int(i)
    return product


import re
if __name__=="__main__":
    array=[]
    fid=open('P8.html','r')
    text=fid.readlines()
    for line in text:
    	if re.match('[0-9]{50}',line):
	    array+=re.match('[0-9]{50}',line).group(0)
    init=array[0:5]
    product=listproduct(init)
    print 'init=',init,'product=',product
    for i in array[5:]:
	init.append(i)
	out=init.pop(0)
	input=init[-1]
	if int(input)>int(out):
	    tmp=listproduct(init)
	    if tmp>product:
		product=tmp
    	print 'init=',init,'product=',product
    fid.close()
