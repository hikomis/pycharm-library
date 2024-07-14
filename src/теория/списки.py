vim = ['bamam', 'potato', 'tupizm'] # список обозначается []
print (vim[-1].title()) # .title() это для того чтобы была заглавная буква
message = f'My mom {vim[1]}'
print (message)
vim[0] = 'banan' # изменение конкретной позиции списка
print (vim)
vim.append('suzuki') # append() это добавление в КОНЕЦ СПИСКА
print (vim)
car = []
car.append('honda')
car.append('mazda')
car.append('lamborgini')
print (car)
vim.insert(3, 'school') # .insert() нужно для добавление в любую позицию списка
print(vim)
del vim[2] # del это удаление выбранной позиции из списка без возможности больше с ней работать
print(vim)
popped_vim = vim.pop() #popped_vim = vim.pop() это удаление последней позиции в списке с возможностью с ней дальше работать
print (vim)
print (popped_vim) # показывание удалённых элементов с помощью pop()
# pop() может пригодиться например когда нужно узнать какой товар последний раз приобрели
extra = 'potato'
vim.remove(extra) # remove нужно для удаление выбранной позиции из списка с возможностью с ней дальше работать
print(vim)
print (f'\nA {extra.title()} is extra') # например как здесь я указал причину почему я удалил элемент из списка
car.sort() # sort() нужно для сортировки позиций списка по алфавиту
print (car)
car.sort(reverse=True) # (reverse=True) нужно для сортировки в обратном алфавитном порядке
print(car)


print('Это оригинал списка: ')
print (car)
print ("\nЭто изменённая версия списка: ")
print(sorted(car)) #sorted() нужно для временного изменения списка
print('это опять оригинал')
print(car)
car.reverse()# просто обратный порядок списка
print(car)
len(car) #len нужно для определение длины списка