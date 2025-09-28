'''Task 3: Slicing Series

Problem:
Create a Series s3 from [10, 20, 30, 40, 50] 
with index labels ['p', 'q', 'r', 's', 't'].
Print a slice from 'q' to 's' using index labels.
Print the first three elements using integer slicing.

Output Format: Series slice

Sample Output:
# Slice by index labels
q    20
r    30
s    40
dtype: int64

# Slice by integer positions
0    10
1    20
2    30
dtype: int64'''

import pandas as pd
s3=pd.Series([10, 20, 30, 40, 50],index=['p', 'q', 'r', 's', 't'])
print("Slice by index labels:\n",s3['q':'s'])
print("Slice by integer positions:\n",s3[:3])