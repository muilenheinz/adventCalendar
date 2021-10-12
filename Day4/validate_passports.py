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
# @strict: for task 2 there are stricter regulations, which can be switched on with this option
def countValidPassports(passports, _strict = False):
    valid_passports = 0

    for id, passport in passports.iterrows():
        if validatePassport(passport, _strict):
            valid_passports += 1

    return valid_passports

# given a single passport check if it is valid or not
# @passport: single-row DataFrame
# @strict: also checks for the stricter policies given in task 2
# @return Boolean of validity of given passport
def validatePassport(passport, strict = False):
    if strict:
        # byr: four digits; at least 1920 and at most 2002
        birthyear = passport["byr"]
        if not (str(birthyear).isdigit() and int(birthyear) >= 1920 and int(birthyear) <= 2002):
            return False

        # iyr: four digits; at least 2010 and at most 2020
        issueYear = passport["iyr"]
        if not (str(issueYear).isdigit() and int(issueYear) >= 2010 and int(issueYear) <= 2020):
            return False

        # eyr: four digits; at least 2020 and at most 2030
        expirationYear = passport["eyr"]
        if not (str(expirationYear).isdigit() and int(expirationYear) >= 2020 and int(expirationYear) <= 2030):
            return False

        # hgt a number followed by either cm or in:
        #     If cm, the number must be at least 150 and at most 193.
        #     If in, the number must be at least 59 and at most 76.
        height = str(passport["hgt"])
        unit = height[-2:]
        value = height[:len(height)-2]
        if not (value.isnumeric() and \
            ((unit == "cm" and int(value) >= 150 and int(value) <= 193) or
             (unit == "in" and int(value) >= 59 and int(value) <= 76))):
            return False

        # exactly one of: amb blu brn gry grn hzl oth
        eyeColor = str(passport["ecl"])
        possibleOptions = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        # list.index does not return -1 on not found, but an exception, so build the index function here
        index = possibleOptions.index(eyeColor) if eyeColor in possibleOptions else -1

        if index == -1:
            return False

        # hcl: a # followed by exactly six characters 0-9 or a-f (interpreting "or" as color can contain all of the
        # listed chars, not as xor)
        haircolor = str(passport["hcl"])
        if not(haircolor is not None and len(haircolor) == 7 and re.search("#[a-f0-9]{6}", haircolor)):
            return False

        # pid: a nine-digit number, including leading zeroes
        passportID = str(passport["pid"])
        if not(len(passportID) == 9 and re.search("[0-9]{9}", passportID)):
            return False

    # if all fields are given, the passport is valid
    countOfNaNFields = passport.isnull().sum()
    if countOfNaNFields == 0:
        return True

    # when only the cid field is missing, the passport is also valid
    cidIsNull = passport.isnull()["cid"]
    if countOfNaNFields == 1 and cidIsNull:
        return True

    return False

# task 1
passports_raw = loadInput()
passports = sortPassports(passports_raw)
result = countValidPassports(passports, False)
print(result, "passports are valid according to task1 regulations")

# task2
result = countValidPassports(passports, True)
print(result, "passports are valid according to task2 regulations")


