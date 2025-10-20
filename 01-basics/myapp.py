


"""
The program calculates how
many yous would we need
to reach the moon from earth.

In addition it can also calculate
how much energy would be needed to
sustain so many people for one day
"""
distance = 384400000
bodies = 0
def decision() :
    tmp = input('Welcome! Would you like to reach the moon (yes - no)? :')
    if tmp not in ['yes', 'no']:
        while tmp not in ['yes', 'no']:
            tmp = input('Welcome! Would you like to reach the moon (yes - no)? :')

    if tmp == 'no':
        return 0
    if tmp == 'yes':
        return 1

def questioner():
    output = {
        'name': input('What is your name? : ').strip(),
        'height': input('How tall are you(cm)? : '),
        'weight': input('How much do you weigh(kg)? : '),
        'gender': input('What is your gender(male - female)? : '),
        'age': input('How much do you age? : '),
        'activity': input('How much do you move around in your day?'
                          "\n"
                          '\nSedentary: little to no exercise'
                          '\nLight: exercise 1-3 times a week'
                          '\nModerate: exercise 4-5 times a week'
                          '\nActive: daily exercise or intense exercise 3-4 times a week'
                          '\nVery (active): intense exercise 6-7 times a week'
                          '\nExtra (active): very intense exercise daily, or physical job'
                          "\nPython is case sensitive, I'm spellsitive (spelling sensitive)"
                          "\n"
                          '\nAnswer: '),
    }
    return output

def bmr(weight, height, age, gender, activity):
    ''''
    Calculation of BMR for males and females based on their activity
    For men:
        BMR = 10W + 6.25H - 5A + 5
    For women:
        BMR = 10W + 6.25H - 5A - 161
    '''
    if (gender == 'male'):
        match (activity):
            case (activity) if activity.lower().strip() == 'sedentary':
                return ((10 * weight) + (6.25 * height) - (5 * age) + 5) * 1.2
            case (activity) if activity.lower().strip() == 'light':
                return ((10 * weight) + (6.25 * height) - (5 * age) + 5) * 1.375
            case (activity) if activity.lower().strip() == 'moderate':
                return ((10 * weight) + (6.25 * height) - (5 * age) + 5) * 1.55
            case (activity) if activity.lower().strip() == 'very':
                return ((10 * weight) + (6.25 * height) - (5 * age) + 5) * 1.725
            case (activity) if activity.lower().strip() == 'extra':
                return ((10 * weight) + (6.25 * height) - (5 * age) + 5) * 1.9
            case _:
                print("Invalid activity level for BMR calculation (male). Returning 0.")
                return 0
    elif (gender == 'female'):
        match (activity):
            case (activity) if activity.lower().strip() == 'sedentary':
                return ((10 * weight) + (6.25 * height) - (5 * age) - 161) * 1.2
            case (activity) if activity.lower().strip() == 'lightly':
                return ((10 * weight) + (6.25 * height) - (5 * age) - 161) * 1.375
            case (activity) if activity.lower().strip() == 'moderately':
                return ((10 * weight) + (6.25 * height) - (5 * age) - 161) * 1.55
            case (activity) if activity.lower().strip() == 'very':
                return ((10 * weight) + (6.25 * height) - (5 * age) - 161) * 1.725
            case (activity) if activity.lower().strip() == 'extra':
                return ((10 * weight) + (6.25 * height) - (5 * age) - 161) * 1.9
            case _:
                print("Invalid activity level for BMR calculation (female). Returning 0.")
                return 0
    else :
        return 0

def main():
    answer = decision()
    calories = 0
    calories_all = 0
    if answer == 1:
        print('Alright lets get to it!!!')
        p_info = questioner()
        match (int(p_info['height']), int(p_info['weight']), p_info['gender'.lower().strip()], int(p_info['age']), p_info['activity'.lower().strip()]):
            case (height, _, _, _, _) if height > 272:
                print('You cannot be taller than Robert Wadlow')
                exit(1)
            case (height, _, _, _, _) if height < 51:
                print('You cannot be smaller than Chandra Bahadur Dangi')
                exit(1)
            case (_, weight, _, _, _) if weight < 2:
                print('You cannot be lighter than Lucía Zárate')
                exit(1)
            case (_, weight, _, _, _) if weight > 635:
                print('You cannot be fatter than Jon Brower Minnoch')
                exit(1)
            case (_, _, gender, _, _) if gender.lower().strip() not in ['male', 'female']:
                print('Sorry, only two genders exist in this programe :/')
                exit(1)
            case (_, _, _, age, _) if age > 122:
                print('You cannot be older than Jeanne Calment')
                exit(1)
            case (_, _, _, age, _) if age < 15:
                print("Isn't it your bedtime already kiddo?")
                exit(1)
            case (_, _, _, _, _, activity) if activity.lower().strip() not in ['sedentary','light',
                                                                        'moderately', 'very', 'extra']:
                print("If you don't want to do this, then please don't waste my time :(")
                exit(1)
            case _:
                bodies = round(distance / int(p_info['height']))
                calories = bmr(int(p_info['weight']), int(p_info['height']), int(p_info['age']), p_info['gender'], p_info['activity'])
                calories_all = calories * bodies
                print(f'\nWe would need around {bodies} {p_info['name'].capitalize()}s (and a wee bit more) to steal the moon!!!')
                print(f"It would take around {calories_all} calories to keep so many {p_info['name'].capitalize()}s alive for just one day!")
                print("I think there are better ways to steal the moon")
                print('\nSorry I meant REACH :D')
                print('Hahahahahahahhahahah')


    elif answer == 0:
        print('Oh well thats bad I guess :/')
        print('Goodbye!')

main()
