import math

def calcArea(r):
    return math.pi * r**2

def calcVol(area, h):
    return area * h

r = int(input("Type integer number for radius:"))
h = int(input("Type integer number for height:"))
area = calcArea(r)
volume = round(calcVol(area, h), 2)

print(f"The volume for a cylinder with radius {r} and height {h} is {volume}") 