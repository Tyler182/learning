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
        Pandas Series

    """
    df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
    print(df)
    return df

class TestPandasDataSeries(unittest.TestCase):

    def test_create_data_frame(self):
        self.assertEqual(
            create_data_frame().to_dict('list'),
            {'X':[78,85,96,80,86],'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
            )

if __name__ == '__main__':
    unittest.main()
