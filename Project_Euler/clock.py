class Time(object):
    """A Practice example
    from http://en.wikibooks.org/wiki/Think_Python/Classes_and_functions
    represents the time of day.
       attributes: hour, minute, second"""
        
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
        self.IsValid()

    def __str__(self):
        
        return str(self.hour)+':'+str(self.minute)+':'+str(self.second)

    def __gt__(self,other):
        a=''.join(map(str,[self.hour,self.minute,self.second]))
        b=''.join(map(str,[other.hour,other.minute,other.second]))
        return ((int(a)-int(b))>0)
    """ a pure function version calculate sum of two time"""

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self,seconds):
        minutes, second = divmod(seconds, 60)
        hour, minute = divmod(minutes, 60)
        return Time(hour,minute,second)

    def __add__(t1, t2):
        seconds = t1.time_to_int() + t2.time_to_int()
        return t1.int_to_time(seconds)

    def increment(self,seconds):
        return self.int_to_time(self.time_to_int()+seconds)

    def IsValid(self):
        try:
            assert all(type(i)==int for i in [self.hour,self.minute,self.second]) 
            assert (self.hour>=0 and self.hour<24)
            assert (self.minute>=0 and self.minute<60)
            assert (self.second>=0 and self.second<60)
        except AssertionError:
            print 'OOPS!!! '+str(self)+' is not a valid time'
            raise AssertionError
        
if __name__ == '__main__':
    a=Time(10,20,45)
    b=Time(11,23,30)
    print a>b
    print a.int_to_time(1000)
    print a.time_to_int()
    print a+b
    print a.increment(1000)
    # c=Time(11,73,30)
    # print c.IsValid()
    
