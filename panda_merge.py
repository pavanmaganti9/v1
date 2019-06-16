import pandas as pd

xl = pd.read_excel('store.xls', index_col="Order ID")

cs = pd.read_csv('nba.csv')

df1 = xl[['Customer Name','City']]

df1.head(100)

df2 = cs[['City','Salary']]

df2.head(100)

# Return only the rows in which the left table have matching keys in the right table
print pd.merge(df1, df2, on='City', how='inner')

# Returns all rows from both tables, join records from the left which have matching keys in the right table
print pd.merge(df1, df2, on='City', how='outer')

# Return all rows from the left table, and any rows with matching keys from the right table
print pd.merge(df1, df2, on='City', how='left')

# Return all rows from the right table, and any rows with matching keys from the left table
print pd.merge(df1, df2, on='City', how='right')