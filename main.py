print('Café au Lait daily summary. \n')
menu = {1: 'cuppaccino $3.00', 2: 'esppresso $2.25', 3: 'latte $2.50', 4: 'iced coffee $2.50'}
inorout = input('dine in or take away? \n')
print(menu)
order = input('\nwhich coffee would you like to order?')
while more == 'yes':
    input(order)
    if order == 'cuppaccino' or order == '1':
        input('how many cuppaccinos?')
    elif order == 'esspresso' or order == '2':
        input('how many esppressos?')
    elif order == 'latte' or order == '3':
        input('how many lattes?')
    elif order == 'iced coffee' or order == '4':
        input('how many iced coffees?')
    more = input('whould you like to order more?')











