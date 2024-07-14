s = '1.1.1.1'
result = [int(char) if char.isdigit() else char for char in s]
for i in range(0,len(result)):
    if result[i] == '.':
        result[i] = '[.]'

        print(result)
