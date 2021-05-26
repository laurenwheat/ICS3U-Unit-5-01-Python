#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program displays all integers 1000-2000


def fahrenheit():

    temp_c = input("Enter a temperature in Celcius: ")

    try:
        temp_c_int = int(temp_c)

        fahrenheit_temp = (9/5) * temp_c_int + 32

        print("{0} is equal to {1}".format(temp_c_int, fahrenheit_temp))

    except Exception:
        print("That is not a valid temperature!!!!!")
    finally:
        print("Thanks for playing <3")


def main():

    fahrenheit()


if __name__ == "__main__":
    main()
