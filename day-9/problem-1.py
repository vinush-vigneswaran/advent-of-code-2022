import numpy as np

# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()

head_path = [(0,0)]
tail_path = [(0,0)]

def move(coord, action):

    if action == 'D':
        new_loc = (coord[0], coord[1]-1)
    elif action == 'U':
        new_loc = (coord[0],coord[1]+1)
    elif action == 'L':
        new_loc = (coord[0]-1,coord[1])
    elif action == 'R':
        new_loc = (coord[0]+1,coord[1])

    return new_loc

def is_within_range(coord1, coord2):
    abs_x = abs(coord1[0] - coord2[0])
    abs_y = abs(coord1[1] - coord2[1])

    if abs_x <= 1 and abs_y <= 1:
        return True
    else:
        return False


def move_tail(curr_tail_state, next_head_state, action):
    # if same row or column
    if curr_tail_state[0] == next_head_state[0] or curr_tail_state[1] == next_head_state[1]:
        return move(curr_tail_state, action)

    # diagonally
    else:
        dx = curr_tail_state[0] - next_head_state[0]
        dy = curr_tail_state[1] - next_head_state[1]
        if dx < 0 and dy < 0:
            # move diagonally UR
            move1 = move(curr_tail_state, 'U')
            move2 = move(move1, 'R')
            return move2
        elif dx < 0 and dy > 0:
            # move diagonally DR
            move1 = move(curr_tail_state, 'D')
            move2 = move(move1, 'R')
            return move2
        elif dx > 0 and dy < 0:
            # move diagonally DU
            move1 = move(curr_tail_state, 'U')
            move2 = move(move1, 'L')
            return move2
        elif dx > 0 and dy > 0:
            # move diagonally DL
            move1 = move(curr_tail_state, 'D')
            move2 = move(move1, 'L')
            return move2


for line in lines:
    line = line.rstrip('\n')
    action, num_of_moves = line.split()[0], int(line.split()[1])

    for i in range(num_of_moves):
        curr_head_state = head_path[-1]
        #state 1
        next_head_state = move(curr_head_state, action)
        head_path.append(next_head_state)

        curr_tail_state = tail_path[-1]

        #state 2
        if not is_within_range(curr_tail_state, next_head_state):
            next_tail_state = move_tail(curr_tail_state, next_head_state, action)
            tail_path.append(next_tail_state)

results = len(set(tail_path))
print(results)







