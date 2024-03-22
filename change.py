def change():
    expense = 23.75
    money = 100
    print('Ingresar gasto:')
    print(expense)
    print('Dinero recibido')
    print(money)

    print('Vuelto')

    print('Pesos:')
    print(int(money-expense))
    print('Centavos:')
    print(((money-expense)%1)*100)
    
