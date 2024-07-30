#python list comprehension
numbers = [12, 13, 14,]
doubled = [x * 2 for x in numbers]
print(doubled)

# dictionary comprehension
#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)
