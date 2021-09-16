# Omid Mohajearni - Python Class -  Thursdays -  14 to 18
# Ask a list of fruits from the User and show the number of unique fruits. Enter "End" to finish accepting new values
# Output: https://github.com/Omid-Mohajerani/pyclass/wiki/PYTHON-HOMEWORKS#s5h23-ask-a-list-of-fruits-from-the-user-and-show-the-number-of-unique-fruits

firstfruit = input("Enter name of a fruit: ")
fruits = []
fruits.append(firstfruit.title())
condition = "True"
while condition == "True":
    nextfruite = input("Enter name of another fruite or enter 'End' to finish: ")
    if nextfruite.title() == "End":
        condition = "False"
        break
    fruits.append(nextfruite.title())
    print(f"All fruits:    {fruits}")
    uniquefruits = set(fruits)
    print(f"Unique fruits: {uniquefruits}")
print(f"You have entered {len(fruits)} fruits that {len(uniquefruits)} are unique")
