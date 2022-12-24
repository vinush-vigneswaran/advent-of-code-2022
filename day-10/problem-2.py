import re

# read file
file = "data.txt"
read_file = open(file, 'r')
lines = read_file.readlines()

pixel_pos = 0
x = 1
crt_display = []


def crt_draw(pixel_pos, x):
    sprite_vals = [x-1, x, x+1]
    if pixel_pos in sprite_vals:
        return "#"
    else:
        return "."

for line in lines:
    line = line.rstrip('\n')

    action = line.split()[0]

    if action == "addx":
        print(pixel_pos, x)
        crt_display.append(crt_draw(pixel_pos, x))
        print(crt_display[-1])
        pixel_pos += 1

        if pixel_pos == 40:
            pixel_pos = 0

        print(pixel_pos, x)
        crt_display.append(crt_draw(pixel_pos, x))
        print(crt_display[-1])
        pixel_pos += 1

        x += int(line.split()[1])

    elif action == "noop":
        print("--", pixel_pos, x)
        crt_display.append(crt_draw(pixel_pos, x))
        pixel_pos += 1
        print("--",crt_display[-1])

    if pixel_pos == 40:
        pixel_pos = 0

    #print(pixel_pos, crt_display)

print("".join(crt_display[0:40]))
print("".join(crt_display[40:80]))
print("".join(crt_display[80:120]))
print("".join(crt_display[120:160]))
print("".join(crt_display[160:200]))
print("".join(crt_display[200:240]))