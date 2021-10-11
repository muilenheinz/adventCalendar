import pandas as pd

target_value = 2020

# loads the input data file given as "expenses.csv" in this dir
def loadInput():
    expenses = pd.read_csv('expense_report.csv', header=None)
    return expenses

# "Specifically, they need you to find the two entries that sum to target_value and then multiply those two
# numbers together"
# @_expenses: Pandas Data Frame of the expense report
# @_target_value: value the two found numbers should add up to
def getNumbersAddingUpToTargetValue(_expsens, _target_value):
    global target_value

    if _expsens.empty:
        return -1

    for id, expense_row in _expsens.iterrows():
        current_expense = expense_row.loc[0]

        # calc the number which would add up to target value with current_expense
        second_summand = target_value - current_expense
        # print(second_summand , "=", target_value, " - ", current_expense)

        # when the value is negative return an error (-1), since negative expenses are not very likely to happen
        if second_summand < 0:
            return -1

        # search for the second summand in the DataFrame of expenses
        foundValue = _expsens[_expsens.eq(second_summand).any(1)]
        if not foundValue.empty:
            return current_expense * second_summand

    # no result found
    return -1

expenses = loadInput()
result = getNumbersAddingUpToTargetValue(expenses, target_value)

if result == -1:
    print("No value found")
else:
    print ("result is: {0}".format(result))

