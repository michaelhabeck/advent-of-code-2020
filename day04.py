import re

def count_digits(s):
    return len([c for c in s if c.isdigit()])

def check_range(value, n_digits, lower, upper):
    n = count_digits(value)
    if n != len(value):
        return False
    return lower <= int(value) <= upper

class Validator:

    required_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

    pattern_height = re.compile('([0-9]+)(in|cm)')
    pattern_haircolor = re.compile('(\#[0-9a-z]{6})')

    @classmethod
    def validate1(cls, passport):
        return set(passport.keys()).issuperset(cls.required_fields)
        
    @classmethod
    def validate2(cls, passport):
        if not cls.validate1(passport):
            return False
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if not check_range(passport['byr'], 4, 1920, 2002):
            return False
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if not check_range(passport['iyr'], 4, 2010, 2020):
            return False
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if not check_range(passport['eyr'], 4, 2020, 2030):
            return False
        # hgt (Height) - a number followed by either cm or in:
        if not cls.check_height(passport['hgt']):
            return False
        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if cls.pattern_haircolor.match(passport['hcl']) is None:
            return False
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        value = passport['ecl'].strip()
        if value not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        value = passport['pid']
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not (len(value) == 9 and count_digits(value) == 9):
            return False
        return True

    @classmethod
    def check_height(cls, value):
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        matches = cls.pattern_height.findall(value)
        if len(matches) != 1:
            return False        
        number, unit = matches[0]
        return check_range(number, len(number),
                           150 if unit=='cm' else 59,
                           193 if unit=='cm' else 76)

def parse_passports(filename):
    with open(filename) as handle:
        lines = [line.strip() for line in handle.readlines()]

    pattern = re.compile('([a-z]{3}):([0-9a-z#]+)')

    passports = [{}]
    for line in lines:
        if not line:
            passports.append({})
        else:
            passports[-1].update(dict(pattern.findall(line)))
    return passports

if __name__ == '__main__':

    filename = 'input04.txt'
    passports = parse_passports(filename)

    print('part 1:', sum(list(map(Validator.validate1, passports))))
    print('part 2:', sum(list(map(Validator.validate2, passports))))
