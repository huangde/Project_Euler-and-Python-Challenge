import pickle
if __name__ == '__main__':
    fp=open('banner.p','r')
    tmp=pickle.load(fp)
    for row in tmp:
        a=''
        for sym,num in row:
            a+=sym*num
        print a
