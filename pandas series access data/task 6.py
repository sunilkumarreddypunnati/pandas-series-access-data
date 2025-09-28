'''Task 6: Conditional Access

Problem:
Create a Series s6 from [100, 150, 200, 250, 300].
Print all elements greater than 200.

Output Format: Series slice

Sample Output:

3    250
4    300
dtype: int64'''

import pandas as pd
s6=pd.Series([100, 150, 200, 250, 300])
print(s6[s6>200])