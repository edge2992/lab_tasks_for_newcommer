from Bio import SeqIO
import matplotlib.pyplot as plt

from lab_tutorial.dna.m1_2 import make_comp
from lab_tutorial.dna.m1_4 import PatternMatching


gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def trans_aa(genome):
    start = 'ATG'
    rev_genome = make_comp(genome)
    f_s, f_rv = PatternMatching(start, genome)
    aa = set()

    for f in f_s:
        acid = ''
        for i in range(f, len(genome)-3, 3):
            if gencode[genome[i:i+3]] == '_':
                acid += '_'
                break
            acid += gencode[genome[i:i+3]]
        # print(acid)
        aa.add(acid)

    print(len(aa))

    for f in f_rv:
        acid = ''
        for i in range(f, len(rev_genome)-3, 3):
            if gencode[rev_genome[i:i+3]] == '_':
                acid += '_'
                break
            acid += gencode[rev_genome[i:i+3]]
        # print(acid)
        aa.add(acid)
    print(len(aa))
    return aa


if __name__ == '__main__':
    record = SeqIO.read("data/sequence.fasta", "fasta")
    print("length: ", len(record.seq))
    # print(PatternMatching('ATG', record.seq[:500]))
    print(trans_aa(record.seq))




