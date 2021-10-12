import csv

# loads the input data file given as "password_db.csv" in this dir
def loadInput():

    with open('boardingPasses.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


# recursively calcs the row or col of a seat given the string, consisting of "F"(ront) and "B"(ack) for
# row and "L"(eft) or "R"(ight) for cols. F and L mean the seat is situated in the upper half of range, B and R it
# is in the lower half
# @_range: list of [min, max], in which the seat is situated
# @_seatString: String describing the position of the seat
# @_upper_half_letter: char describing which half of the given interval is the one the seat is situated in
def calcSeat(_range, _seatString, _upper_half_letter):

    remainingString = _seatString[1:len(_seatString)]
    whichHalf = _seatString[0]

    if len(remainingString) > 0:
        newInterval = (_range[1] - _range[0] + 1) / 2

        if whichHalf == _upper_half_letter:
            newRange = [_range[0], _range[0] + newInterval - 1]
        else:
            newRange = [_range[0] + newInterval, _range[1]]

        return calcSeat(newRange, remainingString, _upper_half_letter)
    else:
        if whichHalf == _upper_half_letter:
            return _range[0]
        else:
            return _range[1]

# given the string describing the place of the seat it calcs the position and based on that the id of the seat
# @_seatString: String describing the position of the seat
def calcSeatID(_seatString):
    rowString = _seatString[0:7]
    colString = _seatString[-3:]
    row = calcSeat([0, 127], rowString, "F")
    col = calcSeat([0, 7], colString, "L")

    seatId = row * 8 + col
    # print("_seatString", _seatString, "row", row, "column", col, "seatId", seatId, "rowString", _seatString[0:1], "colString", colString)
    return int(seatId)

# iterate through all given boarding passes
# @_boardingPasses: 2-dimensional list of boarding passes in the form: [['FBBBFFFRLL'], ['FBBFBFBRRL'], ['FBFFFFFRRL']]
def getHighestSeatId(_boardingPasses):
    maxSeatId = 0

    for boardingpass in _boardingPasses:
        seatId = calcSeatID(boardingpass[0])
        if seatId > maxSeatId:
            maxSeatId = seatId

    return maxSeatId

boardingPasses = loadInput()
res = getHighestSeatId(boardingPasses)
print("Highest SeatId is", res)