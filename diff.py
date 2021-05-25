def contradict(x, y):
    for a in range(0, 7):
        if x[a] == '#' and y[a] == 'X':
            return 0
    return 1

def printt(d):
    for i in d:
        print(i)

def print_seats(q):
    s = ''
    for i in range(0, len(q)):
        s = s + str(q[i])
        if i % 2 == 1:
            s = s + ' '
    return s

def find_row(n, k, line2):
    row = 0
    while row < n:
        if contradict(k[row], line2) == 1:
            return row + 1
        row += 1
    return 0

def convert(pos, row):
    seats = []
    s = 'ABC_DEF'
    for i in range(0, 7):
        if pos[i] == 'X':
            seats += str(row)
            seats += s[i]
    return seats

def final_pos(pos, string):
    s = ''
    for i in range(0, 7):
        if string[i] == '#':
            s += '#'
        elif pos[i] == 'X':
            s += 'X'
        elif pos[i] == '_':
            s += '_'
        else:
            s += '.'
    return s

def update(k):
    s = ''
    for d in k:
        for i in range(0, 7):
            if d[i] == 'X':
                s += '#'
            else:
                s += d[i]
    return s

def update(k):
    row = 0
    for j in k:
        s = ''
        for i in range(0, 7):
            if j[i] == 'X':
                s += '#'
            else:
                s += j[i]
        k[row] = s
        row += 1
    return k

n = int(input())
k = [input() for i in range (1, n+1)]

m = int(input())
S = [input().split() for j in range (1, m+1)]

row = 1
for j in range (0, m):
    k = update(k)
    row1 = 0
    pos = '..._...'
    stop = 1
    if S[j][1] == 'left' and S[j][2] == 'aisle':
        if S[j][0] == '3':
            pos = 'XXX_...'
        if S[j][0] == '2':
            pos = '.XX_...'
        if S[j][0] == '1':
            pos = '..X_...'
    if S[j][1] == 'right' and S[j][2] == 'aisle':
        if S[j][0] == '3':
            pos = '..._XXX'
        if S[j][0] == '2':
            pos = '..._XX.'
        if S[j][0] == '1':
            pos = '..._X..'
    if S[j][1] == 'left' and S[j][2] == 'window':
        if S[j][0] == '3':
            pos = 'XXX_...'
        if S[j][0] == '2':
            pos = 'XX._...'
        if S[j][0] == '1':
            pos = 'X.._...'
    if S[j][1] == 'right' and S[j][2] == 'window':
        if S[j][0] == '3':
            pos = '..._XXX'
        if S[j][0] == '2':
            pos = '..._.XX'
        if S[j][0] == '1':
            pos = '..._..X'

    row = find_row(n, k, pos)
    seats = convert(pos, row)

    while row1 < n and stop == 1:
        if contradict(k[row1], pos) == 1:
            print('Passengers can take seats:', print_seats(seats))
            print('')
            k[row1] = final_pos(pos, k[row1])
            printt(k)
            print('')
            stop = 0
        row1 += 1
    if stop == 1:
        print('Cannot fulfill passengers requirements.')
        print('')
