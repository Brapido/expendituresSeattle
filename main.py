import csv


class Info:
    name: str
    total: int

    # Constructor
    def __init__(self, name, amount):
        self.name = name
        self.total = amount



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

totalDictionary = {}
for item in getInfo:
    # print(item.name + " payed: " + item.total)
    if item.name in totalDictionary:
        x = totalDictionary[item.name]
        total = x + item.total
        totalDictionary[item.name] = total
    else:
        totalDictionary[item.name] = item.total

# print(totalDictionary)
sorted_Dictionary = dict(sorted(totalDictionary.items()))
print("{:15} {:>15}".format("Department", "Total Spent"))
print("_______________________________")
for items in sorted_Dictionary:
    # print(items + "\t\t\t\t\t", sorted_Dictionary[items])
    print("{:15}${:>15,.2f}".format(items, sorted_Dictionary[items]))
