import pandas as pd

starters = {
    'Player': ['White', 'Brown', 'Hauser', 'Tatum', 'Queta'],
    'Position': ['PG', 'SG', 'SF', 'PF', 'C']
}
df = pd.DataFrame(starters, index=['9', '7', '30', '0', '88'])
print(df)

bench = {
    'Player': ['Pritchard', 'Scheierman', 'Walsh', 'Gonzalez', 'Garza', 'Vucevic'],
    'Position': ['G', 'G', 'G', 'G', 'C', 'C']
}
df_bench = pd.DataFrame(bench, index=['11', '55', '27', '28', '52', '4'])
two_way = pd.DataFrame([{'Player': 'Harper Jr.', 'Position': 'G/F'},
                         {'Player': 'Shulga', 'Position': 'G'},
                         {'Player': 'Tonje', 'Position': 'G'},
                         {'Player': 'Williams','Position': 'F/C'}], index=['13', '44', '8', '77'])
df_bench = pd.concat([df_bench, two_way])
print(df_bench)
