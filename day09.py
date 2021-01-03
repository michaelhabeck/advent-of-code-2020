def load_numbers(filename):
    return list(map(int, open(filename).readlines()))

def find_pair(numbers, sum):
    for i, a in enumerate(numbers):
        for b in numbers[i+1:]:
            if a != b and a + b == sum:
                yield a, b

def find_invalid(numbers, n_preamble=25, n_previous=25):
    for i in range(n_preamble, len(numbers)):
        number = numbers[i]
        if not list(find_pair(numbers[i-n_previous:i], number)):
            return number

def find_range(target, numbers):
    for i in range(len(numbers)):
        sum = numbers[i]
        for j in range(i+1, len(numbers)):
            sum += numbers[j]
            if sum == target:
                return numbers[i:j+1]
            elif sum > target:
                break
            
if __name__ == '__main__':
    
    filename = 'input09.txt'
    numbers = load_numbers(filename)

    invalid = find_invalid(numbers)    
    print('part 1: {0} is invalid'.format(invalid))

    subset = find_range(invalid, numbers)
    print('part 2:', min(subset) + max(subset))
