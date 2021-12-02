import json

with open('data.txt', 'r') as data_file:
    data = [d for d in data_file.read().split('\n')]

with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2))


def part1(data):
    position = {
        'forward': 0,
        'depth': 0
    }
    for move in data:
        direction, distance = move.split(' ')
        distance = int(distance)
        match direction:
            case 'forward':
                position['forward'] += distance
            case 'up':
                position['depth'] -= distance
            case 'down':
                position['depth'] += distance
    
    return position['forward'] * position['depth']

# print(part1(data)) # 1714680


def part2(data):
    position = {
        'aim': 0,
        'forward': 0,
        'depth': 0
    }

    for move in data:
        direction, value = move.split(' ')
        value = int(value)
        match direction:
            case 'forward':
                position['forward'] += value
                position['depth'] += position['aim'] * value
            case 'up':
                position['aim'] -= value
            case 'down':
                position['aim'] += value

    return position['forward'] * position['depth']

# print(part2(data))