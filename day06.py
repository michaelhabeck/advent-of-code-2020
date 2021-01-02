from functools import reduce

def read_input(filename):
    with open(filename) as handle:
        groups = [[]]
        for line in handle.readlines():
            line = line.strip()
            if not line:
                groups.append([])
            else:
                groups[-1].append(line)
    return groups

def summarize_group1(group):
    return reduce(lambda a, b: a | b, map(set, group))

def summarize_group2(group):
    return reduce(lambda a, b: a & b, map(set, group))

if __name__ == '__main__':
    groups = read_input('input06.txt')
    print(sum([len(summarize_group1(group)) for group in groups]))
    print(sum([len(summarize_group2(group)) for group in groups]))
