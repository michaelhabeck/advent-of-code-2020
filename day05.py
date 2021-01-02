TABLE = {
    'F': '0', 'B': '1', # row
    'L': '0', 'R': '1', # col
    }
TABLE = str.maketrans(TABLE)

def decode_pass(boarding_pass):
    bincode = boarding_pass.translate(TABLE)
    seatid = int(bincode, 2)
    row, col = seatid // 8, seatid % 8
    return row, col, seatid

def test():
    boarding_pass = ['FBFBBFFRLR', # row 44, column 5, seat ID 357
                     'BFFFBBFRRR', # row 70, column 7, seat ID 567
                     'FFFBBBFRRR', # row 14, column 7, seat ID 119
                     'BBFFBBFRLL', # row 102, column 4, seat ID 820
                     ][2]

    row, col, seatid = decode_pass(boarding_pass)
    print('\nrow {0}, column {1}, seat ID {2}'.format(row, col, seatid))    

if __name__ == '__main__':
    
    with open('input05.txt') as handle:
        entries = [line.strip() for line in handle.readlines()]

    passes = list(map(decode_pass, entries))
    passes.sort(key=lambda x: x[-1])
    seatids = list(zip(*passes))[2]

    print('\npart 1: max seat ID is', max(seatids))

    print('part 2:', end=' ')
    for a, b in zip(seatids, seatids[1:]):
        if b-a != 1:
            print('missing seat IDs:', tuple(range(a+1, b)))


