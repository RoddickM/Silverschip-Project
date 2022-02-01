# imports the python file "validation_functions"
from validation_functions import *

# The while loop of the whole program
while True:
    # variables with no values that will have a value later on in the program
    # converted_money - for displaying the amount of money tha is going to be converted
    # transaction_fee - displays the percentage fee of the transaction
    # total_cost - total cost of the whole transaction
    # staff_discount_price - the price
    # currency - shows the currency that is going to be converted to, and also has the symbol of said currency e.g., $
    converted_money = 0
    transaction_fee = 0
    total_cost = 0
    staff_discount_price = 0
    currency = ""

    # below code displays the menu for types of currency available to be converted to
    # it is a function in the file main_function.py
    menu()

    # print statement informs the user
    print(f"\nType {Colors.WARNING}'E'{Colors.END_COLOUR} to exit the program")
    # asks the user for an input of these characters: "1", "2", "3", "4", "5", "E" and "e"
    # validation is available for this input using lists
    # validation is done with a function in validation_function.py
    convert_to = list_answers(f"Type the {Colors.BLUE}number{Colors.END_COLOUR} "
                              f"next to the currency you want to convert to: ",
                              ["1", "2", "3", "4", "5", "E", "e"])

    # exits the code when the letter "E" or "e" is inputted to convert_to
    if convert_to == "e" or convert_to == "E":
        exit("Thank you for using this program!!")

    # asks the user for an amount of money they want to convert to
    # there is validation for both checking whether it is a float and whether it is within a range of values
    # the validation used a function from validation_function.py
    gbp_to_convert = float_range_accept(f"\nPlease enter the amount of {Colors.GREEN}money{Colors.END_COLOUR} "
                                        f"you want to convert to: £", 10, 2500)

    # a variable connected to the function that calculates the transaction fee
    # based on the amount of money they want to convert
    # the function is at main_function.py
    fee = transaction_fee_percentage(gbp_to_convert)

    # if statement that calculates:
    # - the amount of money when it is converted
    # - and the currency symbol based on the user's selection and inputs
    # this calculation is done in a function in main_function.py
    if convert_to == "1":
        converted_money, currency = convert_currency("$", 1.4, gbp_to_convert)
    elif convert_to == "2":
        converted_money, currency = convert_currency("€", 1.14, gbp_to_convert)
    elif convert_to == "3":
        converted_money, currency = convert_currency("R$", 4.77, gbp_to_convert)
    elif convert_to == "4":
        converted_money, currency = convert_currency("¥", 151.05, gbp_to_convert)
    elif convert_to == "5":
        converted_money, currency = convert_currency("₺", 5.68, gbp_to_convert)
    else:
        break

    # does the calculation of the transaction fee and total cost so far
    transaction_fee = gbp_to_convert * fee
    total_cost = gbp_to_convert + transaction_fee

    # calculates the staff discount price and modifies the total cost depending on
    # whether a staff discount is applied or not
    # the calculation is done within a function in main_function.py
    staff_discount_price, total_cost = staff_discount(total_cost)

    # this displays the transaction in a receipt like way
    # this is one with a function in main_function.py
    display_transaction(gbp_to_convert,
                        currency,
                        converted_money,
                        transaction_fee,
                        staff_discount_price,
                        total_cost)

    # below is an option for the user to either continue with another transaction or exit the program
    # it has its own validation method
    # might be turned into a function in the future
    while True:
        # asks the user whether they want to continue
        continue_program = input("\nDo you want to convert another transaction?(Y/N): ")
        if continue_program == "Y" or continue_program == "y":
            # does another interation of the transaction if user chooses this option
            break
        elif continue_program == "N" or continue_program == "n":
            # exits the program if user inputs "n" or "N"
            exit("Thank you for using this program!!")
        else:
            # prints an error message if user inputs anything other than Y or N in upper or lower case
            print(f"\n{Colors.FAIL}[ERROR]{Colors.END_COLOUR}Please enter either Y or N in upper or lower case!!")
