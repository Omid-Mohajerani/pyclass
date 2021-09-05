# Omid Mohajearni - Python Class -  Thursdays -  14 to 18
# Calculate area of a sphere
# We are using a fucntion with return value
# Area of sphere = 4.0 pi * r**2
# pi = 3.1415926535897931
# Output : https://github.com/Omid-Mohajerani/pyclass/wiki/PYTHON-HOMEWORKS#s4h2--calculate-area-of-a-sphere-using-function-with-return-value


def sphere_area(r):
    pi = 3.1415926535897931
    area = 4.0 * pi * (r**2)
    return area

r= 6.0
print(f"Area of sphere with r = {r} :  {sphere_area(r)}")
