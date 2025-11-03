# Pandas Solution for LeetCode 1075: Project Employees I

import pandas as pd

Project = pd.DataFrame({
    'project_id': [1, 1, 1, 2, 2],
    'employee_id': [1, 2, 3, 1, 4]
})

Employee = pd.DataFrame({
    'employee_id': [1, 2, 3, 4],
    'name': ['Khaled', 'Ali', 'John', 'Doe'],
    'experience_years': [3, 2, 1, 2]
})

result = Project.merge(Employee[['employee_id', 'experience_years']], on='employee_id', how='left')
result = result.groupby('project_id')['experience_years'].mean().reset_index()
result.rename(columns={'experience_years': 'average_years'}, inplace=True)
result['average_years'] = result['average_years'].round(2)

print(result)

