from datetime import datetime, timedelta
import time

# print(time.time())
# number of sec shows jan 1st 1970


def send_email():
    for i in range(100000):
        i += i


start = time.time()
send_email()
end = time.time()
duration = end - start
# print(duration)


dt = datetime(2018, 1, 1)
dt_now = datetime.now()

# converting string date and time to datetime format
dt_string = datetime.strptime('2018/01/01', '%Y/%m/%d')
print(dt_string)

# reading those sec in human  readability format
readfromtime = datetime.fromtimestamp(time.time())
print(readfromtime)

print(f'{readfromtime.year}/{readfromtime.month}')

# converting datetime to string format
print(type(dt.strftime('%Y/%m')))

print(dt_now > dt)


# working with time delta

# from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 2)
dt2 = datetime.now()

duration = dt2 - dt1

print(duration)
print("days", duration.days)
print("seconds", duration.seconds)
# all day converted into sec with hrs and min
print("total_seconds", duration.total_seconds())

# why we dont have month and year because of varying time


# its provide you addition time after dateime
dt3 = datetime(2020, 1, 1) + timedelta(days=1, seconds=3600)
print(dt3)
