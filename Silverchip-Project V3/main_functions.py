# menu function that displays the all the available currency that the program can convert to
# also includes an exit option
def menu():
    display = "\nCurrency options:"
    display += f"\n{Colors.BLUE}[ 1 ]{Colors.END_COLOUR} American Dollars"
    display += f"\n{Colors.BLUE}[ 2 ]{Colors.END_COLOUR} European Euros"
    display += f"\n{Colors.BLUE}[ 3 ]{Colors.END_COLOUR} Brazilian Real"
    display += f"\n{Colors.BLUE}[ 4 ]{Colors.END_COLOUR} Japanese Yen"
    display += f"\n{Colors.BLUE}[ 5 ]{Colors.END_COLOUR} Turkish Lira"
    display += f"\n{Colors.WARNING}[ E ]{Colors.END_COLOUR} To exit the program"
    print(display)


# converts any number into two decimal places
# used when printing currencies
def two_dp(num):
    return format(num, ".2f")


# a function that converts the currency and also calculates the fee and total costs
# also displays the symbol for the chosen currency
# the function returns (in order):
# - the converted amount of money
# - the transaction fee
# - the total cost
# - the currency symbol
def convert_currency(currency_type, currency_from_gbp, original_gbp, transaction_fee):
    converted_money = original_gbp * currency_from_gbp
    fee_money = original_gbp * transaction_fee
    total_cost = original_gbp + fee_money
    currency = f"{currency_type}"
    return converted_money, fee_money, total_cost, currency


# a clas containing all the colours used in the program
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_COLOUR = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# calculates the fee depending on the money the user wants to convert
# returns a decimal/float value
def transaction_fee_percentage(transaction_money):
    if 10 <= transaction_money <= 300:
        return 0.035
    elif 300 < transaction_money <= 750:
        return 0.03
    elif 750 < transaction_money <= 1000:
        return 0.025
    elif 1000 < transaction_money <= 2000:
        return 0.02
    elif 2000 < transaction_money <= 2500:
        return 0.015


# this function calculates both the staff discount
# and modify the total cost depending on whether the customer is a staff or not
# both values are returned from the function
def staff_discount(total_cost_before_discount):
    while True:
        user_input = input(f"\nIs the customer a {Colors.BLUE}staff{Colors.END_COLOUR} member?(Y/N): ")
        if user_input == "Y" or user_input == "y":
            # staff discount and total cost calculation
            staff_discount_price = total_cost_before_discount * 0.05
            total_cost_before_discount = total_cost_before_discount * 0.95
            return staff_discount_price, total_cost_before_discount
        elif user_input == "N" or user_input == "n":
            # no changes needed if customer is not a staff
            return 0, total_cost_before_discount
        else:
            # error message if user enters and invalid value
            print("\nPlease enter either Y or N in upper or lower case!!")


# displays the transaction in a receipt style displaying:
# - how much the user wants to convert to
# - what currency the user wants to convert to
# - the converted money
# - the transaction fee
# - staff discount price
# - total transaction fee
def display_transaction(money_to_convert,
                        currency_to_convert,
                        converted_transaction,
                        transaction_fee,
                        staff_discount_price,
                        total_transaction_cost):
    final_display = "------------------------------------------------------------------------"
    final_display += f"\nConverting £{two_dp(money_to_convert)} to {currency_to_convert}\n\n"
    final_display += f"\nConverted amount".ljust(30) + \
                     f"{Colors.GREEN}{currency_to_convert}{two_dp(converted_transaction)}{Colors.END_COLOUR}\n"
    final_display += f"\nTransaction fee".ljust(30) + f"{Colors.GREEN}£{two_dp(transaction_fee)}{Colors.END_COLOUR}\n"
    final_display += f"\nDiscount".ljust(30) + f"{Colors.GREEN}£{two_dp(staff_discount_price)}{Colors.END_COLOUR}\n"
    final_display += f"\nTotal transaction fee".ljust(30) + \
                     f"{Colors.GREEN}£{two_dp(total_transaction_cost)}{Colors.END_COLOUR}\n"
    final_display += "------------------------------------------------------------------------"
    print(final_display)
