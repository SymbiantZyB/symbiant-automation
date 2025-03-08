import os
import json
import yaml

class ConfigLoader:
    """Loads configuration settings for the application."""

    def __init__(self, config_file=None):
        """Initialize the config loader."""
        self.config_file = config_file
        self.config = {}

    def load_env_config(self):
        """Loads configuration from environment variables."""
        self.config.update(os.environ)

    def load_file_config(self):
        """Loads configuration from a JSON or YAML file."""
        if self.config_file:
            with open(self.config_file, 'r') as file:
                if self.config_file.endswith('.json'):
                    self.config.update(json.load(file))
                elif self.config_file.endswith('.yaml') or self.config_file.endswith('.yml'):
                    self.config.update(yaml.safe_load(file))

    def load_config(self):
        """Loads configuration from all sources."""
        self.load_env_config()
        self.load_file_config()

    def get_config(self, key, default=None):
        """Retrieves a configuration value by key."""
        return self.config.get(key, default)

# Main function
if __name__ == "__main__":
    # Create a config loader and load configuration
    config_loader = ConfigLoader('config.yaml')
    config_loader.load_config()

    # Retrieve a configuration value
    config_value = config_loader.get_config('example_key', 'default_value')
    print(f"Configuration value for 'example_key': {config_value}")
