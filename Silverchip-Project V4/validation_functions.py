# imports function from main_function.py for the colours of the text
from main_functions import *


# validates whether the user input is a float
# uses a try catch method
# the parameter entered is th text for the input
# only returns a value when user enters a number
# returns an error message if there is a wrong input
def float_validation(text):
    while True:
        try:
            user_input = float(input(text))
            return user_input
        except ValueError:
            print(f"\n{Colors.FAIL}[ERROR]{Colors.END_COLOUR}Please type in a number!!")


# the function belo makes sure that the user enters a value that is within a list of accepted values
# uses an if else statement
# parameters includes the text for the input and the list filled with answers of accepted value
# returns the user input if they enter a value within the list
# returns an error message if there is a wrong input
def list_answers(text, list_of_answers):
    while True:
        user_input = input(text).strip()
        if user_input in list_of_answers:
            return user_input
        else:
            print(f"\n{Colors.FAIL}[ERROR]{Colors.END_COLOUR}"
                  f"Please only type in one of these characters: {list_of_answers}\n")


# the function below makes sure that a user input is within a certain range
# the function accepts decimals/floats
# has three parameters, one for the text that will be outputted, the minimum accepted value and maximum accepted value
# uses an if statement to catch errors
# returns an error message if there is a wrong input
def float_range_accept(text, start_num, end_num):
    while True:
        user_input = float_validation(text)
        if start_num <= user_input <= end_num:
            return user_input
        else:
            print(f"\n{Colors.FAIL}[ERROR]{Colors.END_COLOUR}"
                  f"Please type in a number between the range of {start_num} and {end_num}!!")
