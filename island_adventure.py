import random
import math

def start_adventure():
    print("\nWelcome to the tropical island of Bimomba!")
    name = input("What is your name, explorer? ")
    print(f"\nHello, {name}. Your journey begins near the shore of the Bimomba. You come across two converging paths; one through a dense jungle, the other through a dark chasm. ")
    first_choice()

def first_choice():
    choice = input("\nWhich path would you like to take? (jungle/chasm) ")
    if choice.lower() == 'jungle':
        jungle()
    elif choice.lower() == 'chasm':
        chasm()
    else:
        print("Unknown choice, please type 'jungle' or 'chasm'")
        first_choice()


# Jungle Subplot
def jungle():
    print("\nWhile deep into the junge, night wanes and you lose your sense of direction.")
    jungle_choice = input("Make your choice (sleep/continue)")
    if jungle_choice.lower() == 'sleep':
        sleep()
    elif jungle_choice.lower() == 'continue':
        jungle_continue()
    else:
        print("Unknown choice, please type 'sleep' or 'continue'")
        jungle()

def sleep():
    print("\nWhile sleeping an anaconda cyborg injects you with a paralyzing agent and hauls you to their habitat. ")

def jungle_continue():
    print("\nFurther into the jungle darkness falls. Luckily a bioluminescent cyborg bird approaches and offers to guide you. ")
    bird_choice = input("Take the bird up on their offer or stay on your own.Please type (bird/alone)")
    if bird_choice.lower() == 'bird':
        bird()
    elif bird_choice.lower() == 'alone':
        alone()
    else:
        print("Unknown choice, please type 'bird' or 'alone'") 

def bird():
    print("\nThe bird guides you all night. By dawn you encounter a civilization where a intricate network of bridges, boardwalks and causeways lead to highly advanced cabanas.")
    village_choice = input("\nThe bird briefs you on the customs of the village. If you would like to stay in the village for any amount of time, you must be approved by the customs counsel at the embassy. Otherwise you must continue on past the village, The birds informs you there is another, more welcoming village ahead called 'Rundah' but that it can only guide you part of the way. Please choose (embassy/rundah)")
    if village_choice.lower() == 'embassy':
        embassy()
    elif village_choice.lower() == 'rundah':
        rundah_jungle()

# Embassy 
def embassy():
    print("\nAt the embassy, you undergo a rigorous series of tests and interviews. You are told that you can never leave and are given a new identity.")
    print("\nYou will need to answer a few questions in order to recieve your new identity.")

    fav_season = input("What is your favorite season? ")
    fav_food = input("What is your favorite food? ")
    fav_hobby = input("What is your favorite hobby? ")

    new_id = generate_id(fav_season, fav_food, fav_hobby)
    print(f"Your new identity is: {new_id} and you will now reside in the village of Novyo for the remainder of your life.")

def generate_id(season, food, hobby):
    # Take the first three letters of each input and combine them to form a new name
    id_1 = season[:3].capitalize()
    id_2 = food[:3].capitalize()
    id_3 = hobby[:3].capitalize()

    # Combine parts to create a new name
    new_id = f"{id_1}{id_2}{id_3}"
    return new_id

def alone():
    print( "\nYou continue into the jungle alone. You cannot see well and your foot gets trapped in larges vines that constricts you and pulls you into an abyss ")

#Chasm subplot
def chasm():
    print("\nThe chasm opens to a waterfall with a desolate sancuary at the basin. You discover mysterious inscriptions carved into the walls. Suddenly a droning sound emanates from inside the sancuary.")
    chasm_choice = input("\nPlease choose to either go into the temple or continue along the river by typing (temple/river)")
    if chasm_choice.lower() == "temple":
        temple()
    elif chasm_choice.lower() == "river":
        river()

#Temple

def resolve_conflict():
    print("\nYou decide to intervene. Using your newfound knowledge, you guide the villagers in building dams and canals. It takes time and effort, but eventually, the river flows evenly to both villages. As the waters settle, so does the conflict, replaced by cooperation and gratitude.")

def random_universe():
    print("\nYou choose to step back, and as you do, the light swallows you once again. When it clears, you find yourself in an entirely different universe, filled with unknown colors and sounds. Adventure awaits, but the fate of the villages is now out of your hands.")

def make_decision():
    print("\nDo you wish to resolve the war between the villages, or will you let fate take its course and venture into another universe?")
    choice = input("\nType 'resolve' to solve the conflict or 'random' to explore another universe: ").strip().lower()

    if choice == 'resolve':
        rundah_chasm()
    elif choice == 'random':
        random_universe()
    else:
        print("You seem unsure. Let's try that again.")
        make_decision()

def temple():
    print("\nAfter you enter the sancuary you are confronted by a column with shimmering inscriptions that change shape every few seconds. You accidentally step on a stone and the inscriptions light up to reveal 3 sets of numbers. You discover this is a minigame.")

    pass_code = False

    while not pass_code:

        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 100)

        sum_numbers = num1 + num2 + num3

        if sum_numbers % 5 == 0:
            pass_code = True
            print(f"The numbers {num1}, {num2}, {num3} are the keys, The wall sinks into the ground and steps leading down into the sancuary are revealed.")
            print("As you descend further into the sancuary a small beam of light at the landing of the steps grows larger and the droning sound becomes louder and turns into a soothing melodic choir. You are eventually blinded by the light and feel as if you are floating. You envision villagers from both sides prepare for an immenent conflict. As you watch you gain a deep connection to this cause. You are given insight into the resolution of this conflict. A voice tells you that you can either be the beacon of peace or be thrown into a random alternate universe. ")
            make_decision()
        else:
            print(f"The numbers {num1}, {num2}, {num3} are not the keys. Please try again.")

def random_univers():
    print("")

#River
def river():
    print('You decide to continue along the river. After a while a woman in a canoe approaches and inquires about you and your origins. After getting acquainted she offers to give you a ride.')
    river_ride = input("To get in the boat type 'boat'. To continue along the river type 'river'.")
    if river_ride.lower() == 'river':
        river_continue()
    elif river_ride.lower() == 'boat':
        boat_ride()

def river_continue():
    print("Further down the river you are suddenly impaled by several arrows. As you slowly lose conciousness you see several villagers approach.")

def boat_ride():
    print("The boat ride takes you along a diverging river path and through various landscapes. Eventually, you end up in a village where an intricate network of bridges, boardwalks, and causeways lead to highly advanced cabanas.")
    print("The woman docks, and a group of armed soldiers surround the boat. They are about to force you to the embassy for debriefing.")

    while True:
        choice = input("Do you attempt to escape or comply? (escape/comply): ").lower()
        if choice == "comply":
            embassy()
            break
        elif choice == "escape":
            success = random.choice([True, False])  # Randomly decide if the escape attempt succeeds
            if success:
                print("You successfully escape and find a hidden path leading to the jungle.")
                jungle()  # Assuming there's a function to handle this scenario
                break
            else:
                print("Your escape attempt fails. The soldiers recapture you and take you to the embassy.")
        else:
            print("Invalid choice. Please type 'escape' or 'comply'.")


#Rundah - Final Desination
def rundah_jungle():
    print("\nYour journey to Rundah has been long and exhausting. You have travelled through harsh environments and on the brink of collapsing from exhaustion. The mist is so thick that you are disoriented. You decide to rest as your eyes fall you see a figure emerging from the mist.")
    print("\nYou wake up in a room that looks like it is from the end of 2001 A Space Oddysey. A healer steps into the room and welcomes you to Rundah. He offers two elixirs and explains that one will provide tranquility and the other will provide strength")
    elixir_choice = input("Please type (calm/strong)")
    if elixir_choice.lower == 'calm':
        calm()
    elif elixir_choice.lower == 'strong':
        strong()
    else:
        print("Chosen elixir not available. Please choose 'calm' or 'strong'")
    rundah_jungle()

def calm():
    print("\nYou drink the elixir and feel an immediate sense of calm and peace. The room's walls dissolve and you find yourself alone in a sanctuary next to a waterfall.")
    discoveries = 0
    while discoveries < 3:
        print("\nYou explore the sanctuary and notice the column with shimmering inscriptions.")
        choice = input("\nDo you explore the left side, right side, or the column itself? (left/right/column): ")
        if choice == "column":
            print("\nYou touch the column and part of the wall slides open, revealing a hidden passage.")
            discoveries += 1
        elif choice in ["left", "right"]:
            print(f"\nYou explore the {choice} side and find ancient artifacts.")
            discoveries += 1
        else:
            print("\nInvalid direction. Please choose 'left', 'right', or 'column'.")
    print("\nYou've discovered all hidden secrets of the sanctuary.")
    temple()


def strong():
    print("\nYou drink the elixir and feel a jolt. The walls around you collapse and suddenly you are on the fringes of a battleground equipped with a light saber and laser cross-bow. ")

def calculate_distance(velocity, angle, gravity=9.81):
    # Convert angle to radians
    angle_radians = math.radians(angle)
    # Calculate the distance
    distance = (velocity**2) * math.sin(2 * angle_radians) / gravity
    return distance


def calculate_distance(velocity, angle, gravity=9.81):
    """ Calculate the horizontal distance achieved by a projectile launched at `angle` with `velocity`. """
    # Convert angle to radians
    angle_radians = math.radians(angle)
    # Calculate the distance
    distance = (velocity**2) * math.sin(2 * angle_radians) / gravity
    return distance

def rundah_chasm():
    print("\nYou come back to familiar consciousness in a prairie surrounded by mountains. You notice a village built into the side of a mountain and recognize it from the vision earlier. You near the village but reach a point where the only way to get into the village is to catapult yourself onto the elevated village platform.")

    target_distance = 150  # Target distance in meters to the village platform
    gravity = 9.81  # Acceleration due to gravity (m/s^2), constant
    catapult_angle = 45  # degrees, fixed angle for the catapult

    print("\nTo reach the village, you must use the catapult. You need to calculate the correct initial velocity or angle to land on the platform.")
    attempts = 0

    while True:
        try:
            guessed_velocity = float(input("Enter your guess for the initial velocity (in m/s) needed to reach the village: "))
            achieved_distance = calculate_distance(guessed_velocity, catapult_angle, gravity)
            attempts += 1

            if math.isclose(achieved_distance, target_distance, abs_tol=10):  # Providing a tolerance for the solution
                print(f"\nNice job! Your guess of {guessed_velocity} m/s is correct! You safely land on the village platform.")
                prime_minister()
                break
            else:
                print(f"\nYour guess of {guessed_velocity} m/s sends you {achieved_distance:.2f} meters. Try again.")

            # Providing hints based on the number of attempts
            if attempts == 2:
                print("Hint: Remember, the optimal angle for maximum distance in projectile motion without air resistance is 45 degrees.")
            if attempts == 3:
                print("Hint: The formula for the range of a projectile is (v^2 * sin(2*theta)) / g. You know theta (45 degrees) and g (9.81 m/s^2).")
            if attempts == 4:
                print("Additional Hint: A typical velocity range to try might be between 35 m/s and 45 m/s. Adjust your guess based on how close your last attempt was to 150 meters.")
        except ValueError:
            print("Please enter a valid number for the velocity.")


def prime_minister():
    print("\nYou made it to the village platform. You are escorted by guards to the prime minister of the village. The prime minister listens to what you have to say and is compelled by your stance. You succeed in bringing peace to the island of Bimomba!")

def save_outcome(outcome):
    with open("adventure_outcomes.txt", "a") as file:
        file.write(outcome + "\n")

def read_outcomes():
    with open("adventure_outcomes.txt", "r") as file:
        outcomes = file.readlines()
        print("Previous adventure outcomes:")
        for outcome in outcomes:
            print(outcome.strip())

if __name__ == "__main__":
    start_adventure()
