import pandas as pd

# Sample DataFrame (replace with your actual data)
ActorDirector = pd.DataFrame({
    'actor_id': [1, 1, 1, 1, 1, 2, 2],
    'director_id': [1, 1, 1, 2, 2, 1, 1],
    'timestamp': [0, 1, 2, 3, 4, 5, 6]
})

result = (ActorDirector.groupby(['actor_id', 'director_id'])
           .size()
           .reset_index(name='count')
           .query('count >= 3')
           [['actor_id', 'director_id']])

print(result)

