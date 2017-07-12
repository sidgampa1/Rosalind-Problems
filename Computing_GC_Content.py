import sys

file_name = str(sys.argv[1])
file = open(file_name, 'r')

seq = ''
max_ID = ''
max_GC_content = 0

def calcGC(seq):
    count = 0
    for letter in seq:
        if letter == 'G' or letter == 'C':
            count += 1
    return float(count)/len(seq)

for line in file:
    if (line[0] == '>'):
        if (seq != ''):
            GC = calcGC(seq)
            if GC > max_GC_content:
                max_GC_content = GC
                max_ID = ID
            seq = ''
        ID = line[1:]

    else:
        seq += line
