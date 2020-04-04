from Bio import SeqIO
from m1_2 import rev_comp


def Pattern_Matching(pattern, genome):
    ans = []
    for i in range(0, len(genome)-len(pattern), 1):
        if pattern == genome[i:i + len(pattern)]:
            ans.append(i)
    return ans


def all_Pattern_Matching(pattern, genome):
    ans = Pattern_Matching(pattern, genome)
    rev_ans = Pattern_Matching(pattern, rev_comp(genome))
    return ans, rev_ans


if __name__ == '__main__':
    record = SeqIO.read("data/sequence.fasta", "fasta")
    pattern1 = 'GAATTC'
    pattern2 = 'ATG'

    ans1, r_ans1 = all_Pattern_Matching(pattern1, record.seq)
    ans2, r_ans2 = all_Pattern_Matching(pattern2, record.seq)

    print(pattern1 + " :")
    print(ans1)
    print(r_ans1)
    print(pattern2 + " :")
    print(ans2)
    print(r_ans2)

    assert len(ans1) == record.seq.count(pattern1)
    assert record.seq[ans1[0]:ans1[0]+len(pattern1)] == pattern1

    assert len(r_ans1) == record.reverse_complement().seq.count(pattern1)
    assert record.reverse_complement().seq[r_ans1[0]:r_ans1[0]+len(pattern1)] == pattern1
