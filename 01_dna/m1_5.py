from Bio import SeqIO
from Bio.Data import CodonTable
from m1_2 import rev_comp
from m1_4 import Pattern_Matching, all_Pattern_Matching

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

def trans_to_protein(genome):
    # standard_table = CodonTable.unambiguous_dna_by_id[1]
    # starts = standard_table.start_codons
    starts = ['ATG']
    rev_genome = rev_comp(genome)
    f_s = []
    f_rv = []
    for start in starts:
        buf1, buf2 = all_Pattern_Matching(start, genome)
        f_s += buf1
        f_rv += buf2
    aa = set()

    for f in f_s:
        aa.add(cut_protain(genome, f))

    for f in f_rv:
        aa.add(cut_protain(rev_genome, f))

    return aa


def cut_protain(genome, start):
    acid = ''
    for i in range(start, len(genome) -3, 3):
        if gencode[genome[i:i+3]] == '_':
            acid += gencode[genome[i:i+3]]
            break
        acid += gencode[genome[i:i+3]]

    return acid


if __name__ == '__main__':
    record = SeqIO.read("data/sequence.fasta", "fasta")
    ans_set = trans_to_protein(record.seq)
    ans_sorted = sorted(ans_set)

    for amid in ans_sorted:
        print(amid)

    print(len(ans_sorted))