#timestamp

#import datetime

#timstamp=datetime.date.fromtimestamp(3938483984)                     # A Unix timestamp is the number of seconds between a particular date and January 1, 1970 at UTC.
#print(timstamp)

from datetime import date

timestamp=date.fromtimestamp(943847839)
print(timestamp,"#Unix timestamp is the number of seconds")
