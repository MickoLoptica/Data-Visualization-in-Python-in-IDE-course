from main2 import main2
import io
import sys


def test2():
    try:
        captured_output = io.StringIO()
        sys.stdout = captured_output
        data = main2()
        sys.stdout = sys.__stdout__
        assert not data.empty, "Load Test: The data is empty."
        output = captured_output.getvalue()
        lines = output.splitlines()
        print(data.head(10))
        assert len(lines) == 13, "Print Test: Expected 10 data rows plus the header row."
        print("Load Test: Data has been successfully loaded and displayed.")
    except FileNotFoundError:
        print("Load Test: The file was not found.")
    except Exception as e:
        print(f"Load Test: An error occurred - {e}")

if __name__ == "__main__":
    test2()