import json

with open('data.txt', 'r') as data_file:
    data = [d for d in data_file.read().split('\n')]

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

