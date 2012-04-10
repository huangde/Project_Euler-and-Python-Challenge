if __name__ == '__main__':
    fid=open('ocr.html','r')
    text=fid.read()
    #print text
    import string
    print string.translate(text,None,string.punctuation+'\n')
