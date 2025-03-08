"""
This script demonstrates loading configuration from a file.
"""

# Import necessary modules
import json

# Configuration loader class
class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = {}

    def load_config(self):
        """Loads configuration from a JSON file."""
        with open(self.config_file, 'r') as file:
            self.config = json.load(file)

    def get_config(self, key, default=None):
        """Retrieves a configuration value by key."""
        return self.config.get(key, default)

# Main function
if __name__ == "__main__":
    # Create a config loader and load configuration
    config_loader = ConfigLoader('config.json')
    config_loader.load_config()

    # Retrieve a configuration value
    config_value = config_loader.get_config('example_key', 'default_value')
    print(f"Configuration value for 'example_key': {config_value}")
