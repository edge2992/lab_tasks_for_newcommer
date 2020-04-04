from Bio import SeqIO


def count_atgc(req):
    seeds = 'ATGC'
    result = []
    for xx in seeds:
        result.append(record.seq.count(xx))

    return result


if __name__ == '__main__':
    file = "data/sequence.fasta"
    record = SeqIO.read(file, "fasta")
    result = count_atgc(record)
    print(*result)
    assert len(record.seq) == sum(result)

