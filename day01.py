import numpy as np

def sum_expenses(expenses, n=2):
    sums = 0. 
    for _ in range(n):
        sums = np.add.outer(sums, expenses)
    return sums

def product_of_expenses(expenses, n_summands, target):
    sums = sum_expenses(expenses, n_summands)
    for i in zip(*np.nonzero(sums == target)):
        return np.prod(expenses[np.array(i)])
        
if __name__ == '__main__':
    
    expenses = np.loadtxt('input01.txt', dtype=int)

    print('part1:', product_of_expenses(expenses, 2, 2020))
    print('part2:', product_of_expenses(expenses, 3, 2020))
