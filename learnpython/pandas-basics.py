# Pandas is a high-level data manipulation tool. Built in the Numpy package and it key
# data structure is colled the DataFrame. DataFrames allow you to store and manipulate
# tabular data in rows of observations and columns of variables.

# One way to create a DataFrame is to use a dictionary.

dict = {"country": ["Brazil", "Russia", "India", "China", "South Afraica"],
	"capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
	"area": [8.516, 17.10, 3.286, 9.597, 1.221],
	"population": [200.4, 143.5, 1252, 1357, 52.98]
}

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)
