#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program finds the sum of all integers from 1 - an inputted number


def main():
    # this function finds the sum of the integers

    # variables
    loop_counter = 0
    sum_of_integers = 0

    # input
    number_as_string = input("Enter a positive integer: ")

    # process & output
    try:
        integer = int(number_as_string)
        if integer > 0:
            while loop_counter <= integer:
                sum_of_integers = sum_of_integers + loop_counter
                loop_counter = loop_counter + 1
            print("\nThe sum of integers 1 - {0} is {1}".format(
                  integer, sum_of_integers))
        else:
            print("\nInvalid Input. Enter a positive integer.")
    except (Exception):
        print("\nInvalid Input. Enter a positive integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
