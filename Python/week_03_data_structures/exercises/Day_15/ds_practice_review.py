""" Day 15: Data Structures Practice & Review """

# Task Manager

# Requirements:
# Use a Queue for pending tasks (FIFO - first task added is first to do)
# Use a Stack for completed tasks (LIFO) - can undo last completion)
# Use a Linked List for task history (chronological order)

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import Queue
from ds_modules import Stack
from ds_modules import Node
from ds_modules import LinkedList

class TaskManager:
    def __init__(self):
        self.pending = Queue()           # Tasks to do
        self.completed = Stack()         # Completed tasks
        self.history = LinkedList()      # All tasks ever added
    
    # 1) Add Task - Adds to pending queue
    def add_task(self, task):
        """Add new task"""
        # Add to pending queue
        self.pending.enqueue(task)
        # Add to history linked list
        self.history.append(task)
        return
    
    # 2) Complete next task - Dequeue from pending, push to completed stack
    def complete_next(self):
        """Complete the next pending task"""
        # Dequeue from pending
        task = self.pending.dequeue()
        if task:
            # Push to completed
            self.completed.push(task)
            return task
        return None
    
    # 3) Undo completion - Pop from completed, add to pending
    def undo_completion(self):
        """Undo last completion"""
        # Pop from completed
        task = self.completed.pop()
        if task:
            # Add back to pending
            self.pending.enqueue(task)
            return task
        return None
    
    # 4) Show pending - Display queue
    def show_pending(self):
        """Show tasks to do"""
        self.pending.display()
        return
    
    # 5) Show completed - Display stack
    def show_completed(self):
        """Show completed tasks"""
        self.completed.display()
        return
    
    # 6) Show history - Display all tasks ever (linked list)
    def show_history(self):
        """Show all tasks ever added"""
        self.history.display()
        return
    
tm = TaskManager()
tm.add_task("Buy groceries")
tm.add_task("Clean room")
tm.add_task("Study Python")

tm.show_pending()      # All 3 tasks

tm.complete_next()     # Completes "Buy groceries"
tm.show_pending()      # 2 tasks left
tm.show_completed()    # 1 completed

tm.undo_completion()   # Undo "Buy groceries"
tm.show_pending()      # 3 tasks again