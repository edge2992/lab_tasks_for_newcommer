from Bio import SeqIO

record = SeqIO.read("data/sequence.fasta", "fasta")
print("length: ", len(record.seq))

print("A: ", record.seq.count('A'))
print("T: ", record.seq.count('T'))
print("G: ", record.seq.count('G'))
print("C: ", record.seq.count('C'))

