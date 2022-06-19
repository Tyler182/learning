import pandas as pd

def create_series()->'Pandas Series':
  """
  1. Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module.
  """
  ser = pd.Series(['Yana','Ivan','Alex'], name = 'Children')
  print(ser)
  return ser
  

create_series()
