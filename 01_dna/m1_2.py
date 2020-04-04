from Bio import SeqIO


def comp(text):
    dic = {'A': 'T', 'T': 'A', 'G': 'C', 'C':'G'}
    result = ''
    for word in text:
        result += dic[word]

    return result


def rev_comp(text):
    return comp(text)[::-1]


if __name__ == '__main__':
    record = SeqIO.read("data/sequence.fasta", "fasta")
    print(rev_comp(record.seq))
    assert rev_comp(record.seq) == record.reverse_complement().seq

