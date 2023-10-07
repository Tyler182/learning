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
    
class TestPandasDataSeries(unittest.TestCase):

    def test_create_data_frame(self):
        self.assertEqual(
            create_data_frame().to_dict('list'),
            {'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
            )

if __name__ == '__main__':
    exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                 'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                 'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                 'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = pd.DataFrame(exam_data, labels)
    print(score_between_15_20(df))
    unittest.main()
    
    
    
