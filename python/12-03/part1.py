import json
with open('data.txt', 'r') as data_file:
    diagnostic_report = [list(d) for d in data_file.read().split('\n')]


def generate_json(data):
    with open('data.json', 'w') as json_file:
        json_file.write(json.dumps(diagnostic_report, indent=2))


def to_decimal(binary):
    '''
    Convert each number in the list to decimal by multiplying it by 2 ** n
    where 'n' is the length of the list less the position of the current digit

     8  4  2  1
    [1, 0, 1, 0] => 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 10
    '''
    decimal = 0

    for index, number in enumerate(binary):
        exponent = len(binary) - (index + 1)
        decimal += number * (2**exponent)

    return decimal

# create list of 0s to count occurances of 1s in diag report
counts = [0 for i in diagnostic_report[0]]

row = 0
while row < len(diagnostic_report):
    col = 0
    while col < len(diagnostic_report[row]):
        # increase the count for current 'col' position if a '1' exists
        if diagnostic_report[row][col] == '1':
            counts[col] += 1

        col += 1

    row += 1

# replace each value with 1 if the count was greater than
# half of the length of the diag report otherwise 0
gamma = [0 if x <= len(diagnostic_report) // 2 else 1 for x in counts]

# invert gamma digits to form epsilon array
epsilon = [1 if x == 0 else 0 for x in gamma]

gamma = to_decimal(gamma)
epsilon = to_decimal(epsilon)

print(gamma * epsilon)
