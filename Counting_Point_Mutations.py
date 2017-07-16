import sys


seq1 = str(sys.argv[1])
seq2 = str(sys.argv[2])

Hamming_distance = 0
index = 0

while (index < len(seq1)):
    if (seq1[index] != seq2[index]):
        Hamming_distance += 1
    index += 1

print('sequence 1 is ' + seq1)
print('sequence 2 is ' + seq2)
print('The Hamming distance between these two sequences is ' + str(Hamming_distance))
