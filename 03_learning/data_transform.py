import pandas as pd
import numpy as np


def scale2df(filename, size=35):
    df = pd.DataFrame()

    with open(filename, "r") as f:
        num = 0
        for line in f:
            # print(line)
            buf = line.split()
            seri = pd.Series(name=num, dtype=np.float64)
            seri['0'] = buf[0]
            for one in buf[1:]:
                youso = one.split(':')
                seri[youso[0]] = youso[1]
            df = df.append(seri)
            num += 1

    return df



if __name__ == '__main__':
    filename = "data/ionosphere.scale"
    df = scale2df(filename)
    print(df.head())
    df.to_csv("data/ionosphere.csv")



