# Number validation

ride_number_text = input('Please enter the ride number you want : ')
ride_number_int = int(ride_number_text)

while ride_number_int < 1 or ride_number_int > 6:
    print('No Valid.')
    ride_number_text = input('Please enter the ride number you want : ')
    ride_number_int = int(ride_number_text)

print('You have selected the ride ',ride_number_int,'.')
