class calendar(object):
    """
    a date object discribe year,month and day
    """
        
    def __init__(self,year,month,day,date=0):
        self.year=year
        self.month=month
        self.day=day
        self.date=date
        # self.IsValid(year, day, month)

    def IsValid(self, year, day, month):
        # imput validation
        try:
            assert all(type(i)==int and i>0 for i in [year,month,day])
            assert (month>=1 and month<=12)
            assert (day<=self.daysOfThisMonth())
        except AssertionError:
            print 'OOPS!!! ' + str(self) + ' is not a valid date'
            raise AssertionError
        

    def leapyear(self):
        if self.year%4==0 and self.year%100!=0:
            return True
        if self.year%400==0:
            return True
        return False

    def daysOfMonth(self,month):
        if month in [1,3,5,7,8,10,12]:
            days_m=31
        if month in [4,6,9,11]:
            days_m=30
        if month==2:
            if self.leapyear():
                days_m=29
            else:
                days_m=28
        return days_m


    def daysOfThisYear(self):
        if self.leapyear():
            return 366
        else:
            return 365


            
    def nextday(self):
        self.day+=1
        if self.day>self.daysOfThisMonth():
            self.day=1
            self.month+=1
        if self.month==13:
            self.year+=1
            self.month=1
            self.day=1

    def previousmonth(self):
        day=self.day
        month=self.month-1
        year=self.year
        if month<1:
            month=12
            year=self.year-1
        return calendar(year,month,day)

    def nextmonth(self):
        day=self.day
        month=self.month+1
        year=self.year
        if month>12:
            month=1
            year=self.year+1
        return calendar(year,month,day) 


    def __str__(self):
        DateDict={0:' ',1:'Mon',2:'Tue',3:'Wed',4:'Thr',5:'Fri',6:'Sat',7:'Sun'}
        return str(self.year)+'-'+str(self.month)+'-'+str(self.day)+' '+DateDict[self.date]
        
        
    def __eq__(self,other):
        return (self.year,self.month,self.day,self.date)==(other.year,other.month,other.day,other.date)
        

    def GetDate(self,year,month,day):
        pass


    def __sub__(self,other):
        pass


    def __gt__(self,other):
        a=''.join(map(str,[self.year,self.month,self.day]))
        b=''.join(map(str,[other.year,other.month,other.day]))
        return ((int(a)-int(b))>0)

    def __lt__(self,other):
        return not(self>other) and not(self==other) 


    def yearm():
        doc = """Doc string"""
        def fget(self):
            return self.year+self.month
        def fset(self, value):
            self.year = value
            def fdel(self):
                del self.year
                return locals()
            yearm = property(**yearm())
            

if __name__ == '__main__':
    from datetime import date
    from datetime import timedelta
    a=date(1901,1,1)
    b=date(2000,12,31)
    c=timedelta(days=1)
    NSun=0
    while True:
        if a.weekday()==6 and a.day==1:
            NSun+=1
        if a==b:
            break
        a+=c
    print NSun
        
        
