# One Handed Clock

import time

current_time = time.localtime()

hour = current_time.tm_hour
minutes = current_time.tm_min

it_is_time_to_wake_up = (hour>7) or (hour==7 and minutes>29)


if it_is_time_to_wake_up:
    print('IT IS TIME TO WAKE UP')
