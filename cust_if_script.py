#!/usr/bin/env python3


def main():
    played_games =int( input("How many Demon Souls/Dark Souls games have you played(including Elden Rings, Sekiro, and Bloodborne)? : ") )

    if played_games > 5:
        print("You're a true master chosen one go forth and bring back the embers")
    elif played_games > 3:
        print("I see you like a little bit of a challenge in your life")
    else:
        print("Train hard and you may find a few more victories")


if __name__== "__main__":
    main()

