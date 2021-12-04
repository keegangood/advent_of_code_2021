with open('data.txt', 'r') as data_file:
    diagnostic_report = [d for d in data_file.read().split('\n')]

def to_decimal(binary):
    '''
    Convert each number in the list to decimal by multiplying it by 2 ** n
    where 'n' is the length of the list less the position of the current digit

     8  4  2  1
    [1, 0, 1, 0] => 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 10
    '''
    decimal = 0

    for index, number in enumerate(binary):
        number = int(number)
        exponent = len(binary) - (index + 1)
        decimal += number * (2**exponent)

    return decimal


def get_digit_counts(data):
    output = []
    # create list of 0s to count occurances of 1s in diag report
    ones = [0 for i in data[0]]

    row = 0
    while row < len(data):
        col = 0
        while col < len(data[row]):
            # increase the count for current 'col' position if a '1' exists
            if data[row][col] == '1':
                ones[col] += 1

            col += 1

        row += 1

        # the number of zeros is the length of the data
        # less the number of ones
        zeros = [len(data)-one for one in ones]

    return (zeros, ones)


zeros, ones = get_digit_counts(diagnostic_report)
gamma = [1 if one >= len(diagnostic_report)/2 else 0 for one in ones]
# invert gamma digits to form epsilon array
epsilon = [1 if x == 0 else 0 for x in gamma]

# print(gamma)
# print(epsilon)

# copy diagnostic report. remove rows to find O2 generator
diag_copy = diagnostic_report.copy()

# diag_rate = get_rate(diagnostic_report, 'gamma')
def find_rating(data, criteria):
    prefix = ''
    while len(data) > 1:
        
        zeros, ones = get_digit_counts(data)

        index = len(prefix)

        print(index, len(zeros), len(ones))
        match criteria:
            case 'high':
                if zeros[index] > ones[index]:
                    prefix += '0'
                else:
                    prefix += '1'
            case 'low':
                if zeros[index] <= ones[index]:
                    prefix += '0'
                else:
                    prefix += '1'

        data = [line for line in data if line.startswith(prefix)]

    return data
most_common = find_rating(diag_copy, 'high')
least_common = find_rating(diag_copy, 'low')

print(most_common)
print(least_common)


O2 = to_decimal(most_common[0])
CO2 = to_decimal(least_common[0])

print()
print(O2 * CO2)
