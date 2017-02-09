# now to turn this into a function...
def translate(coordinates, t):
    for n in range(len(coordinates)):
        #coordinates[n] = coordinates[n] + t
        for i in range(len(t)):
            coordinates[n] = coordinates[n][i] + t[i]

coordinates = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3]]
t = [1, 1, 1]
translate(coordinates, t)
print(coordinates)
