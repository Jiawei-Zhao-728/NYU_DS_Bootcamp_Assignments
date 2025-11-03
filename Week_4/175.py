# Pandas Solution for LeetCode 175: Combine Two Tables

import pandas as pd

# Sample DataFrames
Person = pd.DataFrame({
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
})

Address = pd.DataFrame({
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
})


result = Person.merge(Address[['personId', 'city', 'state']], 
                      on='personId', 
                      how='left')


result = result[['firstName', 'lastName', 'city', 'state']]

print(result)

