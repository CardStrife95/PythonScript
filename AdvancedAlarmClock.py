# One Handed Clock

import time

current_time = time.localtime()

week_day = current_time.tm_wday
year_day = current_time.tm_yday

hour = current_time.tm_hour
minutes = current_time.tm_min

it_is_time_to_wake_up = (hour>7) or (hour==7 and minutes>29)


if it_is_time_to_wake_up:
    print('IT IS TIME TO WAKE UP')
print('Week Day :',week_day,' ',year_day)
print('The time is ',hour,':',minutes)
