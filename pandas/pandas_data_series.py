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


class TestPandasDataSeries(unittest.TestCase):

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
