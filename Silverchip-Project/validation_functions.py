def float_validation(text):
    try:
        user_input = float(input(text))
        return user_input
    except ValueError:
        print("\nPlease type in a number!!\n")


def list_answers(text, list_of_answers):
    user_input = input(text)


def range_accept():
    pass
