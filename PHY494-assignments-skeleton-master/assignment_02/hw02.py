# Homework 2 Cartesian Coordinates

positions = [[0.0, 0.0, 0.0], [1.34234, 1.34234, 0.0], [1.34234, 0.0, 1.34234], [0.0, 1.34234, 1.34234]]

# this is for 2.3 part a
# to access the second particles position all that is need is to ask for a specfic index "positions[1]"
print(positions[1])

# this is for 2.3 part b
# to access a just the y variable of particle 2 remember that "positions[1]" is its own list in a sense.
# to access a specific portion of list positions[1] we simply need to ask for a specific index. In this case "positions[1][1]"
print(positions[1][1])

# without using any modules adding vectors becomes combersome. They'll need to basically be done manually. this is for 2.3 part c
t = [1.34234, -1.34234, -1.34234]
positions = [[positions[0][0]+t[0], positions[0][1]+t[1], positions[0][2]+t[2]], [positions[1][0]+t[0], positions[1][1]+t[1], positions[1][2]+t[2]], [positions[2][0]+t[0], positions[2][1]+t[1], positions[2][2]+t[2]], [positions[3][0]+t[0], positions[3][1]+t[1], positions[3][2]+t[2]]]
print(positions)

# now to turn this into a function... here's the function for 2.3 part d
def translate(coordinates, t):
    for n in range(len(coordinates)):
            coordinates[n]=[coordinates[n][0] +t[0],coordinates[n][1] +t[1],coordinates[n][2] +t[2]]

coordinates = [[0.0, 0.0, 0.0], [1.34234, 1.34234, 0.0], [1.34234, 0.0, 1.34234], [0.0, 1.34234, 1.34234]]
positions2 = [[1.5,-1.5,3],[-1.5,-1.5,-3]]
t2 = [-1.5, 1.5, 3]
translate(coordinates, t)
translate(positions2, t2)
print(coordinates)
print(positions2)



# Problem 2.4
# a.) NumPy array operations differ from linear algebra because it does all operations elementwise. Instead of multiplying row to column, it multiplies exact index to index

import numpy as np
sx = np.array([[0,1],[1,0]])
sy = np.array([[0,-1j],[1j,0]])
sz = np.array([[1,0],[0,-1]])
j=j
print(sx*sy*sz) #when performing this operation, because all elements multiply elementwise, after the calculations all that were left over were zeros
print(np.dot(np.dot(sx,sy),sz)) # performing the operation in this manner performs that actual linear algebra multiplication operation

# now let perform the commutator calculations
commutator = (np.dot(sx,sy)-np.dot(sy,sx))
print("heres the commmutator")
print(commutator)
print("heres the 2jqz")
print(2*j*sz)

# Problem 2.5
positions3 = np.array(\
[[0.0, 0.0, 0.0], [1.34234, 1.34234, 0.0], \
[1.34234, 0.0, 1.34234], [0.0, 1.34234, 1.34234]])
t3 = np.array([1.34234, -1.34234, -1.34234])
