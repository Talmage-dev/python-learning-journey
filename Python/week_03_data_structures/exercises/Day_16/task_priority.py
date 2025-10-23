""" Day 16: Tree Project - Task Priority System """

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')

from ds_modules import Stack, Queue, Node, LinkedList, BinarySearchTree

class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __str__(self):
        return f"{self.name} (Prority: {self.priority})"
    
class TaskPrioritySystem:
    def __init__(self):
        self.priority_tree = BinarySearchTree()
        self.pending = Queue()
        self.completed = Stack()
        self.history = LinkedList()
    
    def add_task(self, name, priority):
        """Add new task to all structures"""
        
        new_task = Task(name, priority)
        self.priority_tree.insert(priority)
        self.pending.enqueue(new_task)
        self.history.append(new_task)

    def complete_next(self):
        """Complete next pending task"""

        task = self.pending.dequeue()
        self.completed.push(task)
        return task
    
    def undo_completion(self):
        """Undo last completion"""

        task = self.completed.pop()
        self.pending.enqueue(task)
        return task

    
    def find_by_priority(self, priority):
        """Check if priority exists"""

        return self.priority_tree.search(priority)

    def show_priorities_sorted(self):
        """Show all priorities in sorted order"""

        self.priority_tree.inorder(self.priority_tree.root)

    def show_pending(self):
        """Show pending tasks"""

        if self.pending.is_empty():
            print(" No pending tasks")
        else:
            for task in self.pending.items:
                print(f" -{task}")

    def show_completed(self):
        """Show completed tasks"""

        if self.completed.is_empty():
            print(" No completed tasks")
        else:
            for task in self.completed.items:
                print(f" -{task}")

system = TaskPrioritySystem()

# Add tasks
system.add_task("Fix critical bug", 90)
system.add_task("Write documentation", 50)
system.add_task("Code review", 70)
system.add_task("Update tests", 60)

print("Pending tasks:")
system.show_pending()

print("\nPriorities (sorted):")
system.show_priorities_sorted()

print("\nCompleting next task...")
task = system.complete_next()
print(f"Completed: {task}")

print("\nCompleted tasks:")
system.show_completed()

print("\nUndo last completion...")
system.undo_completion()

print("\nPending tasks after undo:")
system.show_pending()

print("\nFind priority 70:")
print(system.find_by_priority(70))