import math

def calVolCylinder(r, h):
    v = math.pi * r**2 * h
    return round(v, 2)

'''
def calVolCylinder(r, h):
    v = round(math.pi * r**2 * h, 2)
    return v
'''

'''
def calVolCylinder(r, h):
    return round(math.pi * r**2 * h, 2)
'''

print(calVolCylinder(4, 10))