# One Handed Clock

import time

current_time = time.localtime()

year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday

hour = current_time.tm_hour
minutes = current_time.tm_min
secondes = current_time.tm_sec

print('We are :',month,'/',day ,'/',year)
print('Time is :',hour,':',minutes,':',secondes)
