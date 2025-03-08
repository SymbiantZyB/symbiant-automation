"""
This script demonstrates a simple task scheduler for automation tasks.
"""

# Import necessary modules
import time
import threading

# Task scheduler class
class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, interval):
        """Adds a task to the scheduler with a specified interval in seconds."""
        self.tasks.append((task, interval))

    def start(self):
        """Starts the task scheduler."""
        for task, interval in self.tasks:
            threading.Thread(target=self._run_task, args=(task, interval)).start()

    def _run_task(self, task, interval):
        """Runs a task at the specified interval."""
        while True:
            task()
            time.sleep(interval)

# Example task function
def example_task():
    """An example task that prints a message."""
    print("Example task executed.")

# Main function
if __name__ == "__main__":
    # Create a task scheduler
    scheduler = TaskScheduler()

    # Add the example task to the scheduler with a 5-second interval
    scheduler.add_task(example_task, 5)

    # Start the scheduler
    print("Starting task scheduler...")
    scheduler.start()
