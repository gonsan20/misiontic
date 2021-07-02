#file = open('data.txt', 'r')
with open('data.txt', 'r') as file:
    data = file.read()
    print(data)
    data2 = file.readlines()
    print(data2)
    file.close()