# Pandas Solution for LeetCode 176: Second Highest Salary

import pandas as pd

Employee = pd.DataFrame({
    'id': [1, 2, 3],
    'salary': [100, 200, 300]
})

# Get distinct salaries, sorted in descending order
distinct_salaries = Employee['salary'].unique()
sorted_salaries = pd.Series(distinct_salaries).sort_values(ascending=False)

# Get the second highest salary (index 1), or None if it doesn't exist
if len(sorted_salaries) >= 2:
    second_highest = sorted_salaries.iloc[1]
else:
    second_highest = None

# Create result DataFrame with the correct column name
result = pd.DataFrame({'SecondHighestSalary': [second_highest]})

print(result)

