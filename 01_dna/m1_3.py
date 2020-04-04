from Bio import SeqIO

import matplotlib.pyplot as plt


def calc_gc(word, wid=1000, step=300):
    result = []
    for i in range(0, len(word)-wid, step):
        buf = word[i:i+step]
        result.append((buf.count('G') + buf.count('C')) / wid)
    return result


if __name__ == '__main__':
    w = 1000
    s = 300
    record = SeqIO.read("data/sequence.fasta", "fasta")
    r = calc_gc(record.seq, w, s)
    x = range(0, len(record.seq)-w, s)
    plt.figure(figsize=(10, 10))
    plt.plot(x, r)
    # plt.show()
    plt.savefig('result/1_3.png')

