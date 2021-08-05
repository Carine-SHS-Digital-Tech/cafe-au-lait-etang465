print('Café au Lait daily summary. \n')
menu = {'cappuccino': 3.00,'espresso': 2.25,'latte': 2.50,'iced coffee': 2.50}
inorout = input('dine in or take away? \n')
print(menu)
more = 'yes'
while more == 'yes':
    order = input('\nwhich coffee would you like to order?\n')
    if order == 'cappuccino':
        quan = int(input('how many cappuccinos?\n'))
    elif order == 'espresso':
        quan = int(input('how many espressos?\n'))
    elif order == 'latte':
        quan = int(input('how many lattes?\n'))
    elif order == 'iced coffee':
        quan = int(input('how many iced coffees?\n'))
    more = input('would you like to order more?\n')
GST = float(menu[order]*quan*0.1)
print(f'your order/recipt: {quan} {order}s, $ {menu[order]*quan}, {inorout}, GST: {GST}, TOTAL AMOUNT: $ {GST + menu[order]*quan}.')

DAILY SUMMARY







