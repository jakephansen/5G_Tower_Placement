import math
tower_coordinates = {}
x = 0
with open("tower_locations_coordinates.txt") as f:
    for line in f:
        line = line.split(',')
        line[1] = line[1][:-1]
        line[0] = float(line[0])
        line[1] = float(line[1])
        tower_coordinates[x] = line
        x += 1

x = 0
names_to_coordinates = {}
with open("intersect_points_names.txt") as f:
    for line in f:
        line = line.split(',')
        line[0] = float(line[0])
        line[1] = float(line[1])
        line[2] = line[2][:-1]
        name = line[2]

        names_to_coordinates[x] = line
    
        x += 1

found1 = 0
error = 0
found2 = 0
part1 = ""
part2 = ""
long_string = ""
count = 0
for tower in tower_coordinates:

    found1 = 0
    found2 = 0
    x = tower_coordinates[tower][0]

    y = tower_coordinates[tower][1]


    for name in names_to_coordinates:
        count += 1
        x2 = names_to_coordinates[name][0]
        y2 = names_to_coordinates[name][1]



        if((abs(x - x2) <= 0.05) and (abs(y - y2 <= 0.05) )):
            if(found1 == 0):
                part1 = names_to_coordinates[name][2]
                found1 = 1
            elif (part1 != names_to_coordinates[name][2]):
                part2 = names_to_coordinates[name][2]
                found2 = 1
    if(found1 == 1 and found2 == 1):
        temp_line = part1 + ", " + part2 + "\n"
        long_string += temp_line
    elif(found1 == 1 and found2 == 0):
        temp_line = part1 + ", " + part1 + "\n"
        long_string += temp_line
    else:
        error += 1

with open("answers.txt", "w+") as f:
    f.write(long_string)

print("error ", error )
