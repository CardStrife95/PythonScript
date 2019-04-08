#Create a theme park with age restriction

print('''Welcome to our Theme Park

These are the available rides:

1. Sceneic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator
''')

ride_number_text = input('Please enter the ride number you want : ')
ride_number_int = int(ride_number_text)


if ride_number_int == 1:
    print('You have selected the Scenic River Cruise')
    print('The are no age limits for this ride.')
    
if ride_number_int == 2:
    print('You have selected the Carnival Carousel')
    age_text = input('Please enter your age : ')
    age_int = int(age_text)
    if age_int >= 3:
        print('Welcome to the Carnival Carousel')
    else:
        print('You have to have 3 year old at least.')
        
if ride_number_int == 3:
    print('You have selected the Jungle Adventure Water Splash')
    age_text = input('Please enter your age : ')
    age_int = int(age_text)
    if age_int >= 6:
        print('Welcome to the Jungle Adventure Water Splash')
    else:
        print('You are too young.')
        
if ride_number_int == 4:
    print('You have selected the Downhill Mountain Run')
    age_text = input('Please enter your age : ')
    age_int = int(age_text)
    if age_int >= 12:
        print('Welcome to the Downhill Mountain Run')
    else:
        print('You are too young.')
        
if ride_number_int == 5:
    print('You have selected the Regurgitator')
    age_text = input('Please enter your age : ')
    age_int = int(age_text)
    if age_int >= 12:
        if age_int<70:
            print('Welcome to The Regurgitator')
        else:
            print('You are too old.')
    else:
        print('You are too young.')

