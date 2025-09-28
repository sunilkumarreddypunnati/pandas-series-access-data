'''Task 7: Reverse Series

Problem:
Create a Series s7 from [1, 2, 3, 4] 
with index ['a', 'b', 'c', 'd'].
Print the Series in reverse order using iloc.

Output Format: Series in reverse order

Sample Output:

d    4
c    3
b    2
a    1
dtype: int64'''

import pandas as pd
s7=pd.Series([1, 2, 3, 4],index=['a', 'b', 'c', 'd'])
print(s7.iloc[::-1])