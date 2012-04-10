import divisors

def Tri_Num_Generator():
    i=0
    while True:
        i=i+1
        yield i*(i+1)/2

def Natrual_Num_Generator():
    """docstring for Natrual_Num_Generator"""
    i=0
    while True:
        i=i+1
        yield i

if __name__ == '__main__':
    #a=Tri_Num_Generator()
    #b=a.next()
    #while divisors.div_num(b)<500:
        #b=a.next()
        #print b,divisors.div_num(b)
    #print b

#########version 2:div_num(a*b)=div_num(a)*div_num(b)################
    a=Natrual_Num_Generator()
    b=a.next()
    c=divisors.div_num(b*(b+1)/2)
    while c<500:
        b=a.next()
        if b%2==0:
            c=divisors.div_num(b/2)*divisors.div_num((b+1))
        else:
            c=divisors.div_num(b)*divisors.div_num((b+1)/2)
    print b*(b+1)/2,c

