import pandas as pd
import re
from operator import xor

# loads the input data file given as "password_db.csv" in this dir
def loadInput():
    passwords = pd.read_csv('password_db.csv', header=None, delimiter=":")
    return passwords

# returns the number of correct passwords according to the rules defined in the first col of the _passwordDB
# interpreting them as given in task 1
# @passwordDB: pandas DataFrame, first col with rules applicant for that password, second with the password
# @return: number of correct passwords in the given list
def checkPasswordsTask1(_passwordDB):
    validPasswords = 0

    for id, entry in _passwordDB.iterrows():
        rule = entry.iloc[0]
        password = entry.iloc[1]

        # extract the rule
        rule_parts = re.split( '-| ', rule)
        min_letters = rule_parts[0]
        max_letters = rule_parts[1]
        letter = rule_parts[2]

        # apply rule to the password
        letter_occurs_times = password.count(letter)
        if int(min_letters) <= letter_occurs_times <= int(max_letters):
            validPasswords += 1

    return validPasswords

# returns the number of correct passwords according to the rules defined in the first col of the _passwordDB
# interpreting them as given in task 2
# @passwordDB: pandas DataFrame, first col with rules applicant for that password, second with the password
# @return: number of correct passwords in the given list
def checkPasswordsTask2(_passwordDB):
    validPasswords = 0

    for id, entry in _passwordDB.iterrows():
        rule = entry.iloc[0]
        password = entry.iloc[1]
        validPasswords += checkSinglePassword(password, rule)

    return validPasswords

# given a rule and a passwords checks it according to rule interpretation given in task 2 (see README)
# @password as a String
# @rule as a String
# @return: number of correct passwords (0 or 1)
def checkSinglePassword(password, rule):
    # extract the rule
    rule_parts = re.split( '-| ', rule)
    letter = rule_parts[2]

    first_index = int(rule_parts[0])
    if first_index <= len(password):
        letter_at_first_index = password[first_index]
        correct_letter_at_first_index = (letter_at_first_index == letter)
    else:
        return 0

    second_index = int(rule_parts[1])
    if second_index <= len(password):
        letter_at_second_index = password[second_index]
        correct_letter_at_second_index = (letter_at_second_index == letter)
    else:
        return 0

    # apply rule to the password
    if xor(correct_letter_at_first_index, correct_letter_at_second_index):
        return 1

    return 0

passwordDB = loadInput()
res = checkPasswordsTask2(passwordDB)
print(res, "passwords are correct")
