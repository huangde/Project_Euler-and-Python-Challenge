import itertools
import string
def Pwd_dict_Generator():
    """generate n digits password"""
    dicts=[]
    Pwd_dict=string.lowercase
    Pwd_dict=itertools.combinations(Pwd_dict,3)
    for i in Pwd_dict:
        dicts.append(i)
    return dicts 

def Pwd_Generator():
    """docstring for Pwd_Generator"""
    dicts=Pwd_dict_Generator()
    for key in dicts:
        pwd=itertools.permutations(key)
        for i in pwd:
            yield i

def cyclic_pwd(pwd):
    pwd=itertools.cycle(pwd)
    for i in pwd:
        yield i


def Translator(cipher,key):
    return str(unichr(int(cipher)^ord(key)))

if __name__ == '__main__':
    fid=open('cipher1.txt','r')
    cipher=fid.read()
    cipher=cipher.split(',')
    cipher=map(int,cipher)
    #text=Translator(cipher)
    pwd_generator=Pwd_Generator()
    for key in pwd_generator:
        a=cyclic_pwd(key)
        text=''
        for i in cipher[0:11]:
            b=a.next()
            text+=(Translator(i,b))
            # if text[0] in [' ','\'','\"']:
            #     print key, text
            count=0
            for w in text:
                if w in string.letters:
                    count+=1
                if count>6 and text[0] in ['#']:
                    print key,text
                    
