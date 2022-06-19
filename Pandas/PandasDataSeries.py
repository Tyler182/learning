import pandas as pd
import unittest

def create_series()->'Pandas Series':
  """
  1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
  """
  ser = pd.Series(['Yana','Ivan','Alex'], name = 'Children')
  print(ser)
  return ser
  

def series_to_list(series:'Pandas Series')->'List':
  """
  2. Write a Pandas program to convert a Panda module Series to Python list and it's type.
  """
  return list(series)


class TestPandasDataSeries(unittest.TestCase):
  def test_series_to_list(self):
    """
    Convert Series to List and compare with right List.
    """
    series = pd.Series(['Yana','Ivan','Alex'], name = 'Children')
    _list = ['Yana','Ivan','Alex']
    self.assertEqual(series_to_list(series), _list)


if __name__=='__main__':
  unittest.main()

