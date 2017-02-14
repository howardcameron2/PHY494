# Largest number that can be made by a certain number of bits


def bits(n):
    sumx = 0
    for n in range (n+1):
        x = 2**n
        sumx = sumx + x
    return sumx

print(bits(8))
