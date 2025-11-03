# Pandas Solution for LeetCode 185: Department Top Three Salaries

import pandas as pd

Employee = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max', 'Janet', 'Randy'],
    'salary': [70000, 90000, 80000, 60000, 90000, 69000, 85000],
    'departmentId': [1, 1, 2, 2, 1, 1, 1]
})

Department = pd.DataFrame({
    'id': [1, 2],
    'name': ['IT', 'Sales']
})

# Merge Employee and Department
merged = Employee.merge(Department, left_on='departmentId', right_on='id', how='left')
# Calculate dense rank within each department
merged['rank'] = merged.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
# Filter for top 3 ranks
result = merged[merged['rank'] <= 3]
# Select and rename columns
result = result[['name_y', 'name_x', 'salary']]
result.columns = ['Department', 'Employee', 'Salary']
print(result)

