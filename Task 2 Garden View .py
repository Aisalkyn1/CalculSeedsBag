# Program to calculate amount of grass seeds required by customers

import math


def rectangular():
    area = width * length
    kg5 = area / 100 / 5
    kg5round = math.floor(kg5)
    kg1 = (kg5 - kg5round) * 5
    kg1round = math.ceil(kg1)
    if kg1round == 5:
        kg5round += 1
        kg1round = 0
    price = (kg5round * 60) + (kg1round * 15)
    print("\nAmount of 5kg bag(s) needed: " + str("{:,.0f}".format(kg5round)) + "\nAmount of 1kg bag(s) needed: " +
          str("{:,.0f}".format(kg1round)) + "\nTotal price: NZ$" + str("{:,.2f}".format(price)))
    return"\nThank you for your business!"


def circular():
    pi = math.pi
    area = pi * r * r
    kg5 = area / 100 / 5
    kg5round = math.floor(kg5)
    kg1 = (kg5 - kg5round) * 5
    kg1round = math.ceil(kg1)
    if kg1round == 5:
        kg5round += 1
        kg1round = 0
    price = (kg5round * 60) + (kg1round * 15)
    print("\nAmount of 5kg bag(s) needed: " + str("{:,.0f}".format(kg5round)) + "\nAmount of 1kg bag(s) needed: " +
          str("{:,.0f}".format(kg1round)) + "\nTotal price: NZ$" + str("{:,.2f}".format(price)))
    return"\nThank you for your business!"


shape = None
while shape != '0':
    print("""
    Available options:
    1 - I want grass seeds for a rectangular area
    2 - I want grass seeds for a circular area
    0 - I want to exit the program
    """)

    shape = input("Please select an option: ")
    print()

    if shape == '1':
        print("You have chosen a rectangular area.")
        try:
            width = float(input("\nPlease enter the width in meters: "))
            length = float(input("Please enter the length in meters: "))
            print(rectangular())
        except ValueError:
            print("Invalid input: can not accept text values. Please try again by entering a numerical value.")
            width = float(input("\nPlease enter the width in meters: "))
            length = float(input("Please enter the length in meters: "))
            print(rectangular())

    elif shape == '2':
        print("You have chosen a circular area.")
        try:
            r = float(input("\nPlease enter the radius in meters: "))
            print(circular())
        except ValueError:
            print("Invalid input: can not accept text values. Please try again by entering a numerical value.")
            r = float(input("\nPlease enter the radius in meters: "))
            print(circular())

    elif shape == '0':
        print("Have a nice day!")

    else:
        print("Invalid input. Please select options 1 or 2; select 0 to exit.")
