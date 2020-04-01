from Bio import SeqIO
import matplotlib.pyplot as plt
from DNA_analyze.dna.m1_2 import make_comp


def PatternMatching(pattern, genome):
    ans = []
    rev_ans = []
    for i in range(0, len(genome)-len(pattern), 1):
        if pattern == genome[i:i + len(pattern)]:
            ans.append(i)
    rev_genome = make_comp(genome)
    for i in range(0, len(genome)-len(pattern), 1):
        if pattern == rev_genome[i:i + len(pattern)]:
            rev_ans.append(i)

    return ans, rev_ans


if __name__ == '__main__':
    record = SeqIO.read("../sequence.fasta", "fasta")
    pattern1 = 'GAATTC'
    pattern2 = 'ATG'
    print(PatternMatching(pattern1, record.seq))
    print(PatternMatching(pattern2, record.seq))

    print(record.seq[395:395+len(pattern1)])
