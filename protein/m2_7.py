import math
import numpy as np
import sys


def calc_ag(filename, chain):
    try:
        fs = open(filename, 'r')
    except OSError as e:
        print(e)
    coord = []
    for line in fs:
        line = line.split()
        if line[0] == 'ATOM' and line[4] == chain and line[2] == 'CA':
            x = float(line[6])
            y = float(line[7])
            z = float(line[8])
            coord.append([x, y, z])
    coord = np.array(coord)
    mass = np.sum(coord, axis=0) / len(coord)
    lens = []
    for x in coord:
        lens.append(np.sqrt(np.sum(np.square(x-mass))))
    lens = np.array(lens)
    return np.sum(lens) / len(lens)


if __name__ == '__main__':
    args = sys.argv
    if 3 <= len(args):
        filename = args[1]
        chain = args[2]
        a = calc_ag(filename, chain)
    else:
        print('Arguments are too short')
    print(a)
