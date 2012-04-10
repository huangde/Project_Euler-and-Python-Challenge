def IsPalindrome(N):
    """docstring for IsPalindrome"""
    if str(N)[::1]==str(N)[::-1]:
        return True
    else:
        return False

def IsBinPalindrome(N):
    N=str(bin(N))[2:]
    if N[::1]==N[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    sum=0
    for i in range(1,1000001,1):
        if IsPalindrome(i) and IsBinPalindrome(i):
            print i
            sum+=i
