def alphabecode(name):
    import string
    sum=0
    keys=list(string.uppercase)
    values=range(1,27,1)
    namedict=dict(zip(keys,values))
    #print namedict
    for i in name:
	sum=sum+namedict[i]
    return sum

if __name__=="__main__":
    counter=0
    sum=0 
    fid=open('names.txt','r')
    text=fid.read()
    array=text.split(',')
    array.sort()
    for Eng_name in array:
	counter+=1
	Eng_name=Eng_name.strip('\"')
	numcode=alphabecode(Eng_name)
	sum=sum+numcode*counter
	print counter,Eng_name,numcode
	#if counter==1:
	#    break
