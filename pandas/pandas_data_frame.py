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
    
    return df[0:3]    

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
    print(get_3_rows(df))
    unittest.main()
    
    
    
