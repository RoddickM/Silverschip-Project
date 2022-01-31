from main_functions import *
from validation_functions import *

while True:
    fee = 0
    converted_money = 0
    fee_money = 0
    total_cost = 0
    staff_discount_price = 0
    currency = ""

    gbp_to_convert = float_range_accept("Please enter the amount of money you want to convert to: £", 10, 2500)

    if 10 <= gbp_to_convert <= 300:
        fee = 0.035
    elif 300 < gbp_to_convert <= 750:
        fee = 0.03
    elif 750 < gbp_to_convert <= 1000:
        fee = 0.025
    elif 1000 < gbp_to_convert <= 2000:
        fee = 0.02
    elif 2000 < gbp_to_convert <= 2500:
        fee = 0.015

    menu()

    print("Type 'E' to exit the program")
    convert_to = list_answers("Type the number next to the currency you want to convert to: ",
                              ["1", "2", "3", "4", "5", "E"])

    if convert_to == "1":
        converted_money, \
            fee_money, \
            total_cost, \
            currency = convert_currency("USD", 1.4, gbp_to_convert, fee)
    elif convert_to == "2":
        converted_money, \
            fee_money, \
            total_cost, \
            currency = convert_currency("EUR", 1.14, gbp_to_convert, fee)
    elif convert_to == "3":
        converted_money, \
            fee_money, \
            total_cost, \
            currency = convert_currency("BRL", 4.77, gbp_to_convert, fee)
    elif convert_to == "4":
        converted_money, \
            fee_money, \
            total_cost, \
            currency = convert_currency("JPY", 151.05, gbp_to_convert, fee)
    elif convert_to == "5":
        converted_money, \
            fee_money, \
            total_cost, \
            currency = convert_currency("TRY", 5.68, gbp_to_convert, fee)
    else:
        break

    while True:
        staff_discount = input("\nIs the customer a staff member?(Y/N): ")
        if staff_discount == "Y" or staff_discount == "y":
            staff_discount_price = total_cost * 0.05
            total_cost = total_cost * 0.95
            break
        elif staff_discount == "N" or staff_discount == "n":
            break
        else:
            print("\nPlease enter either Y or N in upper or lower case\n")

    final_display = f"\nYou want to convert {two_dp(gbp_to_convert)} GBP to {currency}"
    final_display += f"\nConverted amount = {two_dp(converted_money)} {currency}"
    final_display += f"\nTransaction fee = {two_dp(fee_money)} GBP"
    final_display += f"\nDiscount = {two_dp(staff_discount_price)} GBP"
    final_display += f"\nTotal transaction fee = {two_dp(total_cost)} GBP"
    print(final_display)
    
    continue_program = input("\nDo you want to convert another currency?")
    if continue_program == "Y" or continue_program == "y":
        continue
    else:
        break
