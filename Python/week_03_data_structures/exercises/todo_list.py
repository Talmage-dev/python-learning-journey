class TodoItem:                                     # Node
    def __init__(self, task, priority):
        self.task = task                            # data
        self.priority = priority                    # data
        self.next = None                            # pointer
    
class TodoList:
    def __init__(self):
        self.head = None                            # First position

    def add_task(self, task, priority):             # Add node at the end
        new_item = TodoItem(task, priority)

        if self.head is None:                       # If there is no 1st node
            self.head = new_item                    # Put it as 1st
            return
        
        current = self.head                         # If there are things already on the list
        while current.next:                         # while a pointer points to something
            current = current.next                  # keep moving till there is no pointer
        current.next = new_item                     # Add to end of list

    def complete_task(self, task):                  # Delete Task 
        if self.head and self.head.task == task:
            self.head = self.head.next
            return True
            
        current = self.head
        while current and current.next:             # while there is a node with a pointer
            if current.next.task == task:           # if you find the node you want to delete
                current.next = current.next.next    # skip it (make the previous pointer point at the next node)
                return True
            current = current.next                  # keep looking
        return False                                # Not Found
    
    def show_tasks(self):
        current = self.head                         # Start at the begining
        while current:                              # While there is a node to show
            print(current.task)                     # print node
            current = current.next                  # move to the next node
        print("No more things to do")

todos = TodoList()
todos.add_task("Buy groceries", "high")
todos.add_task("Clean room", "medium")
todos.add_task("Watch movie", "low")
todos.show_tasks()

todos.complete_task("Clean room")
todos.show_tasks()