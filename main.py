
#NEW ORDER

while True:
    end = 'no'
    print('Café au Lait new order. \n')
    menu = {'cappuccino': 3.00,'espresso': 2.25,'latte': 2.50,'iced coffee': 2.50}
    coffees = ['cappuccino', 'espresso', 'latte', 'iced coffee']
    inorout = input('dine in or take away? \n')
    taquan = 0
    diquan = 0
    if inorout == 'take away':
        taquan = taquan + 1
    elif inorout == 'dine in':
        diquan = diquan +1
    print(menu)
    more = 'yes'
    while True:
        capq = 0
        espq = 0
        latq = 0
        iceq = 0
        while more == 'yes':
            order = input('\nwhich coffee would you like to order?\n')
            if order == 'cappuccino':
                quan = int(input('how many cappuccinos?\n'))
                capq = capq + quan
            elif order == 'espresso':
                quan = int(input('how many espressos?\n'))
                espq = espq + quan
            elif order == 'latte':
                quan = int(input('how many lattes?\n'))
                latq = latq + quan
            elif order == 'iced coffee':
                quan = int(input('how many iced coffees?\n'))
                iceq = iceq + quan
            more = input('would you like to order more?\n')
        GST = float(menu[order]*quan*0.1)
        total1 = GST + menu[order]*quan
        if inorout == 'take away':
            surcharge = '5%'
            total = total1/100*5 + total1
        elif inorout == 'dine in':
            surcharge = '0%'
            total = GST + menu[order]*quan
        format_total = '{:.2f}'.format(total)
        format_GST = '{:.2f}'.format(GST)
        ethan_is_very_cool_give_him_A = print(f'YOUR ORDER/RECIPT: cappuccino/s: {capq}, espresso/s: {espq}, latte/s: {latq}, iced coffee/s: {iceq}, ${menu[order]*quan}, {inorout}, surcharge/extra charge: {surcharge}, $GST: {format_GST}, TOTAL AMOUNT DUE: ${format_total}.\n')
        more = 'yes'
        orderquan = 0
        if 'your' in 'ethan_is_very_cool_give_him_A':
            orderquan = orderquan + 1
        end = input('are we done for the day?')
        if end == 'yes':
            break
    break


#DAILY SUMMARY

print('Café au Lait daily summary. \n')
print('CUPS (OF JOE):\n'
      f'cappuccino/s: {capq}\n'
      f'expresso/s: {espq}\n' 
      f'latte/s: {latq}\n' 
      f'iced coffee/s: {iceq}\n' )
print('DINE IN AND TAKE AWAY:\n'
      f'take away: {taquan}\n'
      f'dine in: {diquan}\n')
print('NO. OF ORDERS:\n'
      f'{capq+espq+latq+iceq}\n')
print('GST COLLECTED\n'
      f'{format_GST}\n')
print('AMOUNT COLLECTED:\n'
      f'{format_total}\n')

#THE END





