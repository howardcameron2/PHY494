# now to turn this into a function...
def translate(coordinates, t):
    for n in range(len(coordinates)):
        coordinates[n]=[coordinates[n][0] +t[0],coordinates[n][1] +t[1],coordinates[n][2] +t[2]]

coordinates = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]]
t = [1, 1, 1]
translate(coordinates, t)
print(coordinates)
