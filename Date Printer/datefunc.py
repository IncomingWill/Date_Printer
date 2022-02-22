# Title: Date Printer Program
# Program created by William Schaeffer
# CPS 313
# P. 462, Exercise 3, Date Printer Program
# 02.08.22

# Function definitions for Date Printer Program

    # Welcome Function to introduce program

def welcome_function(): 

    print(f'\tWelcome to the Date Printer Program!\n\n')
    print(f'This program will convert date from the format 01/01/2020 to January 01, 2020.\n')

# Function to convert date month from number to word
    # Commented out sections are for user input

def convert_date(list):
    
    month = list[0]

    month = month_swap(month)

    list[0] = month

    day = list[1]

    day = validate_day(day)

    list[1] = day
    
    return list

    # Function to swap month number with month name
        # Also tests for invalid input

def month_swap(m):
       
    flag = 0                                        # set flag for user input verification

    while(flag == 0):

        flag = 1                                    # will exit loop unless invalid input for month

        if (m == '01' or m == '1'):
            m = 'January'
        elif (m == '02' or m == '2'):
            m = 'February'
        elif (m == '03' or m == '3'):
            m = 'March'
        elif (m == '04' or m == '4'):
            m = 'April'
        elif (m == '05' or m == '5'):
            m = 'May'
        elif (m == '06' or m == '6'):
            m = 'June'
        elif (m == '07' or m == '7'):
            m = 'July'
        elif (m == '08' or m == '8'):
            m = 'August'
        elif (m == '09' or m == '9'):
            m = 'September'
        elif (m == '10'):
            m = 'October'
        elif (m == '11'):
            m = 'November'
        elif (m == '12'):
            m = 'December'
        else:
            m = input('Month input not recognized. Please try again: ')
            flag = 0                                # reset flag for retest
            continue                                # to restart while loop due to invalid input

    return m

    # Function to validate user input to rerun program

def validate_day(d):

    while (int(d) <= 0 or int(d) >= 31):
        d = input('Day input is invalid. Cannot be less than 1 or greater than 31. Please try again: ')

    d = str(d)

    return d

def validate_input(i):

    i = i.upper()

    while (i != 'Y' and i != 'N'):
            i = input('\nInvalid input. Please enter Y or N: ').upper()

    return i

    # Fuction to print date in proper format

def print_date_list(date_list):
    month = date_list[0]
    day = date_list[1]
    year = date_list[2]

    print(f'{month} {day}, {year}')
