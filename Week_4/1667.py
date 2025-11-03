
import pandas as pd

Users = pd.DataFrame({
    'user_id': [1, 2],
    'name': ['alice', 'boB']
})

result = Users.copy()
result['name'] = result['name'].str.capitalize()

# Sort by user_id
result = result.sort_values('user_id')

print(result)

