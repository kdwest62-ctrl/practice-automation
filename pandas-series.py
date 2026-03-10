import pandas as pd

drivers = ['Russell', 'Antonelli', 'Leclerc']
podium = pd.Series(drivers, index=['P1', 'P2', 'P3'])
print(podium)
