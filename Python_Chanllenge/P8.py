import png
def RGBToGrey(R,G,B):
    """docstring for RGBToGrey"""
    return int(0.2989*R+0.5870*G+0.1140*B)


if __name__ == '__main__':
    a=png.Reader('oxygen.png')
    b=a.read()[2]
    tmp=''
    ###########covert color png file to greyscale###########
    #for col in b:
        #for i in range(0,2516,4):
            #Grey=RGBToGrey(col[i],col[i+1],col[i+2])
            #tmp.append(Grey)
    #fp=open('tmp.png','w')
    #c=png.Writer(width=629,height=95,greyscale=True,bitdepth=8)
    #d=c.array_scanlines(tmp)
    #c.write(fp,d)
    #fp.close()
    #fp=open('tmp.txt','w')
    #tmp_asc=''
    #for i in tmp:
        #tmp_asc+=chr(i)
    #fp.write(tmp_asc)
    #fp.close()
    for col in b:
        for i in range(0,2516,4):
            rgba=(col[i],col[i+1],col[i+2])
            text=map(chr,rgba)
            for j in text:
                tmp+=j
    fp=open('tmp.txt','w')
    fp.write(tmp)
    fp.close()
    #the next level is chr[105,110,116,101,103,114,105,116,121]
    print map(chr,[105,110,116,101,103,114,105,116,121])


    
