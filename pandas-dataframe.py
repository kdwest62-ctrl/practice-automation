import pandas as pd

celtics = {
    'Player': ['Brown', 'Tatum', 'Pritchard', 'White', 'Hauser'],
    'Position': ['FW', 'FW', 'PG', 'G', 'FW']
}
df = pd.DataFrame(celtics, index=['7', '11', '0', '9', '30'])
print(df)
