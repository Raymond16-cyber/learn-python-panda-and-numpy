import numpy as np
import pandas as pd

# You can create a dataframe from:

#-----------------------------  1) an array------------------------------------------/

# OPTION 1

# /-----Step 1----/
#-----create an array with numpy
np_arr_data = np.array([[1,4], [2,5], [3,6]])
# /-----Step 2----/
# creating a dataframe with pandas
first_dataframe = pd.DataFrame(np_arr_data, index=['row1','row2','row3'],columns=['col1', 'col2'])
print(first_dataframe)

# OPTION 2

#-----------------------------  2) a dictionary------------------------------------------/

