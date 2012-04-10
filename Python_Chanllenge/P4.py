if __name__ == '__main__':
    fid=open('equality.html','r')
    text=(fid.read()).split('<!--')[1]
    print text
    import re
    textmatch=re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]',text)
    #print textmatch
    pswd=''
    for word in textmatch:
        pswd+=(word[4])
    print pswd
