from main4 import main4
import pandas as pd

def test4():
    expected_data = pd.DataFrame({
        'platform': ['PC', 'PC', 'PS4', 'PS4', 'XOne', 'XOne', 'WiiU', 'WiiU'],
        'genre': ['Action', 'Adventure', 'Action', 'Adventure', 'Action', 'Adventure', 'Action', 'Adventure'],
        'count': [5, 3, 4, 2, 6, 1, 2, 1]
    })
    aggregated_data = main4()
    assert 'platform' in aggregated_data.columns, "Column 'platform' is missing."
    assert 'genre' in aggregated_data.columns, "Column 'genre' is missing."
    assert 'count' in aggregated_data.columns, "Column 'count' is missing."
    assert isinstance(aggregated_data, pd.DataFrame), "Result is not a DataFrame."
    assert aggregated_data.shape[0] == expected_data.shape[
        0], "The number of rows in the aggregated data does not match the expected number."
    pd.testing.assert_frame_equal(aggregated_data.reset_index(drop=True), expected_data.reset_index(drop=True),
                                  check_dtype=True)
    print("Aggregation Test: Data has been successfully aggregated.")


if __name__ == "__main__":
    test4()