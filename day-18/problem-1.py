# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()

class Cube():
    def __init__(self, coord):
        self.coord = coord
        self.n_exposed_sides = 6

def check_neighbours(cube, cubes):
    x1, y1, z1 = cube.coord

    num_neighbours = 0

    for other_cube in cubes:
        x2, y2, z2 = other_cube.coord

        abs_dx_bool = (abs(x1-x2) == 1)
        abs_dy_bool = (abs(y1-y2) == 1)
        abs_dz_bool = (abs(z1-z2) == 1)

        #print(abs_dx_bool, abs_dy_bool, abs_dz_bool)

        if x1==x2 and y1==y2 and abs_dz_bool:
            num_neighbours += 1
        elif x1==x2 and abs_dy_bool and z1==z2:
            num_neighbours += 1
        elif abs_dx_bool and y1==y2 and z1==z2:
            num_neighbours += 1

    return num_neighbours

cubes = []

for line in lines:
    line = line.rstrip('\n')
    line = line.split(',')
    x,y,z = int(line[0]), int(line[1]), int(line[2])
    print(x,y,z)

    cube = Cube((x,y,z))
    cubes.append(cube)

length = len(cubes)

for i in range(length):
    cube = cubes[i]

    num_neighbours = check_neighbours(cube, cubes)
    print(num_neighbours)
    cube.n_exposed_sides -= num_neighbours


#result
total = 0
for cube in cubes:
    total += cube.n_exposed_sides

print("Result: ", total)