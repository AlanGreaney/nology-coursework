import os
import csv
import pandas as pd

fileName = "file_challenge.txt"

with open(fileName, encoding="utf-8") as fileObj:
    lineNum = 1
    while True:
        line = fileObj.readline()
        if not line:
            break

        line = line.strip()

        if len(line) == 0:
            print("Line #" + str(lineNum) + " has 0 words.")
        else:
            print("Line #" + str(lineNum) + " has " + str(len(line.split(" "))) + " words: " + line)
        lineNum += 1




for i in range(5):
    print("----")




dataframeUSA = pd.read_csv("unitedStates.csv")

capitals = {}
fileNameCapitals = "stateCapitals.txt"

with open(fileNameCapitals, encoding="utf-8") as fileObj:
    lineNum = 1
    while True:
        line = fileObj.readline()
        if not line:
            break

        line = line.strip().split(" ")
        capitals[line[0]] = line[1]

        lineNum += 1


print(capitals)
for i in range(5):
    print("----")

#.map creates a list
dataframeUSA["Capital"] = dataframeUSA["State"].map(capitals)

dataframeUSA.to_csv("unitedStatesWithCapitals.csv", index = False)

print(dataframeUSA)
for i in range(5):
    print("----")

dataframeUSA.rename(columns=lambda x: x.strip(),inplace=True)
totalPop = 0
for index, row in dataframeUSA.iterrows():
    totalPop += row["Population"]

print("Total Population of these " + str(len(dataframeUSA)) + " states: " + f"{totalPop:,}")
