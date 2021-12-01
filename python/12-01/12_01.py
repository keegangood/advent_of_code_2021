
with open('data.txt', 'r') as data_file:
    data = [int(d) for d in data_file.read().split('\n')]

find_increases = lambda data: len([data[i] for i in range(len(data)-1) if data[i] < data[i + 1]])

print(find_increases(data))



