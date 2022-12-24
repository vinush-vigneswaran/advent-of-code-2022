import re
import numpy as np

def values_in_between(x, n_x, y, n_y):
    coords = []

    if x == n_x and y == n_y:
        coords.append((n_x, n_y))
    elif x == n_x:
        sign = np.sign(n_y - y)
        #print(sign)
        for y_i in range(y, n_y, sign):
            coords.append((x, y_i))
        coords.append((x, n_y))

    elif y == n_y:
        sign = np.sign(n_x - x)
        #print(sign)
        for x_i in range(x, n_x, sign):
            coords.append((x_i, y))
        coords.append((n_x, y))

    return coords

def calculate_rest_state(sand_coords, rocks_coords, curr_coord):

    curr_x, curr_y = curr_coord
    next_y = curr_y + 1
    floor_y = (max(rocks_coords, key=lambda tup: tup[1]))[1] + 2

    if (curr_x, next_y) in sand_coords or (curr_x, next_y) in rocks_coords or next_y == floor_y:
        #move left
        left_coord = (curr_x - 1, next_y)

        # if left blocked moved right
        if left_coord in sand_coords or (left_coord in rocks_coords) or left_coord[1] == floor_y:
            right_coord = (curr_x + 1, next_y)

            #if right is blocked = in state
            if right_coord in sand_coords or right_coord in rocks_coords or right_coord[1] == floor_y:
                return (curr_x, curr_y)

            else:
                # move right then repeat
                return calculate_rest_state(sand_coords, rocks_coords, right_coord)
        else:
            # move left then repeat
            return calculate_rest_state(sand_coords, rocks_coords, left_coord)
    else:
        # keep moving down
        below_coord = (curr_x, next_y)
        return calculate_rest_state(sand_coords, rocks_coords, below_coord)


# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()

source_coord = (500,0)
rocks_coords = []

# get all rocks
for line in lines:
    line = line.rstrip('\n')
    line = re.findall(r'\d+', line)


    for i in range(0,len(line)-2,2):
        x, y = int(line[i]), int(line[i+1])
        n_x, n_y = int(line[i+2]), int(line[i+3])
        for coord in values_in_between(x, n_x, y, n_y):
            rocks_coords.append(coord)

# simulate flow
sand_coords = []
source_reached = False

# print("rocks", rocks_coords)
while not source_reached:
# units_of_sand = 28
# for i in range(0, units_of_sand-1):

    sand_rest_state = calculate_rest_state(sand_coords, rocks_coords, source_coord)
    print(source_reached, sand_rest_state)

    if sand_rest_state == source_coord:
        source_reached = True
    else:
        sand_coords.append(sand_rest_state)

#results
print(len(sand_coords)+1)