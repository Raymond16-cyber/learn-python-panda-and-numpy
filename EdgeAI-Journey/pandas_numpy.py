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
# print(first_dataframe)



#-----------------------------  2) a dictionary------------------------------------------/
# /-----Step 1----/
states = ['California', 'Texas', 'Chicago', 'New York']
population = [37265874,72819436, 63879190, 43526178]
# /-----Step 2----/
# Store the lists with a dictionary
dicts_states = { 'States': states, 'Population': population }
# /-----Step 3----/
# creating the dataframe
df_population = pd.DataFrame(dicts_states, index=['1','2','3','4'])
# print(df_population)

#-----------------------------  3) a csv file------------------------------------------/
csv_data = pd.read_csv('EdgeAI-Journey/data/students.csv')
# showing first 5 rows of the csv_data dataframe
# print(csv_data.head())
# showing last 5 rows of the csv_data dataframe
# print(csv_data.tail())
# showing last n rows of the csv_data dataframe
# print(csv_data.head(6))   # it recives an arguement to show the first n rows, which is 6 here
# print(csv_data.tail(6))   # it recives an arguement to show the last n rows, which is 10 here

# Getting access to the shape attribute
csv_data_shape = csv_data.shape   # This gives us the number of rows followed by number of columns
# print(csv_data_shape)




#-----------------------------ATTRIBUTES, METHODS & FUNCTIONS------------------------------------------/
# (1)-------ATTRIBUTES--------/
# Getting Access To The Index Attribute
csv_data_index = csv_data.index
# print(csv_data_index)    # This logs the start index and end index, with the step being how they increasse: RangeIndex(start=0, stop=10, step=1)

# Getting Access To The Column Attribute
csv_data_columns = csv_data.columns
# print(csv_data_columns)    # This logs the column names in the data.

# Getting Access To The Data Types Of Each Column
csv_data_column_types = csv_data.dtypes
# print(csv_data_column_types)   # This logs the columns and their data types at the side


# (2)-------METHODS--------/
# Showing first five columns
# print(csv_data.head()) 

# Showing the dataframe info
# print(csv_data.info())   # This shows the index, total columns, the data, the column types count, and memory usage. Basicaly ing=fo concerning the DataFrame

# Showing/Describing basic statistics of the DataFrame like mean,max, min, e.t.c.
# print(csv_data.describe())



# (3)-------FUNCTIONS--------/
#  These funtions are basically Pyhton functions used in pandas:

# Getting the length of the functions, the row length to be precise
# print(len(csv_data))

# Obtainig the higher index of the DF
# print(max(csv_data.index))

# Obtainig the lowest index of the DF
# print(min(csv_data.index))

# Obtainig the data type of the DF
# print(type(csv_data))



#-----------------------------GETTING ACCESS TO A COLUMN/COLUMNS IN A DATAFRAME------------------------------------------/
#------Using the '[]', this is the prefered way-----
# print(csv_data['python_score'])
#------Using the '.', this has pitfalls, as white spaces will fail(Not Recommended)----
# print(csv_data.age)

# Selecting more than a column
# print(csv_data[['python_score', 'math_score', 'age']])
# NOTE TO REMEMBER: we can't select more than 2 columns with the '.'
