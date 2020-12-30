#Timedelta

from datetime import date

t1=date(year=2000,month=11,day=12)
t2=date(year=2005,month=2,day=11)

t3=t2-t1

print(t3)


#Timedelta object

from datetime import timedelta

t1=timedelta(weeks=11,days=5,hours=1,seconds=33)
t2=timedelta(days=4,hours=11,minutes=4,seconds=54)

t3=t1-t2

print("t1-t2 =",t3)

#Negative timedelta

t1=timedelta(weeks=11,days=5,hours=1,seconds=33)
t2=timedelta(days=4,hours=11,minutes=4,seconds=54)

t3=t2-t1

print("t2-t1 =",t3)

#timedelta in seconds

t1=timedelta(weeks=11,days=5,hours=1,seconds=33)
t2=timedelta(days=4,hours=11,minutes=4,seconds=54)

t3=t1-t2

print("t1-t2 =",t3.total_seconds())


#formate date using strftime(dd/mm/yy) /striptime (hh or any other formate

from datetime import datetime

now=datetime.now()

t=now.strftime("%d/%m/%y,%H:%M:%S")        #you can reaarange argument

print("our format==",t)

#TimeZones pytz module

from datetime import datetime

import pytz

local=datetime.now()

tz_NY = pytz.timezone("America/New_York")
datetime_NY=datetime.now(tz_NY)
print("NY:",datetime_NY.strftime("%d/%m/%Y,%H:%M:%S"))

India=pytz.timezone("Asia/Kolkata")
datetime_India=datetime.now(India)
print("Asia/Kolkata:",datetime_India.strftime(("%d/%m/%Y,%H:%M:%S")))

