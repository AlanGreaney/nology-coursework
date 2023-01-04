import os
import csv

os.mkdir("deletedRightAway")

os.rmdir("deletedRightAway")

#https://docs.python.org/3/library/os.path.html
#https://docs.python.org/3/library/os.html#mkdir-modebits



fileName = "fileWorking1.txt"

#with open(fileName, mode="w", encoding="utf-8") as fileObj:
    #for i in range(10):
        #fileObj.write("A number is: " + str(i) + "\n")

with open(fileName, encoding="utf-8") as fileObj:
    lineNum = 1
    while True:
        line = fileObj.readline()
        if not line:
            break
        print("Line #" + str(lineNum) + " | ", line, end="")
        lineNum += 1

"""
rows = []
with open("employers.csv", newline='') as csvFile:
    csvReader = csv.reader(csvFile)
    headers = next(csvreader)
    for row in csvreader:
        rows.append(row)

print("The headers are: " + headers)
print(rows)
"""

import pandas as pd

exampleDictionary = {"name": ["Rich", "Ash", "Ben", "Steph"], 
                    "age": [35, 26, 37, 26],
                    "designation:": ["US Head", "Lead Coach", "Instructor", "A.Instructor"]}

dataframe = pd.DataFrame(exampleDictionary)

print(exampleDictionary)
print(dataframe)

#https://docs.python.org/3/library/csv.html
dataframe.to_csv("fileWorking2.csv", index = False)


dataframeRead = pd.read_csv("fileWorking2.csv")
print(dataframeRead)



#json
data = {
    'col1': [10, 20, 30],
    'col2': ["a", "b", "c"]
}

print(data)

dataframeJson = pd.DataFrame(data)

print(dataframeJson.to_json())

dataframeJson.to_json("fileWorking3.json")

dataframeJsonRead = pd.read_json("fileWorking3.json")
print(dataframeJsonRead)