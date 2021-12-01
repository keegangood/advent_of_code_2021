
with open('data.txt', 'r') as data_file:
    data = [int(d) for d in data_file.read().split('\n')]

# PART 1
find_increases = lambda data: len([data[i] for i in range(len(data)-1) if data[i] < data[i + 1]])
# print(find_increases(data))

# PART 2
def sonar_sweep(data):
    previous_depth = 0
    increases = 0
    for i in range(len(data)-3):
        depth = sum(data[i:i+3])

        if depth > previous_depth:
            increases += 1

        previous_depth = depth

    return increases 

# print(sonar_sweep(data))