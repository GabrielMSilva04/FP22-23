import math

# You throw a dart that hits coordinates (x, y) on a dartboard.
# Create a program that gives you the score.
# See:
#   https://en.wikipedia.org/wiki/Darts#Dartboard
#   https://www.dimensions.com/element/dartboard

print("Enter the coordinates in mm from the center of the board.")
x = float(input("x? "))
y = float(input("y? "))

# Points of the sectors, clockwise from the top
# Example: the sector right from the center is POINTS[5] == 6.
POINTS = (20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5)

# COMPLETE...



TAN=y/x
anglePI=math.atan(TAN)
angle=(360*anglePI)/(2*math.pi)

if angle<0:
    angle=angle+360

dist=math.sqrt(x**2+y**2)
print(dist)

if x<0 and y<0:
    angle=angle+180
elif x<0:
    angle=angle-180

print(angle)

if 0<=angle<9 or 351<angle<=360:
    score=POINTS[5]
elif 9<angle<27:
    score=POINTS[4]
elif 27<angle<45:
    score=POINTS[3]
elif 45<angle<63:
    score=POINTS[2]
elif 63<angle<81:
    score=POINTS[1]
elif 81<angle<99:
    score=POINTS[0]
elif 99<angle<117:
    score=POINTS[19]
elif 117<angle<135:
    score=POINTS[18]
elif 135<angle<153:
    score=POINTS[17]
elif 153<angle<171:
    score=POINTS[16]
elif 171<angle<189:
    score=POINTS[15]
elif 189<angle<207:
    score=POINTS[14]
elif 207<angle<225:
    score=POINTS[13]
elif 225<angle<243:
    score=POINTS[12]
elif 243<angle<261:
    score=POINTS[11]
elif 261<angle<279:
    score=POINTS[10]
elif 279<angle<297:
    score=POINTS[9]
elif 297<angle<315:
    score=POINTS[8]
elif 315<angle<333:
    score=POINTS[7]
elif 333<angle<351:
    score=POINTS[9]



if 162<dist<170:
    score=score*2
elif 99<dist<107:
    score=score*3

if dist>170:
    score=0
elif dist<(12.7/2):
    score=50
elif dist<(32/2):
    score=25

print(score)