import pandas as pd
from solve_expense_report import *


# tests the normal case, given as ample solution in the task
def test_normal():
    expenses = pd.DataFrame({1721, 979, 366, 299, 675, 1456})
    assert(getNumbersAddingUpToTargetValue(expenses, 2020) == 514579)


# tests what happens, when no two values add up to the target_value
def test_no_matching_values():
    expenses = pd.DataFrame({100, 400, 3000})
    assert(getNumbersAddingUpToTargetValue(expenses, 2020) == -1)


# tests what happens when the expense report is empty
def test_empty_list():
    expenses = pd.DataFrame()
    assert(getNumbersAddingUpToTargetValue(expenses, 2020) == -1)


# tests what happens, when the solution consists of 2020 and 0
def test_zero_and_target_value():
    expenses = pd.DataFrame({2020, 0, 145, 897})
    assert(getNumbersAddingUpToTargetValue(expenses, 2020) == 0)


# execute the tests
test_normal()
test_no_matching_values()
test_empty_list()
test_zero_and_target_value()

print("all tests passed")
