
# Omid Mohajearni - Python Class 14 to 18
# Calculate volume of a sphere
# We are using a fucntion with return value
# Volume of sphere = 4.0/ 3.0 * pi * r**3
# pi = 3.1415926535897931


def sphere_volume(r):
    pi = 3.1415926535897931
    volume = (4.0/3.0)* pi * (r**3)
    return volume

r= 6.0
print(f"Volume of sphere with r = {r} :  {sphere_volume(r)}")
