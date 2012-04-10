import zipfile
#from pudb import set_trace; set_trace()
import re
if __name__ == '__main__':
    a=zipfile.ZipFile('channel.zip')
    nxt_file='90052.txt'
    text=a.read(nxt_file)
    tmp=''
    while True:
        print text
        #file_list.append(nxt_file)
        c=a.getinfo(nxt_file)
        tmp+=c.comment
        rep=re.search('\d+',text)
        if rep:
            nxt_file=rep.group(0)+'.txt'
            text=a.read(nxt_file)
        else:
            break
    print tmp
