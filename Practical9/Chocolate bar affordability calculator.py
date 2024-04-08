def chocolate_bar_affordability_calculator(total_money, price):
    number_of_bars = total_money//price
    charge = total_money%price
    return number_of_bars, charge
# example
total_money = 100 
price = 7
number_of_bars, charge=chocolate_bar_affordability_calculator(total_money, price)
print(number_of_bars)
print(f"The number of bars that can be bought is {number_of_bars}, and the charge that will be left ove is {charge}")