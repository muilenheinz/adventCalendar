import csv
import pandas as pd
import re

# loads the input data file given as "passwords.csv" in this dir
def loadInput():

    with open('passports.txt') as f:
        passports = f.read()
        passports = passports.split("\n\n")

        return passports

# given the chaotic input from the txt file it sorts the fields into a DataFrame with all possible cols
# @return pandas DataFrame of the ordered passports
def sortPassports(_passports_raw):
    passports_ordered = pd.DataFrame({}, columns = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

    for passport_raw in _passports_raw:
        # get single fields from passport
        passport_tuples = re.split( '\n| ', passport_raw)
        entry = dict(string.split(':') for string in passport_tuples)
        passports_ordered = passports_ordered.append(entry, ignore_index=True)

    return passports_ordered

# loop over all passports and check each one for validity
# @passports: DataFrame of the (ordered) passports
def countValidPassports(passports):
    valid_passports = 0

    for id, passport in passports.iterrows():
        if validatePassport(passport):
            valid_passports += 1

    return valid_passports

# given a single passport check if it is valid or not
# @passport: single-row DataFrame
# @return Boolean of validity of given passport
def validatePassport(passport):
    # if all fields are given, the passport is valid
    countOfNaNFields = passport.isnull().sum()
    if countOfNaNFields == 0:
        return True

    # when only the cid field is missing, the passport is also valid
    cidIsNull = passport.isnull()["cid"]
    if countOfNaNFields == 1 and cidIsNull:
        return True

    return False

passports_raw = loadInput()
passports = sortPassports(passports_raw)
result = countValidPassports(passports)

print(result, "passports are valid")

