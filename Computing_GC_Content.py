import sys

file_name = str(sys.argv[1])
seq = ''
max_ID = ''
max_GC_content = 0

def calcGC(seq, ID):
    count = 0
    global max_GC_content
    global max_ID
    for letter in seq:
        if letter == 'G' or letter == 'C':
            count += 1
    GC = float(count)/len(seq)
    print(ID)
    print(GC)
    if GC > max_GC_content:
        max_GC_content = GC
        max_ID = ID
        print('new max_GC_content')


with open(file_name) as file:
    for line in file:
        if (line[0] == '>'):
            if (seq != ''):
                calcGC(seq, ID)
                seq = ''
            ID = line[1:len(line) - 1]
        else:
            seq += line[:len(line) - 1]

calcGC(seq, ID)
print
print(max_ID)
print(max_GC_content * 100)
