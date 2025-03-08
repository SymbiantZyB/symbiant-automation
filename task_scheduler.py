"""
This script demonstrates a simple task scheduler for automation tasks.
"""

# Import necessary modules
import time
import threading

# Task scheduler class
cimport time
import threading
import logging

class TaskScheduler:
    """A task scheduler for running tasks at specified intervals."""

    def __init__(self):
        """Initialize the task scheduler."""
        self.tasks = []
        logging.basicConfig(filename='scheduler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def add_task(self, task, interval):
        """Adds a task to the scheduler with a specified interval in seconds."""
        self.tasks.append((task, interval))
        logging.info(f"Task {task.__name__} added with interval {interval} seconds.")

    def start(self):
        """Starts the task scheduler."""
        logging.info("Task scheduler started.")
        for task, interval in self.tasks:
            threading.Thread(target=self.run_task, args=(task, interval)).start()

    def run_task(self, task, interval):
        """Runs a task at the specified interval."""
        while True:
            task()
            logging.info(f"Task {task.__name__} executed.")
            time.sleep(interval)

    def schedule_event(self, event, action):
        """Schedules an action to be executed when an event occurs."""
        event.wait()
        action()
        logging.info(f"Event {event} triggered action {action.__name__}.")

# Example task function
def example_task():
    """An example task that prints a message."""
    print("Example task executed.")

# Main function
if __name__ == "__main__":
    # Create a task scheduler
    scheduler = TaskScheduler()

    # Add tasks to the scheduler
    scheduler.add_task(example_task, 5)

    # Start the scheduler
    scheduler.start()

    scheduler.add_task(example_task, 5)

    # Start the scheduler
    print("Starting task scheduler...")
    scheduler.start()
