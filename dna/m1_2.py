from Bio import SeqIO


def make_comp(text):
    dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C':'G'}
    result = ''
    for word in text[::-1]:
        result +=dict[word]

    return result


if __name__ == '__main__':
    record = SeqIO.read("data/sequence.fasta", "fasta")
    print("length: ", len(record.seq))
    print(make_comp(record.seq))

