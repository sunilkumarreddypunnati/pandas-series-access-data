'''Task 1: Access by Index Label

Problem:
Create a Series s1 from [100, 200, 300, 400] 
with index labels ['a', 'b', 'c', 'd'].
Print the value corresponding to index 'c'.

Input Format: None (Series is predefined)
Output Format: Integer value

Sample Output:

300
'''

import pandas as pd
s1=pd.Series([100, 200, 300, 400],index=['a', 'b', 'c', 'd'])
print(s1)
print(s1['c'])