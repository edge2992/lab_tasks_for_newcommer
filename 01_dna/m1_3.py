from Bio import SeqIO

import matplotlib.pyplot as plt
from matplotlib.font_manager import  FontProperties

font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams["font.size"] = 20


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
    plt.figure(figsize=(20, 10))
    plt.plot(x, r)
    plt.xlabel('bp', fontsize=25)
    plt.ylabel('GC含量(%)', fontsize=25)
    # plt.show()
    plt.savefig('result/1_3.png')

