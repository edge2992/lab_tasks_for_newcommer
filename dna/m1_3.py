from Bio import SeqIO

import matplotlib.pyplot as plt
from lab_tutorial.dna.m1_2 import make_comp


def calc_gc(word, wid=1000, step=300):
    result = []
    for i in range(0, len(word)-wid, step):
        buf = word[i:i+step]
        result.append((buf.count('G') + buf.count('C')) / wid)
    return result


if __name__ == '__main__':
    wid = 1000
    step = 300
    record = SeqIO.read("data/sequence.fasta", "fasta")
    print("length: ", len(record.seq))
    r = calc_gc(record.seq, wid, step)
    r2 = calc_gc(make_comp(record.seq), wid, step)
    x = range(0, len(record.seq)-wid, step)
    plt.figure(figsize=(10, 10))
    plt.plot(x, r)
    plt.plot(x, r2[::-1])
    plt.show()
    plt.savefig('result/m1_3.png')

