import sys

seq = sys.argv[1]
bases = {'A': 0,'C': 0,'T': 0,'G': 0}

for char in seq:
    for base in bases:
        if char == base:
            bases[base] += 1

for count in bases.values():
    print(str(count) + ' ')
