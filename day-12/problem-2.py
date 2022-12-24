import numpy as np
import math


def calculate_neighbour_score(curr_letter, curr_score, neighbour_letter):
    next_score = curr_score - 1

    if ord(curr_letter) - ord(neighbour_letter) <= 1:
        return next_score
    else:
        return 0

def find_valid_neighbours(height_map, reward_map, curr_coord, curr_score):
    (x, y) = curr_coord
    x_lim, y_lim = reward_map.shape[0] - 1, reward_map.shape[1] - 1
    neighbours_coord = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    curr_letter = height_map[x, y]
    valid_neighbours = {}

    for i in range(len(neighbours_coord)):
        (n_x, n_y) = neighbours_coord[i]

        #1) should not be on the edge
        if n_x >= 0 and n_x <= x_lim and n_y >= 0 and n_y <= y_lim:
            neighbour_letter = height_map[n_x, n_y]
            neighbour_score = calculate_neighbour_score(curr_letter, curr_score, neighbour_letter)

            # 2) the score calculated should be higher
            if neighbour_score > reward_map[n_x, n_y]:
                valid_neighbours[neighbours_coord[i]] = neighbour_score

    return valid_neighbours

def update_matrix(reward_map, valid_neighbours):
    for coord, score in valid_neighbours.items():
        (x, y) = coord
        reward_map[x, y] = score
    return reward_map

# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()
map_list = []

#create map
for line in lines:
    line = list(line.rstrip('\n'))
    map_list.append(line)

height_map = np.array(map_list)

# get imp coords
start_x, start_y = np.where(height_map == 'S')
start_coord = (start_x[0], start_y[0])
end_x, end_y = np.where(height_map == 'E')
end_coord = (end_x[0], end_y[0])

height_map[start_x, start_y] = 'a'
height_map[end_x, end_y] = 'z'

# initiate reward map
reward_map = np.zeros(height_map.shape, dtype=int)
highest_score = height_map.size
reward_map[end_coord[0], end_coord[1]] = highest_score

curr_coord_score_dict = {}

#add first value
curr_coord_score_dict[end_coord] = highest_score
terminate = False

print("Height map:\n", height_map)

#update map with best reward from each neighbouring point
while not terminate:
    valid_neighbours_coord_score_dict = {}
    for curr_coord, score in curr_coord_score_dict.items():
        valid_neighbour_exists = False
        temp_neighbours_coord_score_dict = find_valid_neighbours(height_map, reward_map, curr_coord, score)
        for valid_coord, valid_score in temp_neighbours_coord_score_dict.items():
            valid_neighbours_coord_score_dict[valid_coord] = valid_score
        if len(valid_neighbours_coord_score_dict.keys()) > 0:
            valid_neighbour_exists = True
            reward_map = update_matrix(reward_map, valid_neighbours_coord_score_dict)

    if valid_neighbour_exists:
        curr_coord_score_dict = valid_neighbours_coord_score_dict
    else:
        terminate = True

#result
print("Reward map:\n",reward_map)

coords = np.where(height_map == 'a')
min_score = math.inf

for i in range(len(coords[0])):
    x, y = coords[0][i], coords[1][i]
    score = highest_score - reward_map[x, y]
    if score < min_score:
        min_score = score

print("Min score at any \'a\' \n", min_score)