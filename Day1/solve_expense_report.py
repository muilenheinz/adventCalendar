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
def getNumbersAddingUpToTargetValue(_expenses, _target_value):
    if _expenses.size < 3:
        return -1

    for id, expense_row in _expenses.iterrows():
        current_expense = expense_row.loc[0]

        # calc the number which would add up to target_value with current_expense
        second_summand = _target_value - current_expense

        if second_summand > -1:
            # search for the second summand in the DataFrame of expenses
            foundValue = _expenses[_expenses.eq(second_summand).any(1)]
            if not foundValue.empty:
                # only the first solution is returned, if there are others they are simply ignored
                return current_expense * second_summand

    # no result found
    return -1

expenses = loadInput()
result = getNumbersAddingUpToTargetValue(expenses, target_value)

if result == -1:
    print("No result found for two values")
else:
    print ("result for multiplication of two values, which add up to {0} is: {1}".format(target_value, result))

