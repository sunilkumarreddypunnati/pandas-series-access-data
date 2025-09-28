'''Task 5: Access Multiple Elements

Problem:
Create a Series s5 from [10, 20, 30, 40]
with index ['m', 'n', 'o', 'p'].
Access indexes 'm' and 'o' using loc.
Access the first, third, and fourth elements using iloc.

Output Format: Series slices

Sample Output:

# Using loc
m    10
o    30
dtype: int64

# Using iloc
0    10
2    30
3    40
dtype: int64'''

import pandas as pd
s5=pd.Series([10, 20, 30, 40],index=['m', 'n', 'o', 'p'])
print(s5.loc[['m','o']])
print(s5.iloc[[0,2,3]])