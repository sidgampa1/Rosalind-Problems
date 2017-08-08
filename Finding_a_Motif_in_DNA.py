import sys

DNA = sys.argv[1]
motif = sys.argv[2]

motif_indices = []

counter = 0
while (counter < len(DNA)):
    if (DNA[counter:(counter + len(motif))] == motif):
        motif_indices.append(counter + 1) 
    counter += 1

print(str(motif_indices))
