import re

file = "data.txt"
read_file = open(file, 'r')

lines = read_file.readlines()

#current stack condition
stacks = {
    1 : ['F','D','B','Z','T','J','R','N'],
    2 : ['R','S','N','J','H'],
    3 : ['C','R','N','J','G','Z','F','Q'],
    4 : ['F','V','N','G','R','T','Q'],
    5 : ['L','T','Q','F'],
    6 : ['Q','C','W','Z','B','R','G','N'],
    7 : ['F','C','L','S','N','H','M'],
    8 : ['D','N','Q','M','T','J'],
    9 : ['P','G','S']
}

def move_crate(stacks:dict, n_crates:int, from_stack:int, to_stack:int)->dict:

    if len(stacks[from_stack])==0:
        return stacks

    if n_crates > len(stacks[from_stack]):
        n_crates = len(stacks[from_stack])

    to_move_stack = stacks[from_stack][-n_crates:]

    stacks[to_stack] = stacks[to_stack] + to_move_stack[::-1]
    del stacks[from_stack][-n_crates:]

    return stacks

for line in lines:
    action = line.rstrip('\n')
    n_crates, from_stack, to_stack = re.findall(r'\d+', action)
    stacks = move_crate(stacks, int(n_crates), int(from_stack), int(to_stack))

# get results
for keys, value in stacks.items():
   print(value[-1], sep=' ', end='', flush=True)
