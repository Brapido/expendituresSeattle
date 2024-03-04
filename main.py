# Take a CSV file and gather running total for each department on actual monies spent.
import csv


# class object for info
class Info:
    name: str
    total: int

    # Constructor
    def __init__(self, name, amount):
        self.name = name
        self.total = amount


# open CSV fil and write needed information into a list object.
with open("city-of-seattle-2012-expenditures-dollars.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")

    getInfo = []
    row_number = 1
    for x in reader:
        if row_number != 1:
            info = Info(x[0], int(float(x[3])))
            getInfo.append(info)
            row_number += 1
        else:
            row_number += 1

# initialize a dictionary
totalDictionary = {}
# iterate through list to add to dictionary while updating total for each department
for item in getInfo:
    if item.name in totalDictionary:
        x = totalDictionary[item.name]
        total = x + item.total
        totalDictionary[item.name] = total
    else:
        totalDictionary[item.name] = item.total

# sort new dictionary for better look
sorted_Dictionary = dict(sorted(totalDictionary.items()))

# print dictionary with string format for easier read
print("{:15} {:>15}".format("Department", "Total Spent"))
print("_______________________________")
for items in sorted_Dictionary:
    print("{:15}${:>15,.2f}".format(items, sorted_Dictionary[items]))
