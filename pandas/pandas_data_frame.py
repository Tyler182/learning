import pandas as pd
import unittest
import numpy as np

def create_data_frame():
    """Create Pandas Series

    1. Write a Pandas program to create a dataframe
    from a dictionary and display it. 

    Args:
        -
    Returns:
        Pandas Data Frame

    """
    df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
    # print(df)
    return df
    
def create_data_frame_with_index():
    """Write a Pandas program to create and display a DataFrame
    from a specified dictionary data which has the index labels. 

    Args:
        -
    Returns:
        Pandas Data Frame

    """
    df = pd.DataFrame   (  
                            {
                            'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
                            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
                            },
                            index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
                        )
    print(df)
    return df

def sum_inf_data_frame():
    """3. Write a Pandas program to display a summary of the
    basic information about a specified DataFrame and its data. 

    Args:
        -
    Returns:
        Pandas Data Frame

    """
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = pd.DataFrame(exam_data, labels)
    return df.info()
    
def get_3_rows(df):
    """Write a Pandas program to get the first 3 rows
    of a given DataFrame. 

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame - 3 rows
    """
    
    return df.iloc[0:3]    
    
def get_name_and_score(df):
    """
    5. Write a Pandas program to select the 'name' and 'score'
    columns from the following DataFrame.

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame - name and scores columns
    """
    return df.loc[:, ['name', 'score']]
    
def get_columns_and_rows(df, rows, columns):
    """
    6. Write a Pandas program to select the specified
    columns and rows from a given data frame. 

    Args:
        df(Pandas Data Frame) 
        columns (List)
        rows (List)
    Returns:
        Pandas Data Frame with specified columns and rows
    """
    return df.loc[:, columns].iloc[rows]
    
def attempts_greater_2(df):
    """
    7. Write a Pandas program to select the rows where
    the number of attempts in the examination is greater than 2.  

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    return df[df.attempts > 2]

def number_rows_columns(df):
    """
    8. Write a Pandas program to count the number
    of rows and columns of a DataFrame. 

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    return len(df.axes[0]), len(df.axes[1])

def rows_score_nan(df):
    """
    9. Write a Pandas program to select the rows
    where the score is missing, i.e. is NaN. 

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    return df.loc[df['score'].isnull()]      

def score_between_15_20(df):
    """
    10. Write a Pandas program to select the rows
    the score is between 15 and 20 (inclusive). 

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    return df.loc[(df['score'] >= 15) & (df['score'] <= 20)]     

def attemps_less_2_score_greater_15(df):
    """
    11. Write a Pandas program to select the rows where
    number of attempts in the examination is less than 2 
    and score greater than 15.  

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    return df.loc[(df['attempts'] < 2) & (df['score'] > 15)]

def change_score_in_d(df):
    """
    12. Write a Pandas program to change the score 
    in row 'd' to 11.5.

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    df.loc['d', 'score'] = 11.5
    return df

def sum_attempts(df):
    """
    13. Write a Pandas program to calculate the sum
    of the examination attempts by the students. 

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    return df.loc[:, 'attempts'].sum()
    
def mean_score(df):
    """
    14. Write a Pandas program to calculate the mean
    of all students' scores. Data is stored in a dataframe.  

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    return df.loc[:, 'score'].mean()

def append_row(df):
    """
    15. Write a Pandas program to append a new row 'k' to data
    frame with given values for each column.
    Now delete the new row and return the original DataFrame. 
    name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"    

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    df.loc['k'] = ["Suresh", 15.5, 1, "yes"]
    print(df)
    df = df.drop(index=['k'])
    return df
    
def sot_by_name_score(df):
    """
    16. Write a Pandas program to sort the 
    DataFrame first by 'name' in descending order,
    then by 'score' in ascending order.    

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    df = df.sort_values(by=['name', 'score'], ascending = [False, True])
    print(df)
    return df
    
def replace_qualify(df):
    """
    17. Write a Pandas program to replace the 'qualify'
    column contains the values 'yes' and 'no' with
    True and False.     

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    df1 = df.loc[df.qualify == 'yes']
    df1['qualify'] = True
    df2 = df.loc[df.qualify == 'no']
    df2['qualify'] = False
    df = pd.concat([df1, df2])
    print(df)
    return df
    
def james_to_suresh(df):
    """
    18. Write a Pandas program to change the name
    'James' to 'Suresh' in name column of the DataFrame.     

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    df['name'] = df['name'].map({'James': 'Suresh'}).fillna(df['name'])
    return df
    
def delete_attempts(df):
    """
    19. Write a Pandas program to delete the 'attempts'
    column from the DataFrame.     

    Args:
        df(Pandas Data Frame) 
    Returns:
        Pandas Data Frame 
    """
    df = df.drop('attempts', axis = 1)
    return df
    
class TestPandasDataSeries(unittest.TestCase):

    def test_create_data_frame(self):
        self.assertEqual(
            create_data_frame().to_dict('list'),
            {'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
            )
    def test_sum_attempts(self):
        self.assertEqual(sum_attempts(df), 19)

if __name__ == '__main__':
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = pd.DataFrame(exam_data, labels)
    df = delete_attempts(df)
    print(df)
    # unittest.main()
    
    
    
