import time


time_text = input('Enter the cooking time in seconds : ')

#time_int = int(time_text)
time_float = float(time_text)

print('Put the egg in boiling water now')
time.sleep(time_float)
print('Take out the egg now')
