#
# Problem 4
#
from ps4b import nestEggVariable
from ps4c import postRetirement

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # TODO: Your code here.
    savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    low = 0
    high = savings
    expenses = (low + high) / 2.0
    ctr = 1
    while abs(postRetirement(savings, postRetireGrowthRates, expenses)[-1]) > epsilon and ctr < 100:
        print("ctr:", ctr, "expenses :", expenses, "accounts:", postRetirement(savings, postRetireGrowthRates, expenses)[-1])
        if postRetirement(savings, postRetireGrowthRates, expenses)[-1] < 0:
            high = expenses
        else:
            low = expenses
        ctr += 1
        expenses = (low + high) / 2.0
    return expenses
    
    
def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.
    
testFindMaxExpenses()