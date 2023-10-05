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

class TestPandasDataSeries(unittest.TestCase):

    def test_create_data_frame(self):
        self.assertEqual(
            create_data_frame().to_dict('list'),
            {'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
            )

if __name__ == '__main__':
    create_data_frame_with_index()
    unittest.main()
    
    
    
