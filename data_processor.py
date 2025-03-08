"""
Data Processing Module
-----------------------
Handles data cleaning, validation, and transformation.

Author: SymbiantZyB
"""

import pandas as pd

class DataProcessor:
    """
    Provides functionalities for cleaning and transforming datasets.
    """

    def __init__(self):
        """Initialize the data processor."""
        pass

    def clean_data(self, df: pd.DataFrame):
        """
        Cleans the given DataFrame.

        Args:
            df (pd.DataFrame): Input data.

        Returns:
            pd.DataFrame: Cleaned data.
        """
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        return df

# Example Usage
if __name__ == "__main__":
    sample_data = pd.DataFrame({'col1': [1, 2, None, 4], 'col2': ['A', 'B', 'B', None]})
    processor = DataProcessor()
    print(processor.clean_data(sample_data))
