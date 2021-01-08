import functools
from collections import defaultdict

def load_adapters(filename):
    adapters = list(sorted(map(int, open(filename).readlines())))
    return [0] + adapters + [adapters[-1] + 3]
    
@functools.lru_cache(maxsize = 128) 
def n_paths(n):
    """Number of paths in size-n block of adapters with consecutive joltages.
    """
    a, b, c = 0, 0, 1
    for _ in range(n-1):
        a, b, c = b, c, a+b+c
    return c

if __name__ == '__main__':
        
    filename = 'input10.txt'
    adapters = load_adapters(filename)
    
    # part 1
    counts = defaultdict(int)
    for a, b in zip(adapters, adapters[1:]):
        counts[b-a] += 1
    print('part 1:', counts[1] * counts[3])

    # part 2
    counts, n = 1, 0
    for a, b in zip(adapters, adapters[1:]):
        n += 1
        if b-a == 3:
            counts *= n_paths(n)
            n = 0
    print('part 2:', counts)
