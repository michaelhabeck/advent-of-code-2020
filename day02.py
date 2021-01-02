import re

PASSWORD = re.compile('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
TYPES = (int, int, str, str)

def parse_password(entry):
    return tuple(t(i) for t, i in zip(TYPES, entry))

def read_passwords(filename):
    with open(filename) as handle:
        content = handle.read()
    return [parse_password(entry) for entry in PASSWORD.findall(content)]

def is_valid1(a, b, letter, phrase):
    return a <= phrase.count(letter) <= b

def is_valid2(a, b, letter, phrase):
    return (phrase[a-1] == letter) ^ (phrase[b-1] == letter)

if __name__ == '__main__':

    entries = read_passwords('input02.txt')

    print('part 1:', sum([is_valid1(*entry) for entry in entries]))
    print('part 2:', sum([is_valid2(*entry) for entry in entries]))

