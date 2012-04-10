import re
# class Node(object):
#     """
#     class record the xpos,ypos and the value of nodes
    
#     """
    
#     def __init__(self,Xpos,Ypos):
#         """
#         """
#         self.Xpos=Xpos
#         self.Ypos=Ypos


#     def __hash__(self):
#         return hash((self.Xpos, self.Ypos))

#     def __eq__(self, other):
#         return (self.Xpos, self.Ypos) == (other.Xpos, other.Ypos)

def Parents(i,j):
    if i==1 & j==1:
        return []
    if i==2:
        return [(1,1)]
    if i==j:
        p=[(i-1,j-1)]
        return p
    if j==1:
        p=[(i-1,j),(i-1,j+1)]
        return p
    return [(i-1,j-1),(i-1,j)]



if __name__ == '__main__':
    # open file and read the numbers into a list
    fp=open('P67.txt','r')
    text=fp.readlines()
    list={}
    SumSoFar={}
    list[(1,1)]=59
    SumSoFar[(1,1)]=list[(1,1)]
    row=0
    totalrows=100

    
    for line in text:
        row+=1
        col=1
        nums=map(int,line.split(' '))
        for node in nums:
            list[(row,col)]=node
            col+=1
    # print list 


    for i in range(1,totalrows+1):
        for j in range(1,i+1):
            NodeParents=Parents(i,j)
            tmp=0
            for p in NodeParents:
                # print list[(i,j)],list[p]
                if SumSoFar[p]>tmp:
                    tmp=SumSoFar[p]
                SumSoFar[(i,j)]=tmp+list[(i,j)]
    print max(SumSoFar.values())
