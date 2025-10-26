# Problem-Solving Framework for Programming Projects

## Date Created: October 24, 2025

---

## Overview

A systematic approach to building any programming project from requirements to working code.

---

## The 5-Step Process

### Step 1: Understand the Problem
### Step 2: Gather Requirements
### Step 3: Design the Solution
### Step 4: Break It Down
### Step 5: Implement & Test

---

## Step 1: Understand the Problem

### Questions to Ask:

1. **What is the main goal/purpose?**
   - What problem are we solving?
   - Why does this need to exist?

2. **Who will use it?**
   - End users (students, teachers, customers, etc.)
   - Technical level of users?

3. **What are the inputs?**
   - Customer-friendly: "What information do you need to provide?"
   - "What data will you enter into the system?"
   - "Walk me through what you'd type in"

4. **What are the outputs?**
   - Customer-friendly: "What do you want to see at the end?"
   - "What results are you looking for?"
   - "What should the program tell you?"

5. **What are the constraints/rules?**
   - Any limitations?
   - Business rules?
   - Technical requirements?

### Example:

**Problem:** Build a grade calculator

**Answers:**
- **Goal:** Calculate student's final grade
- **Users:** Teachers and students
- **Inputs:** Homework, quiz, midterm, final scores
- **Outputs:** Final percentage and letter grade
- **Rules:** Weighted calculation, standard grading scale

---

## Step 2: Gather Requirements

### Questions to Ask:

1. **What features are MUST-HAVE?**
   - Core functionality
   - Without these, it doesn't work

2. **What features are NICE-TO-HAVE?**
   - Extra features
   - Can be added later

3. **What data needs to be stored?**
   - Temporary vs permanent
   - What format?

4. **What operations need to be performed?**
   - Calculations
   - Lookups
   - Modifications

5. **Are there any edge cases?**
   - Invalid input
   - Empty data
   - Boundary conditions
   - Error scenarios

### Example:

**Grade Calculator Requirements:**

**Must-Have:**
- Accept 4 scores (homework, quiz, midterm, final)
- Calculate weighted average
- Display letter grade

**Nice-to-Have:**
- Store multiple students
- Look up by name
- View all students

**Data:**
- Student name (string)
- 4 scores (floats, 0-100)
- Final grade (float)
- Letter grade (string)

**Operations:**
- Input validation
- Weighted calculation
- Grade conversion

**Edge Cases:**
- Invalid input (negative, > 100, non-numeric)
- Perfect score (100)
- Zero score (0)
- Boundary cases (exactly 90.0)

---

## Step 3: Design the Solution

### Questions to Ask:

1. **What data structures do I need?**
   - Lists, dictionaries, sets?
   - Stack, queue, tree?
   - Custom classes?

2. **What classes/functions do I need?**
   - What are the main components?
   - How do they interact?

3. **How will data flow through the system?**
   - Input → Processing → Output
   - What transforms the data?

4. **What's the simplest version that works?**
   - MVP (Minimum Viable Product)
   - What can I build first?

### Data Structure Selection Guide:

**Need to store:**
- **Ordered collection** → List
- **Key-value pairs** → Dictionary
- **Unique items** → Set
- **LIFO (undo)** → Stack
- **FIFO (queue)** → Queue
- **Sorted data** → Binary Search Tree
- **Fast lookup** → Dictionary or Hash Table
- **Hierarchical data** → Tree
- **Relationships** → Graph

### Example:

**Grade Calculator Design:**

**Data Structures:**
- List of dictionaries for students
- Dictionary for each student's info

**Functions:**
- `get_score(type)` - Input validation
- `calculate_grade(scores)` - Weighted calculation
- `get_letter_grade(percentage)` - Convert to letter
- `add_student()` - Add new student
- `display_student(name)` - Show results

**Data Flow:**

Input scores → Validate → Calculate weighted average → Convert to letter → Store → Display

**MVP:**
- Single student
- Basic calculation
- No validation (add later)

- - -

## Step 4: Break It Down

### Questions to Ask:

1. **What's the smallest piece I can build first?**
   - Start with core functionality
   - Build incrementally

2. **What can I test immediately?**
   - Each piece should be testable
   - Don't build everything before testing

3. **What depends on what?**
   - Build dependencies first
   - Independent pieces can be parallel

4. **What order should I build things?**
   - Bottom-up or top-down?
   - What makes sense?

### Build Order Strategy:

**Option 1: Bottom-Up**
1. Build basic data structures
2. Build helper functions
3. Build main functions
4. Build user interface

**Option 2: Top-Down**
1. Build main structure (skeleton)
2. Fill in functions (stubs first)
3. Implement each function
4. Test and refine

**Option 3: Feature-by-Feature**
1. Build one complete feature
2. Test it thoroughly
3. Move to next feature
4. Integrate features

### Example:

**Grade Calculator Build Order:**

**Phase 1: Core Calculation**
1. Write calculate_grade() function
2. Test with hardcoded values
3. Write get_letter_grade() function
4. Test grade conversion

**Phase 2: Input**
1. Write get_score() function
2. Add validation
3. Test with invalid inputs

**Phase 3: Storage**
1. Create student dictionary structure
2. Write add_student() function
3. Test adding students

**Phase 4: Display**
1. Write display_student() function
2. Test lookup

**Phase 5: Interface**
1. Add menu system
2. Connect all pieces
3. Final testing

- - -

## Step 5: Implement & Test

### The Process:

1. **Write one small piece**
   - Focus on one function/feature
   - Keep it simple

2. **Test it immediately**
   - Don't wait to test
   - Use print statements
   - Try edge cases

3. **Fix any issues**
   - Debug as you go
   - Don't accumulate bugs

4. **Move to next piece**
   - Build on what works
   - Iterate

5. **Repeat**
   - Keep building incrementally
   - Test continuously

### Testing Strategy:

**For Each Function:**
- ✅ Test with valid input
- ✅ Test with invalid input
- ✅ Test edge cases
- ✅ Test boundary conditions

**Example Test Cases:**

```python
# Test calculate_grade()
print(calculate_grade(100, 100, 100, 100))  # Should be 100.0
print(calculate_grade(0, 0, 0, 0))          # Should be 0.0
print(calculate_grade(80, 90, 70, 85))      # Should be 80.5

# Test get_letter_grade()
print(get_letter_grade(95))   # Should be 'A'
print(get_letter_grade(90))   # Should be 'A' (boundary)
print(get_letter_grade(89.9)) # Should be 'B'
print(get_letter_grade(0))    # Should be 'F'

# Test get_score()
# Try entering: -5, 150, "abc", 50

- - -

Common Patterns

Pattern 1: Input Validation
def get_valid_input(prompt, min_val, max_val):
    """Get validated numeric input"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Must be between {min_val} and {max_val}")
        except ValueError:
            print("Must be a number")

Pattern 2: Menu System
def main():
    """Main program loop"""
    while True:
        print("\nMenu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Quit")
        
        choice = input("Choose: ")
        
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            break
        else:
            print("Invalid choice")

Pattern 3: Data Storage
# List of dictionaries
students = []

# Add item
student = {
    'name': 'Alice',
    'grade': 95.5,
    'letter': 'A'
}
students.append(student)

# Find item
for student in students:
    if student['name'] == 'Alice':
        print(student['grade'])

Pattern 4: Calculation with Weights
def weighted_average(values, weights):
    """Calculate weighted average"""
    total = sum(v * w for v, w in zip(values, weights))
    return total

# Example
scores = [80, 90, 70, 85]
weights = [0.2, 0.2, 0.3, 0.3]
final = weighted_average(scores, weights)

- - -

Debugging Tips

When Stuck:

1. Print everything
- Print variables at each step
- See what's actually happening

2. Test smaller pieces
- Isolate the problem
- Test functions individually

3. Check assumptions
- Is the data what you think it is?
- Are functions returning what you expect?

4. Read error messages
- They tell you exactly what's wrong
- Line numbers are your friend

5. Take a break
- Fresh eyes see problems
- Walk away and come back

Common Mistakes:
Off-by-one errors - Check loop ranges
Type mismatches - String vs number
Missing return - Function returns None
Wrong variable - Typo in variable name
Logic errors - if/elif order matters

- - -

Example: Complete Process

Problem: Build a Todo List

Step 1: Understand
- Goal: Manage daily tasks
- Users: Anyone with tasks
- Input: Task descriptions
- Output: List of tasks, mark complete
- Rules: Tasks can be added, completed, deleted

Step 2: Requirements
- Must-have: Add, complete, view tasks
- Nice-to-have: Priority, due dates
- Data: Task text, completion status
- Operations: Add, complete, delete, display
- Edge cases: Empty list, invalid task number

Step 3: Design
- Data structure: List of dictionaries
- Functions: add_task(), complete_task(), view_tasks()
- Flow: Input → Store → Display
- MVP: Just add and view (no complete yet)

Step 4: Break Down
1. Create task list (empty list)
2. Write add_task() - append to list
3. Write view_tasks() - print all
4. Write complete_task() - mark as done
5. Add menu system
6. Test everything

Step 5: Implement
tasks = []

def add_task(description):
    task = {'description': description, 'done': False}
    tasks.append(task)
    print(f"Added: {description}")

def view_tasks():
    if not tasks:
        print("No tasks")
        return
    for i, task in enumerate(tasks, 1):
        status = "✓" if task['done'] else " "
        print(f"{i}. [{status}] {task['description']}")

def complete_task(task_num):
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1]['done'] = True
        print("Task completed!")
    else:
        print("Invalid task number")

# Test
add_task("Buy groceries")
add_task("Study Python")
view_tasks()
complete_task(1)
view_tasks()

- - -

Key Principles
1. Start Simple - Build MVP first, add features later
2. Test Early - Don't wait until everything is built
3. One Thing at a Time - Focus on one piece
4. Ask Questions - Better to clarify than assume
5. Iterate - Build, test, improve, repeat
6. Document - Comments and clear names
7. Handle Errors - Validate input, catch exceptions
8. Think in Steps - Break complex into simple

- - -

Practice Projects by Level

Beginner (Variables, Functions, Lists)
- Calculator
- Temperature converter
- Grade calculator
- Todo list
- Contact list

Intermediate (Dictionaries, Classes, Files)
- Student management system
- Inventory tracker
- Expense tracker
- Library system
- Recipe manager

Advanced (Data Structures, Algorithms)
- Task priority system
- Restaurant order system
- File organizer
- Search engine (simple)
- Game with AI

- - -

Checklist for Every Project

Before Coding:
[ ] Understand the problem
[ ] Gather all requirements
[ ] Design the solution
[ ] Break into small pieces
[ ] Know what to build first

While Coding:
[ ] Build one piece at a time
[ ] Test immediately
[ ] Fix bugs as you go
[ ] Add comments
[ ] Handle edge cases

After Coding:
[ ] Test all features
[ ] Test edge cases
[ ] Clean up code
[ ] Add documentation
[ ] Get feedback

- - -

Remember

Good programmers:
- Ask lots of questions
- Plan before coding
- Build incrementally
- Test continuously
- Learn from mistakes

The process matters more than the code!

- - -

End of Problem-Solving Framework