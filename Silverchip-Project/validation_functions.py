def float_validation(text):
    try:
        user_input = float(input(text))
        return user_input
    except ValueError:
        print("\nPlease type in a number!!\n")


def list_answers(text, list_of_answers):
    user_input = input(text)
    if user_input in list_of_answers:
        return user_input
    else:
        print(f"\nPlease only enter these values: {list_of_answers}\n")


def float_range_accept(text, start_num, end_num):
    user_input = float_validation(text)
    if user_input in range(start_num, end_num+1):
        return user_input
    else:
        print(f"\nPlease enter a number between the range of {start_num} and {end_num+1}\n")

