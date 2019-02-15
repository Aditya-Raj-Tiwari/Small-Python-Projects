def tipps_calc():
    money = order_please()
    noofpeople = int(input('Please input the number of people served: '))
    service_quality = int(input('Please input how satisfied you were(%) : '))

    return ((money*service_quality)/noofpeople)/100



def order_please():
    foods = {'pizza': 200, 'momo': 140, 'spagetti': 900, 'yamari': 80}
    totalmoney = 0
    print('----------------------\n'
          '\t\tMenu: \n'
          '----------------------')
    for name, value in foods.items():
        print(f'{name} -- {value}')
    try:
        nameoffood = str(input('Please enter the name of the food you want: ')).lower()
        amount = int(input('Please enter the quantity: '))
        totalmoney += amount * foods[nameoffood]
    except ValueError:
        print('Value not accepted')

    return totalmoney


tipps_amt = tipps_calc()
print('Thanks for {} Rs B-)'.format(tipps_amt))