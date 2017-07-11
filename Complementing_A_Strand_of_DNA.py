import sys

seq = sys.argv[1]
rev_seq = ''
complement_table = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

seq = seq[::-1]
for base in seq:
    rev_seq += complement_table[base]

print rev_seq
