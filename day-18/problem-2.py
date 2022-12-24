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

def check_neighbours_list(coord, other_coords):
    x1, y1, z1 = coord

    num_neighbours = 0

    for other_coord in other_coords:
        x2, y2, z2 = other_coord

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

def update_exposed_sides(cubes):
    for i in range(len(cubes)):
        cube = cubes[i]

        num_neighbours = check_neighbours(cube, cubes)
        cube.n_exposed_sides -= num_neighbours

def get_surface_area(cubes):
    total = 0
    for cube in cubes:
        total += cube.n_exposed_sides
    return total

cubes = []
air_cubes = []
x_max = 0
y_max = 0
z_max = 0
coords = {
    'cubes': [],
    'enclosed': [],
}

for line in lines:
    line = line.rstrip('\n')
    line = line.split(',')
    x,y,z = int(line[0]), int(line[1]), int(line[2])
    #print(x,y,z)

    if x > x_max:
        x_max = x
    if y > y_max:
        y_max = y
    if z > z_max:
        z_max = z

    cube = Cube((x,y,z))
    cubes.append(cube)
    coords['cubes'].append((x,y,z))

length = len(cubes)

def is_enclosed(coord, cube_coord_list):
    x1, y1, z1 = coord

    f1, f2, f3, f4, f5, f6 = False, False, False, False, False, False

    for other_coord in cube_coord_list:
        x2, y2, z2 = other_coord

        if x1==x2 and y1==y2 and z1 > z2:
            f1 = True
        elif x1==x2 and y1==y2 and z1 < z2:
            f2 = True
        elif x1==x2 and y1 > y2 and z1 == z2:
            f3 = True
        elif x1==x2 and y1 < y2 and z1 == z2:
            f4 = True
        elif x1 > x2 and y1==y2 and z1 == z2:
            f5 = True
        elif x1 < x2 and y1==y2 and z1 == z2:
            f6 = True

    # print("n_blocked_sides", n_blocked_sides)
    return f1 and f2 and f3 and f4 and f5 and f6


# print(is_enclosed((2,2,5), coords['cubes']))

#check map if enclosed
for x in range(x_max):
    for y in range(y_max):
        for z in range(z_max):
            curr_coord = (x, y, z)

            if (curr_coord not in coords['cubes']) and is_enclosed(curr_coord, coords['cubes']):
                coords['enclosed'].append(curr_coord)

# check for cavity
for coord in coords['enclosed']:

    rocks_and_enclosed_list = coords['cubes'] + coords['enclosed']

    if check_neighbours_list(coord, rocks_and_enclosed_list) == 6:
        air_cube = Cube(coord)
        air_cubes.append(air_cube)

# find number of exposed sides
update_exposed_sides(cubes)
update_exposed_sides(air_cubes)

# result
print(get_surface_area(cubes))
print(get_surface_area(air_cubes))
total = get_surface_area(cubes) - get_surface_area(air_cubes)
print(total)





