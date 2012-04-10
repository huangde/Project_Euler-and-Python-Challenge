import string
if __name__ == '__main__':
    # alphabet dict
    alphabetdict={}
    letters=string.uppercase
    keys=range(1,len(letters)+1)
    for i in range(len(letters)):
        alphabetdict[letters[i]]=keys[i]
    # triangle number list
    trinum=[i*(i+1)/2 for i in range(1,21)]
    fp=open("words.txt",'r')
    words=fp.read().replace('"','').split(',')
    count=0
    for w in words:
        # c=sum(map(lambda x:alphabetdict[x],w[1:len(w)-1]))
        c=sum(map(lambda x:alphabetdict[x],w))
        if c in trinum:
            count+=1
    print count
