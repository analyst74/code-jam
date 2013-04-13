__author__ = 'Bill'

def process_case(case):
    map = case
    winner = ''

    symbol_sets = []
    #  rows
    for i in range(4):
        symbol_sets.append(map[i])

    # test columns
    for i in range(4):
        symbol_sets.append(''.join([row[i] for row in map]))

    # test diagonal
    symbols = ''
    for i in range(4):
        symbols = symbols + map[i][i]
    symbol_sets.append(symbols)
    symbols = ''
    for i in range(4):
        symbols = symbols + map[i][3-i]
    symbol_sets.append(symbols)

    for symbols in symbol_sets:
        winner = test_winner(symbols)
        if len(winner) > 0:
            return winner

    # unfinished
    if '.' in ''.join(map):
        return 'Game has not completed'

    # draw
    return 'Draw'

def parse_case(file):
    map = []
    for i in range(4):
        line = file.readline().strip()
        map.append(line)

    file.readline()
    return map

def test_winner(symbols):
    if '.' in symbols:
        return ''
    elif 'X' in symbols and 'O' in symbols:
        return ''
    elif 'X' in symbols:
        return 'X won'
    else:
        return 'O won'