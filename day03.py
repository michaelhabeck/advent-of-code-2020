import numpy as np

TREE = '#'
GRAS = '.'
SYMBOLS = {GRAS, TREE}

def check_field(field):
    lengths = list(map(len, field))
    assert len(set(lengths)) == 1
    symbols = set(list(''.join(field)))
    assert SYMBOLS.issuperset(symbols)

def read_field(filename):
    with open(filename) as handle:
        lines = [line.strip() for line in handle.readlines()]
    return [line for line in lines if line]

def count_trees(field, dx=3, dy=1):
    nx = len(field[0])
    n = 0
    for x, row in enumerate(field[::dy]):
        n += int(row[(x*dx) % nx] == TREE)
    return n

if __name__ == '__main__':

    filename = 'input03.txt'
    field = read_field(filename)
    check_field(field)
    
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    n_trees = [count_trees(field, dx, dy) for dx, dy in steps]
    print(np.prod(n_trees))
