"""Day 22: Warm Up - Queue Wax On Wax Off"""

# Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0

# Application
# def hot_potato(names, num):
#     """Hot Potato elimination game"""
#     queue = Queue()
#     #Add all names to queue
#     for name in names:
#         queue.enqueue(name)
#     #play until one person left
#     while len(queue.items) > 1:                     # While there is more than one person in the queue
#         #Pass the potato 'num' times
#         for i in range(num):
#             queue.enqueue(queue.dequeue())          # Move first(front of queue) person to the back(back of queue)
#         #Eliminate the person holding potato
#         eliminated = queue.dequeue()                # At the end of the potato passing, front person gets eliminated
#         print(f"{eliminated} is eliminated!")
#     #Return the winner
#     return queue.dequeue()  # Last person in queue

# def task_scheduler(tasks):
#     """Process tasks in order(FIFO)"""
#     queue = Queue()
#     #Add all tasks
#     for task in tasks:
#         queue.enqueue(task)
#         print(f"Task added: {task}")
#     print("\nProcessing tasks...")
#     #Process all tasks
#     while not queue.is_empty():         # While there are tasks to process
#         task = queue.dequeue()          # process task
#         print(f"Processing: {task}")    # display task being processed
#     print("All tasks complete!")

# def print_queue_simulation():
#     """Simulate printer queue"""
#     printer = Queue()
#     #Add printjobs
#     jobs = ["Document1.pdf", "Photo.jpg", "Report.docx", "Presentation.pptx"]
#     print("=== Adding print jobs ===")
#     for job in jobs:
#         printer.enqueue(job)
#         print(f"Added to queue: {job}")
#     print(f"\nJobs in queue: {len(printer.items)}")
#     print("\n=== Printing ===")
#     while not printer.is_empty():
#         current = printer.dequeue()
#         print(f"Printing: {current}...")
#     print("\nAll Jobs printed!")

def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    while len(queue.items) > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        eliminated = queue.dequeue()
        print(f"{eliminated} has being eliminated")
    return queue.dequeue()

def task_scheduler(tasks):
    task_list = Queue()
    for task in tasks:
        task_list.enqueue(task)
        print(f"Task added: {task}")
    
    print("\nProcessing tasks...")
    while not task_list.is_empty():
        task = task_list.dequeue()
        print(f"Processing: {task}")
    
    print("All tasks complete!")

def print_queue_simulation():
    queue = Queue()
    jobs = ["Sonic.jpg", "CV.docx", "world_history.pdf"]
    for job in jobs:
        queue.enqueue(job)
        print(f"Added to queue: {job}")
    print(f"\nJobs in queue: {len(queue.items)}")
    print("\n=== Printing ===")
    while not queue.is_empty():
        current = queue.dequeue()
        print(f"Printing: {current}")
    print("\nAll jobs printed!")

# ===== TESTS =====

print("=" * 50)
print("TEST 1: Hot Potato")
print("=" * 50)
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
winner = hot_potato(names, 3)
print(f"\nWinner: {winner}")

print("\n" + "=" * 50)
print("TEST 2: Task Scheduler")
print("=" * 50)
tasks = ["Compile code", "Run tests", "Deploy app", "Send email"]
task_scheduler(tasks)

print("\n" + "=" * 50)
print("TEST 3: Print Queue")
print("=" * 50)
print_queue_simulation()