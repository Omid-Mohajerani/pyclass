# Omid Mohajearni - Python Class -  Thursdays -  14 to 18
# Calculate area and volumme of a cone
# We are using a fucntion with return value
import math

def cone_area(r,h):
    pi = 3.1415926535897931
    area = pi * r * (r + math.sqrt(h**2 + r**2))
    return area


def cone_volume(r,h):
    pi = 3.1415926535897931
    volume = pi * r ** 2 * ( h / 3 )
    return volume

r = 4
h = 5
print(f" Area   of a cone with r = {r} and h = {h} is :  {cone_area(r,h)}")
print(f" Volume of a cone with r = {r} and h = {h} is :  {cone_volume(r,h)}\n")
