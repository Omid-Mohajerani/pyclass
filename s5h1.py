# Omid Mohajearni - Python Class -  Thursdays -  14 to 18
# add 3 lists and print in reversed Decussated 
# Output: https://github.com/Omid-Mohajerani/pyclass/wiki/PYTHON-HOMEWORKS#s5h1-add-3-lists-and-print-in-reversed-decussated
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
newlist = list1[:] + list2[:] + list3[:]
print(newlist[::-2])
