import pandas as pd

p1 = input("First: ")
p2 = input("Second: ")
p3 = input("Third: ")
drivers = [p1, p2, p3]
podium = pd.Series(drivers, index=['P1', 'P2', 'P3'])
print(podium)
