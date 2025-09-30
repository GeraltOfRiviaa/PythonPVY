"""
The program calculates how
many yous would we need
to reach the moon from earth.
"""
distance = 384400
bodies = 0
answer = input('Welcome! Would you like to reach the moon (yes - no)? :').strip
while answer not in ['yes', 'no']:
    answer = input('Welcome! Would you like to reach the moon (yes - no)? :')

if answer == 'yes':
    print('Alright lets get to it!!!')
    name = input('What is your name? : ').strip()
    height = input('\nHow tall are you? : ')

    if int(height) > 251:
        print('You cannot be taller than the talles man on Earth!!!')

    bodies = round(distance / int(height))
    print('\nWe would need around {} {}s (and a wee bit more) to steal the moon!!!'.format(bodies, name.capitalize()))
    print('Sorry I meant REACH :D')
    print('Hahahahahahahhahahah')

elif answer == 'no':
    print('Oh well thats bad I guess :/')
    print('Goodbye!')
