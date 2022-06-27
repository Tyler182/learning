import pandas as pd
import unittest

def create_series():
    """Create Pandas Series

    1. Write a Pandas program to create and display a one-dimensional
    array-like object containing an array of data using Pandas module.

    Args:
        -
    Returns:
        Pandas Series

    """
    ser = pd.Series(['Yana', 'Ivan', 'Alex'], name='Children')
    print(ser)
    return ser


def series_to_list(series):
    """Series to List

    2. Write a Pandas program to convert a Panda module Series to Python
    list and it's type.

    Args:
        series (pandas.Series): Series to be converted.
    Returns:
        List converted from series

    """
    return list(series)


def add_series(series1, series2):
    """Sum of two series

    3. Write a Pandas program to add two Pandas Series.

    Args:
        series1 (pandas.Series): First argument of sum.
        series2 (pandas.Series): Second argument of sum.
    Returns:
        Sum of series1 and series2

    """

    return series1+series2


def subtract_series(series1, series2):
    """Difference of two series

    3. Write a Pandas program to subtract two Pandas Series.

    Args:
        series1 (pandas.Series): First argument of difference.
        series2 (pandas.Series): Second argument of difference.
    Returns:
        Difference series1 and series2

    """

    return series1-series2


def multiple_series(series1, series2):
    """Multiplication of two series

    3. Write a Pandas program to multiple two Pandas Series.

    Args:
        series1 (pandas.Series): First argument of multiplication.
        series2 (pandas.Series): Second argument of multiplication.
    Returns:
        Multiplication of series1 and series2

    """

    return series1*series2


def divide_series(series1, series2):
    """Devision of two series

    3. Write a Pandas program to devide two Pandas Series.

    Args:
        series1 (pandas.Series): First argument of devision.
        series2 (pandas.Series): Second argument of devision.
    Returns:
        Devision of series1 and series2

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
