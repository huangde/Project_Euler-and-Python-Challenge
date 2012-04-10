if __name__ == '__main__':
    import urllib2
    import re
    urlbase='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    in_file=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579')
    nxtID=(re.search('\d+',in_file.read())).group(0)
    while nxtID:
        in_file=urllib2.urlopen(urlbase+nxtID).read()
        print nxtID,in_file
        nxtID=(re.search('\d+',in_file)).group(0)
        
