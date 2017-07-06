import sys

dna = sys.argv[1]
rna = ""
for letter in dna:
    if (letter == 'T'):
        rna += 'U'
    else:
        rna += letter
print(rna)
