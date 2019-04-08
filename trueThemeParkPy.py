#Theme Park

while True:
    print('''\nWelcome to our Theme Park

These are the available rides:

1. Sceneic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator
''')

    ride_number_valid = False

    while ride_number_valid == False:
        try:
            ride_number_text = input('Please enter the ride number you want : ')
            ride_number_int = int(ride_number_text)
            ride_number_valid = True
        except ValueError:
            print('Invalid number text. Please enter digits.')
        except KeyboardInterrupt:
            print('Please do not try to stop the program')
    
    while ride_number_int < 1 or ride_number_int > 6:
        ride_number_valid = False
        try:
            print('The ride you pressed is not valid.')
            ride_number_text = input('Please enter the ride number you want : ')
            ride_number_int = int(ride_number_text)
            ride_number_valid = True
        except ValueError:
            print('Invalid number text. Please enter digits.')
        except KeyboardInterrupt:
            print('Please do not try to stop the program')

    if ride_number_int == 1:
        print('You have selected the Scenic River Cruise')
        print('The are no age limits for this ride.')
    if ride_number_int == 2:
        print('You have selected the Carnival Carousel')
        age_text = input('Please enter your age : ')
        age_int = int(age_text)
        while age_int<3:
            print('This age is not valid.')
            age_text = input('Please enter your age : ')
            age_int = int(age_text)
        print('Welcome to the Carnival Carousel')
    if ride_number_int == 3:
        print('You have selected the Jungle Adventure Water Splash')
        age_text = input('Please enter your age : ')
        age_int = int(age_text)
        while age_int<6:
            print('This age is not valid.')
            age_text = input('Please enter your age : ')
            age_int = int(age_text)
        print('Welcome to the Jungle Adventure Water Splash!\n')
    if ride_number_int == 4:
        print('You have selected the Downhill Mountain Run\n')
        age_text = input('Please enter your age : ')
        age_int = int(age_text)
        while age_int<12:
            print('This age is not valid.')
            age_text = input('Please enter your age : ')
            age_int = int(age_text)
        print('Welcome to the Downhill Mountain Run\n')
    if ride_number_int == 5:
        print('You have selected the Regurgitator\n')
        age_text = input('Please enter your age : ')
        age_int = int(age_text)
        while age_int<12 or age_int>70:
            print('This age is not valid.')
            age_text = input('Please enter your age : ')
            age_int = int(age_text)
        print('Welcome to The Regurgitator\n')
        



    

