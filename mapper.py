import math

all_coordinates = {}
x = 0
print("reading in file" + "\n")
with open("no_repeats.txt") as f:
    for line in f:

        line = line.split(",")
        line[1] = line[1][:-1]
        line[0] = float(line[0])
        line[1] = float(line[1])
        line[0] = int(line[0])
        line[1] = int(line[1])
        all_coordinates[x] = line
        x += 1

tower_locations = []
covered_locations = []
check_back_later = []
min_distances = {}
tower_locations.append(0)
covered_locations.append(0)


print("starting round 1")
for point in all_coordinates:
    min_dist = 100000
    for tower in tower_locations:
        x2 = all_coordinates[tower][0]
        y2 = all_coordinates[tower][1]
        x1 = all_coordinates[point][0]
        y1 = all_coordinates[point][1]

        distance = math.hypot(x2-x1, y2-y1)
        if(distance <= 1500):
            if(point not in covered_locations):
                covered_locations.append(point)
            break

        else:
            if(distance < min_dist):
                min_dist = distance
    if(min_dist >= 3000):
        if(point not in covered_locations):
            covered_locations.append(point)
            tower_locations.append(point)
    else:
        if(point not in check_back_later):
            check_back_later.append(point)
            min_distances[point] = min_dist

print ("done with first round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)

print("starting round 2")
for point in check_back_later:
    min_distance = 100000
    for tower in tower_locations:
        x2 = all_coordinates[tower][0]
        y2 = all_coordinates[tower][1]
        x1 = all_coordinates[point][0]
        y1 = all_coordinates[point][1]

        distance = math.hypot(x2-x1, y2-y1)
        if(distance <= 1500):
            if(point not in covered_locations):
                covered_locations.append(point)
            break
        elif(distance < min_distance):
            min_distance = distance
    min_distances[point] = min_distance
print("done with second round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)

print("starting round 3")
for point in all_coordinates:
    if(point not in covered_locations):
        if(min_distances[point] >= 2250):
            covered_locations.append(point)
            tower_locations.append(point)
print("done with third round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)

print("starting round 4")
for point in all_coordinates:
    min_distance = 100000
    if(point not in covered_locations):
        for tower in tower_locations:
            x2 = all_coordinates[tower][0]
            y2 = all_coordinates[tower][1]
            x1 = all_coordinates[point][0]
            y1 = all_coordinates[point][1]

            distance = math.hypot(x2-x1, y2-y1)
            if(distance <= 1500):
                covered_locations.append(point)
                break
            elif(distance < min_distance):
                min_distance = distance
        min_distances[point] = min_distance

print ("done with fourth round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)

print("starting round 5")
for point in all_coordinates:
    if(point not in covered_locations):
        if(min_distances[point] >= 2000):
            covered_locations.append(point)
            tower_locations.append(point)
for point in all_coordinates:
    min_distance = 10000
    if(point not in covered_locations):
        for tower in tower_locations:
            x2 = all_coordinates[tower][0]
            y2 = all_coordinates[tower][1]
            x1 = all_coordinates[point][0]
            y1 = all_coordinates[point][1]

            distance = math.hypot(x2-x1, y2-y1)
            if(distance <= 1500):
                covered_locations.append(point)
                break
            elif(distance < min_distance):
                min_distance = distance
        min_distances[point] = min_distance

print ("done with fifth round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)

print("starting round 6")
for point in all_coordinates:
    if(point not in covered_locations):
        if(min_distances[point] >= 1800):
            covered_locations.append(point)
            tower_locations.append(point)
for point in all_coordinates:
    min_distance = 10000
    if(point not in covered_locations):
        for tower in tower_locations:
            x2 = all_coordinates[tower][0]
            y2 = all_coordinates[tower][1]
            x1 = all_coordinates[point][0]
            y1 = all_coordinates[point][1]

            distance = math.hypot(x2-x1, y2-y1)
            if(distance <= 1500):
                covered_locations.append(point)
                break
            elif(distance < min_distance):
                min_distance = distance
        min_distances[point] = min_distance

print ("done with 6th round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)

print("starting round 7")
for point in all_coordinates:
    if(point not in covered_locations):
        if(min_distances[point] >= 1700):
            covered_locations.append(point)
            tower_locations.append(point)
for point in all_coordinates:
    min_distance = 10000
    if(point not in covered_locations):
        for tower in tower_locations:
            x2 = all_coordinates[tower][0]
            y2 = all_coordinates[tower][1]
            x1 = all_coordinates[point][0]
            y1 = all_coordinates[point][1]

            distance = math.hypot(x2-x1, y2-y1)
            if(distance <= 1500):
                covered_locations.append(point)
                break
            elif(distance < min_distance):
                min_distance = distance
        min_distances[point] = min_distance

print ("done with 7th round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)

print("starting round 8")
for point in all_coordinates:
    if(point not in covered_locations):
        if(min_distances[point] >= 1600):
            covered_locations.append(point)
            tower_locations.append(point)
for point in all_coordinates:
    min_distance = 10000
    if(point not in covered_locations):
        for tower in tower_locations:
            x2 = all_coordinates[tower][0]
            y2 = all_coordinates[tower][1]
            x1 = all_coordinates[point][0]
            y1 = all_coordinates[point][1]

            distance = math.hypot(x2-x1, y2-y1)
            if(distance <= 1500):
                covered_locations.append(point)
                break
            elif(distance < min_distance):
                min_distance = distance
        min_distances[point] = min_distance

print ("done with 8th round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)

print("starting Final Round")
for point in all_coordinates:
    if(point not in covered_locations):
        if(min_distances[point] >= 1550):
            covered_locations.append(point)
            tower_locations.append(point)
for point in all_coordinates:
    min_distance = 10000
    if(point not in covered_locations):
        for tower in tower_locations:
            x2 = all_coordinates[tower][0]
            y2 = all_coordinates[tower][1]
            x1 = all_coordinates[point][0]
            y1 = all_coordinates[point][1]

            distance = math.hypot(x2-x1, y2-y1)
            if(distance <= 1500):
                covered_locations.append(point)
                break
            elif(distance < min_distance):
                min_distance = distance
        min_distances[point] = min_distance

print ("done with 9th round")

i = 0
for point in tower_locations:
    i += 1
print ("tower locations, ", i)
i = 0
for point in covered_locations:
    i += 1
print ("covered locations ", i)
numerator = i
i = 0
for point in all_coordinates:
    i += 1
print ("all coordinates, ", i)
denominator = i
percent = float(numerator)/ float(denominator)
print("percentage of covered locations, ", percent)


total_covered = 0
for point in all_coordinates:
    x = all_coordinates[point][0]
    y = all_coordinates[point][1]
    for tower in tower_locations:
        tower_x = all_coordinates[tower][0]
        tower_y = all_coordinates[tower][1]
        dist = math.hypot(tower_x - x, tower_y - y)
        if(dist <= 1500):
            total_covered += 1

average_towers = float( total_covered/denominator)
print ("Average number of towers per point, ", average_towers)
print("printing data")
x = 0
with open("no_repeats.txt") as f:
    for line in f:
        line = line.split(",")
        line[1] = line[1][:-1]
        line[0] = float(line[0])
        line[1] = float(line[1])
        all_coordinates[x] = line
        x += 1
line = ""

for tower in tower_locations:
    x = all_coordinates[tower][0]
    y = all_coordinates[tower][1]
    line += str(x) + ',' + str(y) + '\n'
with open("tower_locations_coordinates.txt", "w+") as f:
    f.write(line)


names_intersections = {}
with open("intersect_points_names.txt") as f:
    for line in f:
        line = line.split(",")
        line[2] = line[2][:-1]
        line[0] = float(line[0])
        line[1] = float(line[1])
        names_intersections[line[2]] = line

output_lines = ""
temp1 = ""
temp2 = ""
found1 = 0
found2 = 0
for tower in tower_locations:
    found1 = 0
    found2 = 0
    for intersect in names_intersections:
        if(all_coordinates[tower][0] == names_intersections[intersect][0] and all_coordinates[tower][1] == names_intersections[intersect][1]):
            if(found1 == 0):
                temp1 = intersect
                found1 = 1
            else:
                if(temp1 != intersect):
                    found2 = 1
                    temp2 = intersect
    if(found1 == 1 and found2 == 1):
        output_lines += temp1 + ", " + temp2 + "\n"

with open("finished_list_intersections.txt", "w+") as f:
    f.write(output_lines)

print ("Completed.")
