#Create a self timer party
import random
import time

print('Welcome to Self Timer')
print()
print('Everybody stand up')
print('Stay standing until you think the time has ended')
print('then sit down')
print('Anyone still standing when the time ends loses')
print('The last person to sit down befire the time ended will win.')

stand_time = random.randint(5,20)

print('Stay standing for ',stand_time,' seconds.')
time.sleep(stand_time)
print('*******TIME UP********')
