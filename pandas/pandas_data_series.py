import pandas as pd
import unittest
import numpy as np

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


def compare_series(series1, series2):
    """Compare elements of two series

    4. Write a Pandas program to compare the elements of the two Pandas Series

    Args:
        series1 (pandas.Series): First series to compare.
        series2 (pandas.Series): Second series to compare.
    Returns:
        Series of boolean, resulting compare elements of two series

    """

    if len(series1) == len(series2):
        return series1 == series2
    else:
        return 'Could not compare because of different length of series'


def convert_dictionary_to_series(dictionary):
    """Convert dictionary to a Pandas series.

    5. Write a Pandas program to convert a dictionary to a Pandas series.

    Args:
        dictionary (dictionary): Dictionary to be converted.
    Returns:
        Pandas series from dictionary

    """

    return pd.Series(dictionary)


def convert_array_to_series(array):
    """6. Write a Pandas program to convert a NumPy array to a Pandas series.

    Args:
        array (numpy array): Array to be converted.
    Returns:
        Pandas series from dicctionary

    """

    return pd.Series(array)


class TestPandasDataSeries(unittest.TestCase):

    def test_convert_array_to_series(self):

        array = np.array([1, 2, 3, 4])
        self.assertEqual(
            list(convert_array_to_series(array)),
            list(pd.Series([1, 2, 3, 4]))
            )

    def test_covert_dictionary_to_series(self):
        """Test - convert dictionary to series
        """

        dictionary = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
        list1 = [100, 200, 300, 400, 800]
        list2 = ['a', 'b', 'c', 'd', 'e']
        self.assertEqual(
            list(convert_dictionary_to_series(dictionary)),
            list1
            )
        self.assertEqual(
            list(convert_dictionary_to_series(dictionary).index),
            list2
            )


    def test_compare_series_equel_length(self):
        """Test - compare 2 series equel length
        """

        series1 = pd.Series([1, 2, 3])
        series2 = pd.Series([2, 2, 'a'])
        self.assertEqual(
            list(compare_series(series1,series2)),
            [False, True, False]
            )


    def test_compare_series_different_length(self):
        """Test - compare 2 series different length
        """

        series1 = pd.Series([1, 2, 3, 4])
        series2 = pd.Series([1, 2, 3])
        self.assertEqual(
            compare_series(series1,series2),
            'Could not compare because of different length of series'
            )


    def test_compare_series_zero_length(self):
        """Test - compare 2 series zero length
        """

        series1 = pd.Series([], dtype='float64')
        series2 = pd.Series([], dtype='float64')
        self.assertEqual(list(compare_series(series1,series2)),[])


    def test_add_series(self):
        """Test add two Pandas Series
        """

        series1 = pd.Series([1, 2, 3])
        series2 = pd.Series([1, 2, 3])
        self.assertEqual(
        list(add_series(series1,series2)), [2, 4, 6])


    def test_subtract_series(self):
        """Test subtract two Pandas Series
        """

        series1 = pd.Series([1, 2, 3])
        series2 = pd.Series([1, 2, 3])
        self.assertEqual(list(subtract_series(series1,series2)), [0, 0, 0])


    def test_multiple_series(self):
        """Test multiple two Pandas Series
        """

        series1 = pd.Series([1, 2, 3])
        series2 = pd.Series([1, 2, 3])
        self.assertEqual(
        list(multiple_series(series1,series2)), [1, 4, 9])


    def test_divide_series(self):
        """Test divide two Pandas Series
        """

        series1 = pd.Series([1, 2, 3])
        series2 = pd.Series([1, 2, 3])
        self.assertEqual(list(divide_series(series1,series2)), [1, 1, 1])


    def test_series_to_list(self):
        """Convert Series to List and compare with right List.
        """

        series = pd.Series(['Yana','Ivan','Alex'], name='Children')
        list_ = ['Yana', 'Ivan', 'Alex']
        self.assertEqual(series_to_list(series), list_)


if __name__ == '__main__':
    unittest.main()
