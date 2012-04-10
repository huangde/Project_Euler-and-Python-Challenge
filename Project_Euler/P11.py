# import pdb
import re

import pylab


# pdb.set_trace()
# from pdb import set_trace
def maxprodcut_list4(arrlist):
    """docstring for maxprodcut"""
    if len(arrlist)==4:
        prod=1
        for i in arrlist: 
            prod*=i
        return prod
    if len(arrlist)>4:
        maxprod=arrlist[0]*arrlist[1]*arrlist[2]*arrlist[3]
        for i in range(0,len(arrlist)-4):
            if arrlist[i+4]>arrlist[i]:
                prod=arrlist[i+1]*arrlist[i+2]*arrlist[i+3]*arrlist[i+4]
                if prod>maxprod:
                    maxprod=prod
            else:
                continue
        return maxprod

def right_diag(ini_i,ini_j):
    """docstring for right_diag"""
    while ini_i<20 and ini_j<20:
        tmp=(ini_i,ini_j)
        ini_i+=1
        ini_j+=1
        yield tmp


def left_diag(ini_i,ini_j):
    """docstring for left_diag"""
    while ini_i<20 and ini_j>=0:
        tmp=(ini_i,ini_j)
        ini_i+=1
        ini_j-=1
        yield tmp


if __name__ == '__main__':
    a,b=[],[]
    fp=open('P11.html','r')
    for text in fp:
        if re.match('^\d{2}',text):
            a.append(map(int,re.findall('(?<!\d)\d{2}(?!\d)',text)))
    print max(map(maxprodcut_list4,a))
    print max(map(maxprodcut_list4,pylab.transpose(a)))
    for ini_i in range(20):
        tmp1=[]
        for i,j in right_diag(ini_i,0):
            tmp1.append(a[i][j])
        b.append(tmp1)
        tmp1=[]
        for i,j in right_diag(0,ini_i):
            tmp1.append(a[i][j])
        b.append(tmp1)
        tmp1=[]
        for i,j in left_diag(0,ini_i):
            tmp1.append(a[i][j])
        b.append(tmp1)
        tmp1=[]
        for i,j in left_diag(ini_i,19):
            tmp1.append(a[i][j])
        b.append(tmp1)
    print max(map(maxprodcut_list4,b))
