import pytz
from datetime import datetime

timezones = pytz.country_timezones('US')

print(timezones)

#for tz in pytz.all_timezones:
   # print(tz)

asia = pytz.timezone('America/New_York')
print(type(asia))

local_date = asia.localize(datetime.now())
print(type(local_date))
print(local_date)
print(local_date.tzinfo)

local_date1 = datetime.now()
print(local_date1, local_date1.tzinfo)

utcdate = local_date.astimezone(pytz.utc)
print(utcdate)

import arrow

utc = arrow.utcnow()
print(utc,type(utc))

local = utc.to('US/Pacific')
print(local)
print(local.format())