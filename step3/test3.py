from main3 import main3
import io
import sys

def test3():
    expected_columns = ['name', 'platform', 'genre']
    valid_platforms = ['PS4', 'PC', 'XOne', 'WiiU']
    captured_output = io.StringIO()
    sys.stdout = captured_output
    filtered_data = main3()
    print(filtered_data)
    sys.stdout = sys.__stdout__
    print(captured_output.getvalue())
    for col in expected_columns:
        assert col in filtered_data.columns, f"Column '{col}' is missing in the filtered data."
    unexpected_columns = set(filtered_data.columns) - set(expected_columns)
    assert not unexpected_columns, f"There are unexpected columns in the filtered data: {unexpected_columns}"
    invalid_platforms = filtered_data[~filtered_data['platform'].isin(valid_platforms)]
    assert invalid_platforms.empty, f"There are invalid platforms in the filtered data: {invalid_platforms['platform'].unique()}"
    print("Filter Test: Data has been successfully filtered.")

if __name__ == "__main__":
    test3()