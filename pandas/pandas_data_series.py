import pandas as pd
import unittest

def create_series()->'Pandas Series':
    """
    1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
    """
    ser = pd.Series(['Yana', 'Ivan', 'Alex'], name='Children')
    print(ser)
    return ser


def series_to_list(series: 'Pandas Series') -> 'List':
    """
    2. Write a Pandas program to convert a Panda module Series to Python list and it's type.
    """
    return list(series)

def add_series(
    series1:'Pandas Series',
    series2:'Pandas Series'
    ) -> 'List of Pandas Series':
    """
    3. Write a Pandas program to add two Pandas Series.
    """
    return series1+series2

def subtract_series(
    series1:'Pandas Series',
    series2:'Pandas Series'
    ) -> 'List of Pandas Series':
    """
    3. Write a Pandas program to subtract two Pandas Series.
    """
    return series1-series2

def multiple_series(
    series1:'Pandas Series',
    series2:'Pandas Series'
    ) -> 'List of Pandas Series':
    """
    3. Write a Pandas program to multiple two Pandas Series.
    """
    return series1*series2

def divide_series(
    series1:'Pandas Series',
    series2:'Pandas Series'
    ) -> 'List of Pandas Series':
    """
    3. Write a Pandas program to divide two Pandas Series.
    """
    return series1/series2

class TestPandasDataSeries(unittest.TestCase):
    def test_add_series(self):
        """
        Test add two Pandas Series
        """
        series1 = pd.Series([1, 2, 3])
        series2 = pd.Series([1, 2, 3])
        self.assertEqual(
        list(add_series(series1,series2)), [2, 4, 6])


    def test_subtract_series(self):
        """
        Test subtract two Pandas Series
        """
        series1 = pd.Series([1,2,3])
        series2 = pd.Series([1,2,3])
        self.assertEqual(list(subtract_series(series1,series2)), [0, 0, 0])

    def test_multiple_series(self):
        """
        Test multiple two Pandas Series
        """
        series1 = pd.Series([1,2,3])
        series2 = pd.Series([1,2,3])
        self.assertEqual(
        list(multiple_series(series1,series2)), [1, 4, 9])

    def test_divide_series(self):
        """
        Test divide two Pandas Series
        """
        series1 = pd.Series([1,2,3])
        series2 = pd.Series([1,2,3])
        self.assertEqual(list(divide_series(series1,series2)), [1, 1, 1])


    def test_series_to_list(self):
        """
        Convert Series to List and compare with right List.
        """
        series = pd.Series(['Yana','Ivan','Alex'], name='Children')
        list_ = ['Yana','Ivan','Alex']
        self.assertEqual(series_to_list(series), list_)


if __name__ == '__main__':
    unittest.main()
