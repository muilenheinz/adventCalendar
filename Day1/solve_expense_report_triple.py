from solve_expense_report import *
import pandas as pd

# searches for three values from _expenses, which add up to target_value
# @_expenses: Pandas Data Frame of the expense report
# @_target_value: value the two found numbers should add up to
# @return: product of three numbers found in expenses, which add up to _target_value
def solveExpenseReportTriple(_expenses, _target_value):
    # if the list has only two elements, return an error
    if _expenses.size < 3:
        return -1

    # loop over the DataFrame, subtract each current value from the target value and call the algorithm from part
    # one of the task to calculate the potential rest
    for id, expense_row in _expenses.iterrows():
        current_expense = expense_row.loc[0]
        target_value_new = _target_value - current_expense

        # remove current_expense from inputs, since it should not be multiplied with itself
        new_expenses = _expenses.drop(id, axis=0)
        res = getNumbersAddingUpToTargetValue(new_expenses, target_value_new)

        if res != -1:
            return current_expense * res

    # nothing found
    return -1

expenses = loadInput()
result = solveExpenseReportTriple(expenses, target_value)

if result == -1:
    print("No result found for three values")
else:
    print ("result for multiplication of three values, which add up to {0} is: {1}".format(target_value, result))

