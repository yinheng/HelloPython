import time
import calendar

print(time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))

print(calendar.month(2018, 1))