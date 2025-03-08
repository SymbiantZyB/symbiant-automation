"""
This script contains utility functions for automation tasks.
"""

# Import necessary modules
import os

# Utility function to check if a file exists
def file_exists(filepath):
    """Checks if a file exists at the given filepath."""
    return os.path.exists(filepath)

# Utility function to create a directory
def create_directory(directory_path):
    """Creates a directory if it does not exist."""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

# Main function for testing utility functions
if __name__ == "__main__":
    # Test file_exists function
    test_file = "test.txt"
    print(f"Does {test_file} exist? {file_exists(test_file)}")

    # Test create_directory function
    test_directory = "test_dir"
    create_directory(test_directory)
    print(f"Directory {test_directory} created.")
