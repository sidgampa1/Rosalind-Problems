import sys

DNA = sys.argv[1]
motif = sys.argv[2]

motif_indices = []

counter = 0
motif_counter = 0
while (counter < len(DNA)):
    base = DNA[counter]
    if (base == motif[motif_counter]):
        if (motif_counter == len(motif) - 1):
            motif_indices.append(counter - len(motif) + 2)
            motif_counter = 0
        else:
            motif_counter += 1
    else:
        motif_counter = 0
    counter += 1

print(str(motif_indices))
