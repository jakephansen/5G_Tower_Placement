Written by Jake Hansen, February 2019

This project takes in GIS data for cities and outputs locations
for placement of 5G towers in order to maximize coverage at minimized cost

Requirements:
1. Newest version of Python 3.6- Python 3.5 and below and python 3.7 and above
will not work
2. QGIS desktop
answer files are included, if you want to just see the answer skip to step 6


Step 1:
Download city shapefile (needs at least .shp and .dbf files) data for
specific city/area, in this example Dallas and launch in QGIS

Step 2:
Click on
"Vector" -> "Analysis Tools" -> "Line Intersection" and create temporary layer

Step 3:
Fixing the pathway for your system, run

layer = iface.activeLayer()
output_file = open('/Users/jacobhansen/Documents/5GPlacement/intersect_points_names.txt', 'w+')
x = 0
line = ''
for f in layer.getFeatures():
    x += 1
    if(x % 10000 == 0):
        print (x)
    geom = f.geometry()
    temp_line = '%f,%f' %(geom.asPoint().x(), geom.asPoint().y())
    line += temp_line + '\n'

output_file.write(line)""

in the python plugin within QGIS
Repeat with this

layer = iface.activeLayer()
output_file = open('/Users/jacobhansen/Documents/5GPlacement/intersect_points_names.txt', 'w+')
x = 0
line = ''
for f in layer.getFeatures():
    x += 1
    if(x % 10000 == 0):
        print (x)
    geom = f.geometry()
    temp_line = '%f,%f' %(geom.asPoint().x(), geom.asPoint().y())
    temp_line += ',' + f['name']
    line += temp_line + '\n'
    line += temp_line + '\n'

output_file.write(line)

Step 4:
Run
python -c "import sys; lines = sys.stdin.readlines(); print ''.join(sorted(set(lines)))" < InputFile > OutputFile

to clean the data from step 3 (intersect_points.txt) to eliminate repeats (no_repeats.txt)

Step 5:
run
python mapper.py

from command line making sure input file is result of step 4, in this example no_repeats.txt

Step 6:
run
python intersect_namer.py

To see graphical locations of towers,
Using the created CSV-tower-location.txt, in QGIS click
layer -> add layer -> Add deliminated text layer
