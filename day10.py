import numpy as np
import functools

def load_adapters(filename):
    adapters = np.sort(np.loadtxt(filename, dtype=int))
    #  charging outlet - adapters - device
    return np.hstack([0, adapters, adapters[-1] + 3])
    
@functools.lru_cache(maxsize = 128) 
def n_paths(n):
    """Number of paths in size-n block of adapters with consecutive joltages.
    """
    x = [1]
    while len(x) < n:
        x.append(sum(x[-3:]))
    return x[-1]
        
if __name__ == '__main__':
        
    filename = 'input10.txt'
    adapters = load_adapters(filename)

    # part 1
    jolts = np.diff(adapters)
    assert np.all(jolts <= 3)

    _, counts = np.unique(jolts, return_counts=True)
    print('part 1:', np.prod(counts))

    # determine sizes of consecutive blocks of adapters that differ
    # by only one jolt
    indices = np.nonzero(jolts==3)[0] + 1
    sizes = np.diff(np.hstack([0, indices, len(adapters)]))

    # unique list of sizes 
    sizes, n = np.unique(sizes, return_counts=True)
    counts = np.array(list(map(n_paths, sizes)))

    print('part 2:', np.prod(counts**n))
