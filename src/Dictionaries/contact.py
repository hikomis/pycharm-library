contact ={}
while True:
    name = input("Введите  имя пользователя: ").split('->')
    if name[0] == 'stop':
        break
    elif len(name) > 1:
        if name[0] in contact.keys():
            contact[name[0]].append(name[1])
        else:
            contact.update({name[0]:[]})
            contact[name[0]].append(name[1])
    elif name[0] == 'search':
        while True:
            name = input("Введите  имя пользователя которого ищете: ")
            if name in contact.keys():
                print(*contact.get(name))
            elif name == 'stop':
                break
            else:
                print('Contact',name,'does not exist')
        break



print(contact)

