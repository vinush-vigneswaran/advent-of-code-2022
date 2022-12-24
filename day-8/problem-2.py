import numpy as np

# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()

def get_count(arr, threshold, reverse=False):
    _count = 0
    if reverse:
        arr = np.flip(arr)

    for i in range(len(arr)):
        if threshold > arr[i]:
            _count += 1
        else:
            return _count + 1

    return _count

# create matrix of int
first_line = list(map(int, lines[0].rstrip('\n')))

matrix = np.array(first_line)

for line in lines[1:]:
    list_values = list(map(int,line.rstrip('\n')))
    matrix = np.vstack([matrix, list_values])

highest_score = 0

for i in range(1, matrix.shape[0]-1):
    for j in range(1, matrix.shape[1]-1):
        a = matrix[i,j]
        a_top_num = get_count(matrix[0:i,j], a, reverse=True)
        a_bottom_num = get_count(matrix[i+1:,j], a, reverse=False)
        a_left_num = get_count(matrix[i,:j], a, reverse=True)
        a_right_num = get_count(matrix[i,j+1:], a, reverse=False)
        #print(a_top_num, a_bottom_num, a_right_num, a_left_num)

        current_score = a_top_num * a_bottom_num * a_right_num * a_left_num

        if current_score > highest_score:
            highest_score = current_score

#results
print(highest_score)




