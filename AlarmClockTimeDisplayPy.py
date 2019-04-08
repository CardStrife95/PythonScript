# Siren Alarm Clock

import time

current_time = time.localtime()

hour = current_time.tm_hour
minutes = current_time.tm_min

it_is_time_to_wake_up = (hour>7) or (hour==7 and minutes>29)
#it_is_time_to_wake_up = (hour>1) or (hour==1 and minutes>29)

if it_is_time_to_wake_up:
    print('IT IS TIME TO WAKE UP')
    print('RISE AND SHINE')
    print('THE EARLY BIRD GETS THE WORM')
else:
    print('Go back to bed')
print('The time is ',hour,':',minutes,'.')
