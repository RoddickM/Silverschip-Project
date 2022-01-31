from validation_functions import *

while True:
    converted_money = 0
    transaction_fee = 0
    total_cost = 0
    staff_discount_price = 0
    currency = ""

    menu()

    print(f"\nType {Colors.WARNING}'E'{Colors.END_COLOUR} to exit the program")
    convert_to = list_answers(f"Type the {Colors.BLUE}number{Colors.END_COLOUR} "
                              f"next to the currency you want to convert to: ",
                              ["1", "2", "3", "4", "5", "E", "e"])

    gbp_to_convert = float_range_accept(f"\nPlease enter the amount of {Colors.GREEN}money{Colors.END_COLOUR} "
                                        f"you want to convert to: £", 10, 2500)

    fee = transaction_fee_percentage(gbp_to_convert)

    if convert_to == "1":
        converted_money, \
            transaction_fee, \
            total_cost, \
            currency = convert_currency("$", 1.4, gbp_to_convert, fee)
    elif convert_to == "2":
        converted_money, \
            transaction_fee, \
            total_cost, \
            currency = convert_currency("€", 1.14, gbp_to_convert, fee)
    elif convert_to == "3":
        converted_money, \
            transaction_fee, \
            total_cost, \
            currency = convert_currency("R$", 4.77, gbp_to_convert, fee)
    elif convert_to == "4":
        converted_money, \
            transaction_fee, \
            total_cost, \
            currency = convert_currency("¥", 151.05, gbp_to_convert, fee)
    elif convert_to == "5":
        converted_money, \
            transaction_fee, \
            total_cost, \
            currency = convert_currency("₺", 5.68, gbp_to_convert, fee)
    else:
        break

    staff_discount_price, total_cost = staff_discount(total_cost)

    display_transaction(gbp_to_convert,
                        currency,
                        converted_money,
                        transaction_fee,
                        staff_discount_price,
                        total_cost)

    continue_program = input("\nDo you want to convert another transaction?(Y/N): ")
    if continue_program == "Y" or continue_program == "y":
        continue
    else:
        break
