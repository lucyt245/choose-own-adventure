def menu_system():
    exit = False
    while not exit:
        print("-------------------------")
        print("Choose your own adventure")
        print("-------------------------")
        print("1 - Start Adventure")
        print("0 - Exit game")
        choice = int_validation()
        if choice == 1:
            choose_adventure()
        elif choice == 0:
            exit = True
        else:
            print("Please enter either 1 or 0")


def int_validation():
    valid = False
    while not valid:
        try:
            choice = int(input("Please enter your decision: "))
            return choice
        except ValueError:
            print("Please enter either 1 or 0")
            valid = False


def choose_adventure():
    print("----------------------")
    print("Goal: Make it to school safely")
    print("----------------------")
    print("You can hear your alarm going off")
    choice = input("a) Press snooze\nb) Get up\n")
    if choice == 'a' or choice == 'A':
        snooze()
    elif choice == 'b' or choice == 'B':
        wake_up()
    else:
        print('Please enter either a or b')
        choose_adventure()


def wake_up():
    print("---------------------")
    print("You wake up and get changed with time to spare")
    choice = input("a) Go to the bus stop early\nb) Play on your Play Station\nc) Beg your mum to drive you to school\n")
    if choice == 'a' or choice == 'A':
        bus()
    elif choice == 'b' or choice == 'B':
        play_game()
    elif choice == 'c' or choice == 'C':
        beg_mum()
    else:
        print("Please enter either a, b, or c")
        wake_up()


def snooze():
    print("---------------------")
    print("Your mum comes into the room and shouts at you")
    choice = input("a) Tell her to go away\nb) Get up\n")
    if choice == 'a' or choice == 'A':
        shut_up()
    elif choice == 'b' or choice == 'B':
        wake_up()
    else:
        print('Please enter either a or b')
        snooze()


def shut_up():
    print("---------------------")
    print("Your mum decides if you are old enough to disrespect her, you are old enough to look after yourself")
    print("You are now homeless")
    loser()


def bus():
    print("---------------------")
    print("You approach the bus stop and see your ex there")
    choice = input("a) Say hi\nb) Sit there in silence\nc) Turn around and walk to school\n")
    if choice == 'a' or choice == 'A':
        say_hi()
    elif choice == 'b' or choice == 'B':
        awkward()
    elif choice == 'c' or choice == 'C':
        walk()
    else:
        print("Please enter either a, b, or c")
        bus()


def play_game():
    print("---------------------")
    print("You lose track of time and miss the bus")
    choice = input("a) Accept defeat and skip school\nb) Beg your mum to drive you to school\n")
    if choice == 'a' or choice == 'A':
        loser()
    elif choice == 'b' or choice == 'B':
        beg_mum()
    else:
        print("Please enter either a or b")
        play_game()


def beg_mum():
    print("---------------------")
    print("Your mum tells you she doesn't have time, but your older sibling offers to drive you instead")
    choice = input("a) Go with them\nb) Walk to school\n")
    if choice == 'a' or choice == 'A':
        drive()
    elif choice == 'b' or choice == 'B':
        walk()


def walk():
    print("---------------------")
    print("On the way, you see a car hit someone and drive off")
    choice = input("a) Help the person\nb) Keep walking\n")
    if choice == 'a' or choice == 'A':
        help_victim()
    elif choice == 'b' or choice == 'B':
        keep_walking()
    else:
        print("Please enter either a or b")
        walk()


def help_victim():
    print("---------------------")
    print("They survive!")
    print("However, you are kept by the police for several hours and fail to make it to school")
    loser()


def keep_walking():
    print("---------------------")
    print("You walk the rest of the way to school without any issues\n")
    print("---------------------")
    print("Congratulations! You made your way to school")
    print("But at what cost?")


def drive():
    print("---------------------")
    print("Your sibling, a learner driver, crashes the car. You have a small scratch on you hand")
    print("However, your sibling is unconscious and bleeding heavily")
    choice = input("a) Call an ambulance and stay with your brother\nb) Get out of the car and keep walking to school\n")
    if choice == 'a' or choice == 'A':
        help_victim()
    elif choice == 'b' or choice == 'B':
        keep_walking()
    else:
        print("Please enter either a or b")
        drive()


def say_hi():
    print("---------------------")
    print("Your ex insults you and you get in an argument")
    print("You get annoyed and storm off into the road, where you get hit by a car and die")
    loser()


def awkward():
    print("---------------------")
    print("Your ex mumbles an insult under his breath and you get in an argument")
    print("You get annoyed and storm off into the road, where you get hit by a car and die")
    loser()


def loser():
    print("YOU LOSE! :)")
    print("Feel free to try again to see if you can make it this time")


menu_system()
