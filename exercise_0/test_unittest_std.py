import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from abcweather import read_dataset, clean_data, train_model, calculate_average, calculate_std_dev

class TestWeatherPredictions(unittest.TestCase):

    def test_standard_deviation(self):
       
        # Test for simple standard deviation
        values = [-1,1]
        result = calculate_std_dev(values)
        self.assertEqual(result, 1)

        # Test for empty list
        values_empty = []
        result_empty = calculate_std_dev(values_empty)
        self.assertIsNone(result_empty)

        # Test for zeros 
        values_zero = [0,0,0]
        result_zero = calculate_std_dev(values_zero)
        self.assertEqual(result_zero, 0)

if __name__ == '__main__':
    unittest.main()

