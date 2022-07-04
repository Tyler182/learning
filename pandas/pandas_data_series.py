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


def change_series_type_to_str(series):
    """7. Write a Pandas program to change the data type of given
    a column or a Series.

    Args:
        series (Pandas Series): Series to be changed data type
    Returns:
        Pandas Series with changed data type

    """

    return series.astype(str, errors='ignore')

def first_column_to_series(dataframe):
    """8. Write a Pandas program to convert the first column of
    a DataFrame as a Series.

    Args:
        dataframe (Pandas DataFrame)
    Returns:
        Pandas Series which is the first column of dataframe

    """
    if len(dataframe.columns) >= 1:
        return dataframe.iloc[:,0]
    else:
        return pd.Series([], dtype='float64')


def convert_series_to_array(series):
    """9. Write a Pandas program to convert a given Series to an array.

    Args:
        series (Pandas Series)
    Returns:
        NumPy Array

    """
    return(np.array(series))


def convert_series_of_lists_to_series(series):
    """10. Write a Pandas program to convert Series of lists to one Series.

    Args:
        series (Pandas Series) - Series of lists
    Returns:
        Series

    """

    s = []
    for iter, item in series.iteritems():
        s += item
    return(pd.Series(s))


def sort_series(series):
    """Sort series ascending.

    11. Write a Pandas program to sort a given Series.

    Args:
        series (Pandas Series) - Series to be sorted
    Returns:
        Pandas Series which is sorted of series

    """

    return series.sort_values(ascending=True)


class TestPandasDataSeries(unittest.TestCase):

    def test_sort_series(self):

        series1 = pd.Series([3, 2, 1])
        series2 = pd.Series([1, 2, 3])
        self.assertEqual(
            list(sort_series(series1)),
            list(series2)
            )


    def test_convert_series_of_lists_to_series(self):

        series1 = pd.Series([['Red', 'Green', 'White'],
            ['Red', 'Black'],
            ['Yellow']])
        series2 = pd.Series(['Red', 'Green', 'White',
            'Red', 'Black', 'Yellow'])
        self.assertEqual(
            list(convert_series_of_lists_to_series(series1)),
            list(series2)
            )


    def test_convert_series_to_array(self):

        series = pd.Series(['Ivan', 'Alex'])
        array = np.array(['Ivan', 'Alex'])
        self.assertEqual(
            list(convert_series_to_array(series)),
            list(array)
            )


    def test_convert_series_to_array(self):

        series = pd.Series(['Ivan', 'Alex'])
        array = np.array(['Ivan', 'Alex'])
        self.assertEqual(
            list(convert_series_to_array(series)),
            list(array)
            )


    def test_first_column_to_series(self):

        dataframe = pd.DataFrame({'Employer':['Ivan', 'Alex'], 'Age':[20, 25]})
        series = pd.Series(['Ivan', 'Alex'])
        self.assertEqual(
            list(first_column_to_series(dataframe)),
            list(series)
            )


    def test_first_column_to_series_empty_dataframe(self):
        """Test with empty dataframe
        """
        dataframe = pd.DataFrame({})
        series = pd.Series([], dtype='float64')
        self.assertEqual(
            list(first_column_to_series(dataframe)),
            list(series)
            )


    def test_change_series_type_to_int(self):

        series = pd.Series([1, 2.3, 3.3])
        self.assertEqual(
            change_series_type_to_str(series).dtypes,
            'object'
            )


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
