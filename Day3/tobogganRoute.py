import pandas as pd
import csv

landscape_input = None
landscape = None

# loads the input data file given as "password_db.csv" in this dir
def loadInput():
    global landscape_input, landscape

    with open('landscape.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    landscape_input = data
    landscape = data

def findTobogganPath():
    global landscape

    # start at the top left corner of the input (row, col)
    position = [0, 0]
    treesHit = 0

    while position[0] < len(landscape) - 1:
        # calculate the next position
        position[0] += 1
        position[1] += 3

        treesHit += getIsTreeAtPosition(position)
    print(treesHit, "trees hit")


# returns whether or not there is a tree at the given position
# @position list as [row, col]
def getIsTreeAtPosition(_position):
    global landscape

    # the input is given as a pattern, which is said to repeat endlessly.
    # Therefore, when the (col-)index runs out of the landscape array, append a new repetition of the original data
    if _position[1] > len(landscape[_position[0]][0]) - 1:
        landscape = repeatLandscape()

    # get the item located at the relevant position
    row = landscape[_position[0]][0]
    target = row[_position[1]]

    if target == "#":
        return 1
    else:
        return 0

# given the current landscape it extends it for one further part, since
# the landscape is said to repeat endlessly
# @return list of lists representing the new landscape
def repeatLandscape():
    global landscape_input, landscape

    # join landscape input to each existing row
    res = list(sub1 + sub2 for sub1, sub2 in zip(landscape_input, landscape))

    # concat the old and new landscape strings in each sublist
    return list(map(lambda list: ["".join(list)], res))

loadInput()
findTobogganPath()
