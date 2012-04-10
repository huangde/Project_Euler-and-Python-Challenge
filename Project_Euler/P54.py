if __name__=="__main__":
    fid=open('poker.txt','r')
    hands=fid.readlines()
    for hand in hands:
	print hand
