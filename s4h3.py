# Omid Mohajearni - Python Class -  Thursdays -  14 to 18
# Calculate area or volume of a sphere based on user input
# We are using a fucntion with return value
# Volume of sphere = 4.0/ 3.0 * pi * r**3
# Area of sphere = 4.0 pi * r**2
# pi = 3.1415926535897931

def sphere(userinput,r):
    pi = 3.1415926535897931
    if(userinput.lower() == 'area'):
        area = 4.0 * pi * (r**2)
        return area
    elif(userinput.lower() == 'volume'):
        volume = (4.0/3.0)* pi * (r**3)
        return volume
# Acceptable user values are volume or area
acceptabblevalues = ['volume', 'area']
#Get user input and validate with acceptable values
print("This program will calculate area or volume of sphere based on the user input")
userinput = input("Do you want to calculate Area or Volume ? : ")
if userinput.lower() not in acceptabblevalues:
    print("Acceptable values are Area or Volume")
    exit()
# Get r from user
r = float(input("Pleae enter r value : "))

sphearvariable = sphere(userinput,r)

print(f"{userinput.title()} of sphere with r = {r} :  {sphearvariable}")
