if __name__ == '__main__':
    arr=[]
    for a in range(2,101,1):
        for b in range(2,101,1):
            arr.append(a**b)
    print len(set(arr))
