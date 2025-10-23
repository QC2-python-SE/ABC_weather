import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from abcweather import read_dataset, clean_data, train_model, calculate_average, calculate_std_dev

def test_calculate_standard_deviation():
    # Test to calculate simple standard deviation
    values = [-1,1]
    result = calculate_std_dev(values)
    assert result == 1

    # Test for empty list
    empty_values = []
    result_empty = calculate_std_dev(empty_values)
    assert result_empty is None

    # Test for zero values
    zero_values = [0,0,0]
    result_zero = calculate_std_dev(zero_values)
    assert result_zero == 0