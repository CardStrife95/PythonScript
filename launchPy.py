import time

counter = 10

print('Prepare to launch')
print(counter)

while counter != 0:
    counter = counter - 1
    time.sleep(1)
    print(counter)
    if counter == 0:
        print('LAUNCH')
