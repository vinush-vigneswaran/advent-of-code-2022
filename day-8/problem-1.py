import numpy as np

# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()

# create matrix of int
first_line = list(map(int, lines[0].rstrip('\n')))

matrix = np.array(first_line)

for line in lines[1:]:
    list_values = list(map(int,line.rstrip('\n')))
    matrix = np.vstack([matrix, list_values])

# count visible trees
count_visible_trees = (matrix.shape[0] + matrix.shape[1])*2 - 4

for i in range(1, matrix.shape[0]-1):
    for j in range(1, matrix.shape[1]-1):
        a = matrix[i,j]
        a_top = matrix[0:i,j]
        a_bottom = matrix[i+1:,j]
        a_left = matrix[i,:j]
        a_right = matrix[i,j+1:]
        #print(a, a_top, a_bottom, a_left, a_right)

        # visible?
        if ((a > a_top).all()) or ((a > a_bottom).all()) or ((a > a_left).all()) or ((a > a_right).all()):
            count_visible_trees += 1

#results
print(count_visible_trees)





