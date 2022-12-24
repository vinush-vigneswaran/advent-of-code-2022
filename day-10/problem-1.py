import re

# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()

recorded_cycles = [20, 60, 100, 140, 180, 220]

x= [1]
prev_x=0
cycle_num = 0
prev_cycle_num = 0
signal_strength_list = []
i = 0
is_noop = False

for line in lines:
    line = line.rstrip('\n')
    action = line.split()[0]

    if action == "addx":
        cycle_num += 2
        x.append(int(line.split()[1]))
        is_noop = False


    elif action == "noop":
        cycle_num += 1
        is_noop = True

    if is_noop:
        total = sum(x)
    else:
        total = sum(x[:-1])

    if recorded_cycles[i] == cycle_num or (recorded_cycles[i] <=  cycle_num and recorded_cycles[i] >  prev_cycle_num):
        signal_strength = recorded_cycles[i] * total
        signal_strength_list.append(signal_strength)
        i += 1

    if i == len(recorded_cycles):
        break

    prev_cycle_num = cycle_num

print(sum(signal_strength_list))