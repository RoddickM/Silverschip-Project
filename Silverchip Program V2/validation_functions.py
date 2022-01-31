from main_functions import *


def float_validation(text):
    while True:
        try:
            user_input = float(input(text))
            return user_input
        except ValueError:
            print(f"\n{Colors.FAIL}[ERROR]{Colors.END_COLOUR}Please type in a number!!")


def list_answers(text, list_of_answers):
    while True:
        user_input = input(text)
        if user_input in list_of_answers:
            return user_input
        else:
            print(f"\n{Colors.FAIL}[ERROR]{Colors.END_COLOUR}"
                  f"Please only type in one of these characters: {list_of_answers}\n")


def float_range_accept(text, start_num, end_num):
    while True:
        user_input = float_validation(text)
        if start_num <= user_input <= (end_num + 1):
            return float(user_input)
        else:
            print(f"\n{Colors.FAIL}[ERROR]{Colors.END_COLOUR}"
                  f"Please type in a number between the range of {start_num} and {end_num}!!")
