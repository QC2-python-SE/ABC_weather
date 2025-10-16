import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from abcweather import read_dataset, clean_data, train_model, calculate_average, calculate_median, calculate_range, calculate_variance

@pytest.fixture
def mock_data():
    """
    Creates a mock dataset for testing.
    """
    data = {
        'temperature': np.random.uniform(15, 35, 100),
        'humidity': np.random.uniform(40, 90, 100),
        'wind_speed': np.random.uniform(0, 20, 100),
        'precipitation': np.random.randint(0, 2, 100)
    }
    df = pd.DataFrame(data)
    return df

def test_read_dataset(mock_data, tmpdir):
    # Save the DataFrame to a temporary CSV file
    temp_file = tmpdir.join("test_weather_data.csv")
    mock_data.to_csv(temp_file, index=False)

    # Read the dataset
    result = read_dataset(temp_file)
    
    assert isinstance(result, pd.DataFrame)
    assert result.shape == mock_data.shape  # Check if the dimensions match

def test_clean_data(mock_data):
    # Test the data cleaning process
    cleaned_df = clean_data(mock_data, ['temperature', 'humidity', 'wind_speed'], 'precipitation')
    
    assert 'temperature' in cleaned_df.columns
    assert 'humidity' in cleaned_df.columns
    assert cleaned_df.isnull().sum().sum() == 0  # Ensure no NaN values
    assert cleaned_df.duplicated().sum() == 0  # Ensure no duplicates

def test_train_model(mock_data):
    # Clean data before training
    cleaned_df = clean_data(mock_data, ['temperature', 'humidity', 'wind_speed'], 'precipitation')
    
    # Train the model
    model, features, target = train_model(cleaned_df)
    
    assert isinstance(model, RandomForestRegressor)  # Check if the model is a RandomForestRegressor
    assert len(features) > 0  # Ensure features were returned
    assert (cleaned_df.iloc[:, -1].values == target.values).all()  # Ensure target matches the last column

def test_calculate_average():
    # Test calculate_average function
    values = [1, 2, 3, 4, 5]
    result = calculate_average(values)
    assert result == 3.0

    # Test for empty input
    empty_values = []
    result_empty = calculate_average(empty_values)
    assert result_empty is None

def test_calculate_variance():
    # Test variance calculation
    values = [1, 2, 3, 4, 5]
    result = calculate_variance(values)
    assert result == 2

    # Test for single value input
    single_value = [5]
    result_single = calculate_variance(single_value)
    assert result_single == 0

    # Test mixed variables (integers and floats)
    mixed_values = [1, 2.5, 3, 4.5, 5]
    result_mixed = calculate_variance(mixed_values)
    assert np.isclose(result_mixed, 2.06)


    # Test for empty input
    empty_values = []
    result_empty = calculate_variance(empty_values)
    assert result_empty is None

    # Test for non-numeric input
    values = ["😁","😁","😁","😁"]
    with pytest.raises(TypeError):
        result = calculate_variance(values)

    # Test for string input
    values = "😁😁😁😁"
    with pytest.raises(TypeError):
        result = calculate_variance(values)
    
    # Test for mixed type input
    values = [1,2,3,4,5,"😁"]
    with pytest.raises(TypeError):
        result = calculate_variance(values)
def test_median():
    # Test median calculation
    values = [1, 3, 3, 6, 7, 8, 9]
    result = calculate_median(values)
    assert result == 6, "Median calculation is incorrect"

    # Test for even number of elements
    even_values = [1, 2, 3, 4]
    result_even = calculate_median(even_values)
    assert result_even == 2.5, "Median calculation for even number of elements is incorrect"

    # test for empty list
    empty_values = []
    result_empty = calculate_median(empty_values) if empty_values else None
    assert result_empty is None, "Median of empty list should be None"

    # test for negative values
    negative_values = [-5, -1, -3, -4, -2, 1, 21, 5]
    result_negative = calculate_median(negative_values)
    assert result_negative == -2, "Median calculation for negative values is incorrect"

    # test functions with float values
    float_values = [1.5e7, 2.5e-2, 3.5e4, 4.5e0, 5.5e-16]
    result_float = calculate_median(float_values)
    assert result_float == 4.5, "Median calculation for float values is incorrect"

def test_range():
    assert calculate_range([2, 3]) == 1
    assert calculate_range([3, 2]) == 1
    with pytest.raises(Exception) as e_info:
        result = calculate_range()
    assert calculate_range([]) == None
    with pytest.raises(Exception) as e_info:
        result = calculate_range(["x","y"])
