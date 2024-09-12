from datetime import datetime
import unittest
 
def calculate_time_differences(reference_time_str, clock_times_str):
    """
    Calculating the time differences in minutes between a reference time and a list of clock times.
 
    Args:
        reference_time_str (str): The reference time in the format "HH:MM".
        clock_times_str (list of str): A list of clock times in the format "HH:MM".
 
    Returns:
        list of int: A list of time differences in minutes. If an error occurs, an empty list is returned.
    """
    try:
        # Initialize the reference time
        reference_time = datetime.strptime(reference_time_str, "%H:%M")
 
        # Initialize the array of clock times
        clock_times = [datetime.strptime(time, "%H:%M") for time in clock_times_str]
 
        # Calculate the time differences in minutes
        time_differences = [(clock_time - reference_time).total_seconds() / 60 for clock_time in clock_times]
 
        # Convert to integers
        time_differences = [int(diff) for diff in time_differences]
 
        return time_differences
 
    except ValueError as e:
        print(f"Error parsing time: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
 
class TestTimeDifferences(unittest.TestCase):
    """
    Unit tests for the calculate_time_differences function.
    """
 
    def test_calculate_time_differences(self):
        """
        Test the calculate_time_differences function with valid input.
        """
        reference_time_str = "15:00"
        clock_times_str = ["14:45", "15:05", "15:00", "14:40"]
        expected = [-15, 5, 0, -20]
        result = calculate_time_differences(reference_time_str, clock_times_str)
        self.assertEqual(result, expected)
 
    def test_invalid_time_format(self):
        """
        Test the calculate_time_differences function with an invalid time format.
        """
        reference_time_str = "15:00"
        clock_times_str = ["14:45", "invalid_time", "15:00", "14:40"]
        result = calculate_time_differences(reference_time_str, clock_times_str)
        self.assertEqual(result, [])
 
    def test_empty_clock_times(self):
        """
        Test the calculate_time_differences function with an empty list of clock times.
        """
        reference_time_str = "15:00"
        clock_times_str = []
        expected = []
        result = calculate_time_differences(reference_time_str, clock_times_str)
        self.assertEqual(result, expected)
 
if __name__ == "__main__":
    # Example usage of the function
    reference_time_str = "15:00"
    clock_times_str = ["14:45", "15:05", "15:00", "14:40", "geyani"]
    time_differences = calculate_time_differences(reference_time_str, clock_times_str)
    print("Time differences:", time_differences)
 
    # Print whether each clock is behind, ahead, or synchronized
    for i, diff in enumerate(time_differences):
        clock_number = i + 1
        if diff < 0:
            print(f"Clock-{clock_number} is behind by {-diff} minutes.")
        elif diff > 0:
            print(f"Clock-{clock_number} is ahead by {diff} minutes.")
        else:
            print(f"Clock-{clock_number} is synchronized with the grand clock.")
 
    # Run the unit tests
    unittest.main(argv=[''], exit=False)