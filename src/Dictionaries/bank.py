bank = {}
while True:
    operation = input("Введите операцию которая вам нужна: ").split()
    if operation[0] == "DEPOSIT":
        if operation[1] in bank.keys():
            bank.update({operation[1]:bank.get(operation[1]) + int(operation[2])})
        else:
            bank.update({operation[1]:int(operation[2])})
    elif operation[0] == 'BALANCE':
        if operation[1] in bank.keys():
            print(bank.get(operation[1]))
        else:
            print('Такого пользователя нет')
    elif operation[0] == 'TRANSFER':
        if (operation[1] in bank.keys()) and (operation[2] in bank.keys()):
            bank.update({operation[1]:bank.get(operation[1]) - int(operation[3])})
            bank.update({operation[2]:bank.get(operation[2]) + int(operation[3])})
        else:
            print('один или более пользователей не найдено')
    elif operation[0] == 'WITHDRAW':
        if operation[1] in bank.keys():
            bank.update({operation[1]: bank.get(operation[1]) - int(operation[2])})
        else:
            print('Такого пользователя нет')
    elif operation[0] == 'INCOME':
        p = 1 + int(operation[1]) / 100
        for i in bank.keys():
            bank.update({i:bank.get(i) * p})








