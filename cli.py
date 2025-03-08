"""
Command-Line Interface Module
------------------------------
Provides CLI capabilities for running automation tasks.

Author: SymbiantZyB
"""

import argparse

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="SymbiantZyB Automation CLI")
    parser.add_argument("-t", "--task", help="Specify task to run", required=True)
    args = parser.parse_args()
    
    if args.task == "example":
        print("Running example task...")

# CLI Entry Point
if __name__ == "__main__":
    main()
