import pandas as pd

big_four = {'Drivers': ['Russell', 'Antonelli',
                        'Leclerc', 'Hamilton',
                        'Norris', 'Piastri',
                        'Verstappen', 'Hadjar'],
            'Teams': ['Mercedes', 'Mercedes',
                      'Ferrari', 'Ferrari',
                      'McLaren', 'McLaren',
                      'Red Bull', 'Red Bull']}
df = pd.DataFrame(big_four, index=['63', '12', '16', '44', '1', '81', '3', '6'])
print(df)
