# Title: Date Printer Program
# Program created by William Schaeffer
# CPS 313
# P. 462, Exercise 3, Date Printer Program
# 02.08.22

# This program will read a string from the user containing a date in the form MM//DD/YYY
# It will then display the date in the format March 12, 2018
# This program will validate Month input and day of the month input, but not year input

# imports for functions

import datefunc
import sys                                          # For Command-Line Args

# Main Function

def main():
    
    choice = 'Y'                                    # initialize tested variable to start while loop

    datefunc.welcome_function()                              # call welcome function

    while choice == 'Y':
        
        date_string = input('Please enter date you wish to convert: ')
        #date_string = sys.argv[1]

        date_list = date_string.split('/')

        #print(f'{date_list}')                       # commented print of date list for testing

        date_list = datefunc.convert_date(date_list)

        datefunc.print_date_list(date_list)

        choice = input('\nWould you like to use the Date Printer Program again? Y or N: ')
        choice = datefunc.validate_input(choice)

        print('\n')

    else:
        print(f'Thankyou for using the Date Printer Program')

main()                                              # call main function

