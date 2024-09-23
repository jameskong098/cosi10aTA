import math

def calAreaCylinder(r, h):
    surface_area = 2 * math.pi * r * h + 2 * math.pi * r**2
    return round(surface_area, 2)

'''
def calAreaCylinder(r, h):
    surface_area = round(2 * math.pi * r * h + 2 * math.pi * r**2, 2)
    return surface_area
'''

'''
def calAreaCylinder(r, h):
    return round(2 * math.pi * r * h + 2 * math.pi * r**2, 2)
'''

print(calAreaCylinder(4,10))