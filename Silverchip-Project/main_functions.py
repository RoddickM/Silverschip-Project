def menu():
    display = "\nCurrency options:"
    display += "\n[ 1 ] American Dollars"
    display += "\n[ 2 ] European Euros"
    display += "\n[ 3 ] Brazilian Real"
    display += "\n[ 4 ] Japanese Yen"
    display += "\n[ 5 ] Turkish Lira"
    display += "\n[ E ] To exit the program\n"
    print(display)


def two_dp(num):
    return format(num, ".2f")


def convert_currency(currency_type, currency_from_gbp, original_gbp, transaction_fee):
    converted_money = original_gbp * currency_from_gbp
    fee_money = original_gbp * transaction_fee
    total_cost = original_gbp + fee_money
    currency = f"{currency_type}"
    return converted_money, fee_money, total_cost, currency
