import sys
import math

# file_name = str(sys.argv[1])
#
# with open(file_name) as file:
#     line = file.readline()
#     k = line[0]
#     m = line[2]
#     n = line[4]

k = int(sys.argv[1])
m = int(sys.argv[2])
n = int(sys.argv[3])

total = k + m + m
f = math.factorial
combinations =  4 * f(total)/f(2)/f(total - 2)
print('combinations: ' + str(combinations))


dominant_childs = k * (total - k) * 2
print('dominant_childs: ' + str(dominant_childs))

hetero_hetero_comb = f(m)/f(2)/f(m - 2)
hetero_hetero_childs = hetero_hetero_comb * 3
print('hetero_hetero_childs: ' + str(hetero_hetero_childs))

recessive_hetero_childs = m * n * 2
print('recessive_hetero_childs: ' + str(recessive_hetero_childs))

total_dominant_childs = dominant_childs + hetero_hetero_childs + recessive_hetero_childs
print('total_dominant_childs: ' + str(total_dominant_childs))
total_prob = float(total_dominant_childs) / combinations
print('total_prob: ' + str(total_prob))



# hetero_counter = 0
# while (hetero_counter < m):
#     hetero_child +=
