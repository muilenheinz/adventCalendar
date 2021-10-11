import pandas as pd
import re

# loads the input data file given as "password_db.csv" in this dir
def loadInput():
    passwords = pd.read_csv('password_db.csv', header=None, delimiter=":")
    print(passwords)
    return passwords

# returns the number of correct passwords according to the rules defined in the first col of the _passwordDB
# @passwordDB: pandas DataFrame, first col with rules applicant for that password, second with the password
# @return: number of correct passwords in the given list
def checkPasswords(_passwordDB):
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

passwordDB = loadInput()
res = checkPasswords(passwordDB)
print(res, "passwords are correct")