'''Task 4: Access Using loc and iloc

Problem:
Create a Series s4 from [2, 4, 6, 8] 
with index ['x', 'y', 'z', 'w'].

Print the value at index 'w' using loc.
Print the last element using iloc.

Output Format: Integer values

Sample Output:
8
8'''

import pandas as pd
s4=pd.Series([2, 4, 6, 8],index=['x', 'y', 'z', 'w'])
print(s4.loc['w'])
print(s4.iloc[-1])