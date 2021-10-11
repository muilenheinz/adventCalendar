import pandas as pd
from solve_expense_report_triple import *

# tests the normal case, given as sample solution in the task
def test_normal():
    expenses = pd.DataFrame({1721, 979, 366, 299, 675, 1456})
    assert(solveExpenseReportTriple(expenses, 2020) == 241861950)


# tests what happens, when no two values add up to the target_value
def test_no_matching_values():
    expenses = pd.DataFrame({100, 400, 3000})
    assert(solveExpenseReportTriple(expenses, 2020) == -1)


# tests what happens when the expense report is empty
def test_empty_list():
    expenses = pd.DataFrame()
    assert(solveExpenseReportTriple(expenses, 2020) == -1)


# tests what happens, when the solution consists of 2020 and two zeros
def test_zero_and_target_value():
    expenses = pd.DataFrame({2020, 0, 0, 145, 897})
    assert(solveExpenseReportTriple(expenses, 2020) == 0)

# test what happens, when the list has only two elements
def test_list_only_two_elements():
    expenses = pd.DataFrame({548, 0})
    assert(solveExpenseReportTriple(expenses, 2020) == -1)


# execute the tests
test_normal()
test_no_matching_values()
test_empty_list()
test_zero_and_target_value()
test_list_only_two_elements()

print("all tests passed")
