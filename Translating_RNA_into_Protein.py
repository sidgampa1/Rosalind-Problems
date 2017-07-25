import sys

codon_table = {}
with open('RNA_Codon_Table.txt') as file:
    for line in file:
        keys = line.split()[::2]
        values = line.split()[1::2]
        pairs = zip(keys,values)
        for item in pairs:
            codon_table[item[0]] = item[1]

RNA = sys.argv[1]
codons = [RNA[i:i+3] for i in range(0,len(RNA), 3)]

protein = ''
for codon in codons:
    letter = codon_table[codon]
    if (letter != 'Stop'):
        protein += letter

print(protein)
