from fundamentals02 import physics

def digit_input(x, message):
    x = input(message)
    if (x.isdigit()):
        return x
    else: 
        while True:
            x = input(message)
            if (x.isdigit() == True):
                break
    return x
            

def main():

    weight = 0
    weight = digit_input(weight,"Please add your weight in kg: ")
    print(f"You would weight {physics.earth_to_moon_weight(int(weight))} kg")

    speed = 0
    speed = digit_input(speed,'How fast are you going rn in km/h?: ')
    print(f"You are going {physics.km_per_hour_to_speed_of_light(int(speed))} % of the speed of light")

    lower_speed = 0
    lower_speed = digit_input(lower_speed, "Puts some speed in km/h and see how many times you broke the sound barier: ")
    print(f"You broke the sound barier {physics.broke_sound_barier(int(lower_speed))}") 

main()