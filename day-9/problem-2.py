import numpy as np

# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()

head_path = [(0,0)]

tail_paths = {
    1: [(0,0)],
    2: [(0, 0)],
    3: [(0, 0)],
    4: [(0, 0)],
    5: [(0, 0)],
    6: [(0, 0)],
    7: [(0, 0)],
    8: [(0, 0)],
    9: [(0, 0)]
}

def move(coord, action):

    if action == 'D':
        new_loc = (coord[0], coord[1]-1)
    elif action == 'U':
        new_loc = (coord[0],coord[1]+1)
    elif action == 'L':
        new_loc = (coord[0]-1,coord[1])
    elif action == 'R':
        new_loc = (coord[0]+1,coord[1])
    elif action == 'UR':
        new_loc = (coord[0]+1,coord[1]+1)
    elif action == 'UL':
        new_loc = (coord[0]-1,coord[1]+1)
    elif action == 'DR':
        new_loc = (coord[0]+1,coord[1]-1)
    elif action == 'DL':
        new_loc = (coord[0]-1,coord[1]-1)

    return new_loc

def is_within_range(coord1, coord2):
    abs_x = abs(coord1[0] - coord2[0])
    abs_y = abs(coord1[1] - coord2[1])

    if abs_x <= 1 and abs_y <= 1:
        return True
    else:
        return False


def move_tail(curr_tail_state, next_head_state):
    # if same row or column
    if curr_tail_state[0] == next_head_state[0]:
        if curr_tail_state[1] > next_head_state[1]:
            return move(curr_tail_state, 'D')
        else:
            return move(curr_tail_state, 'U')

    elif curr_tail_state[1] == next_head_state[1]:
        if curr_tail_state[0] > next_head_state[0]:
            return move(curr_tail_state, 'L')
        else:
            return move(curr_tail_state, 'R')

    # diagonally
    else:
        dx = curr_tail_state[0] - next_head_state[0]
        dy = curr_tail_state[1] - next_head_state[1]
        if dx < 0 and dy < 0:
            return move(curr_tail_state, 'UR')

        elif dx < 0 and dy > 0:
            return move(curr_tail_state, 'DR')

        elif dx > 0 and dy < 0:
            return move(curr_tail_state, 'UL')

        elif dx > 0 and dy > 0:
            return move(curr_tail_state, 'DL')


for line in lines:
    line = line.rstrip('\n')
    action, num_of_moves = line.split()[0], int(line.split()[1])

    for i in range(num_of_moves):
        curr_head_state = head_path[-1]
        #state 1
        next_head_state = move(curr_head_state, action)
        head_path.append(next_head_state)

        prev_item_state = next_head_state

        for tail_i, tail_path in tail_paths.items():

            curr_tail_state = tail_path[-1]
            if tail_i != 1:
                prev_item_state = tail_paths[tail_i - 1][-1]

            #state i
            if not is_within_range(curr_tail_state, prev_item_state):
                move_to_state = move_tail(curr_tail_state, prev_item_state)
                tail_paths[tail_i].append(move_to_state)

results = len(set(tail_paths[9]))
print(results)








