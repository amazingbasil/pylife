# -*- coding: utf-8 -*-
def init_field(height=10, width=10, alives=()):
    fld = [[False] * width for _ in range(height)]
    for x, y in alives:
        fld[x][y] = True
    return fld

def alive_neighbours(field, x, y):
    result = []
    for i in range(-int(y != 0), int(y != len(field[0]) - 1) + 1):
        for j in range(-int(x != 0), int(x != len(field) - 1) + 1):
            if (i or j) and field[x + j][y + i]:
                result.append((x + j, y + i))
    return result

def next_step(fld):
    result = [row[:] for row in fld]
    for i in range(len(fld)):
        for j in range(len(fld[1])):
            alive_nb_count = len(alive_neighbours(fld, i, j))
            if fld[i][j] and alive_nb_count not in (2, 3):
                result[i][j] = False
            elif alive_nb_count == 3:
                result[i][j] = True
    return result






