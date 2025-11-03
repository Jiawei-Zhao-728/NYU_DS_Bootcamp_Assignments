# Pandas Solution for LeetCode 1327: List Products Ordered in a Period

import pandas as pd

Products = pd.DataFrame({
    'product_id': [1, 2, 3, 4, 5],
    'product_name': ['Campus', 'Leetcode', 'Github', 'FuckingAlgo', 'BEAST'],
    'product_category': ['Book', 'Book', 'Book', 'Book', 'Book']
})

Orders = pd.DataFrame({
    'product_id': [1, 1, 2, 2, 3],
    'order_date': pd.to_datetime(['2020-02-05', '2020-02-10', '2020-01-01', '2020-02-11', '2020-02-15']),
    'unit': [60, 70, 30, 80, 10]
})

# Filter for February 2020 orders
feb_orders = Orders[(Orders['order_date'] >= '2020-02-01') & (Orders['order_date'] < '2020-03-01')]
result = feb_orders.merge(Products[['product_id', 'product_name']], on='product_id', how='left')
result = result.groupby(['product_id', 'product_name'])['unit'].sum().reset_index()
result = result[result['unit'] >= 100]
result = result[['product_name', 'unit']]

print(result)

