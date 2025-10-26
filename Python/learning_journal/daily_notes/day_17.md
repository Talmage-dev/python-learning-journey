# Day 17 Summary - Comprehensive Review & Problem-Solving Framework

---

## **Date:** October 24, 2025 (Friday)

---

## **Main Achievements:**

1. **Morning Warm-Up** - Mini "Wax On Wax Off" review of all 5 structures
2. **Restaurant Order System** - Combined Queue, Stack, BST, Dictionary
3. **Problem-Solving Framework** - Learned systematic approach to projects
4. **Grade Calculator** - Built from requirements to working code independently

---

## **Morning Session: Mini Review**

### **"Wax On Wax Off" Warm-Up (15 minutes)**

**Purpose:** Quick review to warm up brain before learning

**Exercises Completed:** 5 (one per structure)
- Stack: `pop()` ✓
- Queue: `front()` ✓
- Singly Linked List: `search()` ✓
- Doubly Linked List: `append()` ✓
- Binary Search Tree: `search()` ✓ (1 typo, corrected)

**Result:** All structures refreshed, brain warmed up!

---

## **Project 1: Restaurant Order System**

### **Overview**

Built a comprehensive restaurant management system combining multiple data structures.

### **Structures Used:**

1. **Binary Search Tree** - Menu prices (sorted display)
2. **Queue** - Pending orders (FIFO processing)
3. **Stack** - Completed orders (LIFO history)
4. **Dictionary** - Menu items lookup (fast access by name)

### **Classes Implemented:**

**MenuItem:**
```python
class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.category})"

Order:
class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.total = sum(item.price for item in items)
    
    def __str__(self):
        items_str = ", ".join(item.name for item in self.items)
        return f"Order #{self.order_id}: {items_str} - Total: ${self.total:.2f}"

RestaurantSystem:
add_menu_item(name, price, category) # Add to menu
place_order(item_names) # Create and queue order
complete_next_order() # Process FIFO
view_pending_orders() # Show queue
view_recent_orders() # Show stack
view_menu_sorted() # BST in-order traversal

How Each Structure Was Used:

BST (Menu Prices)
- Stored prices for sorted display
- In-order traversal: 1.99, 3.99, 6.99, 8.99, 12.99
- Fast price-based operations

Queue (Pending Orders)
- FIFO: First order placed is first cooked
- Order #1 → Order #2 → Order #3
- Completed in order received

Stack (Completed Orders)
- LIFO: Most recent completions shown first
- Can view recent order history
- Undo-friendly structure
 
Dictionary (Menu Items)
- Fast lookup by item name
- O(1) access time
- Easy to check if item exists

Output:
=== Menu (sorted by price) ===
1.99  3.99  6.99  8.99  12.99

=== Placing Orders ===
Order #1: Burger, Fries, Soda - Total: $14.97
Order #2: Pizza, Salad - Total: $19.98
Order #3: Burger, Soda - Total: $10.98

=== Pending Orders ===
Order #1, #2, #3

=== Completing Orders ===
Completed Order #1 (FIFO!)
Completed Order #2 (FIFO!)

=== Pending Orders (after completing 2) ===
Order #3

=== Recent Completed Orders ===
Order #1, Order #2

Key Learning:

✅ Structure Selection - Chose right structure for each task
✅ Integration - Combined multiple structures effectively
✅ Real-World Application - Practical restaurant system
✅ Data Flow - Understood how data moves between structures

- - -

Problem-Solving Framework

The 5-Step Process:

Step 1: Understand the Problem
- What is the goal?
- Who will use it?
- What are inputs/outputs?
- What are the rules?

Step 2: Gather Requirements
- Must-have features
- Nice-to-have features
- Data to store
- Operations needed
- Edge cases

Step 3: Design the Solution
- Choose data structures
- Plan classes/functions
- Map data flow
- Define MVP

Step 4: Break It Down
- Smallest buildable piece
- What to test first
- Dependencies
- Build order

Step 5: Implement & Test
- Build one piece
- Test immediately
- Fix issues
- Move to next
- Repeat

Customer-Friendly Questions:

Instead of technical jargon:
"What information do you need to provide?" (inputs)
"What do you want to see at the end?" (outputs)
"Walk me through what you'd type in" (workflow)
"What results are you looking for?" (expectations)

- - -

Project 2: Grade Calculator

Requirements Gathering Process:

Questions Asked:
1. What is the main goal? → Calculate final grade
2. Who will use it? → Teachers and students
3. What information from user? → 4 scores
4. What information to user? → Final grade + letter
5. What constraints/rules? → Validation, weights, scale
6. What edge cases? → Invalid input, boundaries

Requirements Gathered:

Inputs:
- Homework average (0-100)
- Quiz average (0-100)
- Midterm exam score (0-100)
- Final exam score (0-100)

Outputs:
- Final grade percentage (2 decimals)
- Letter grade (A, B, C, D, F)

Weights:
- Homework: 20%
- Quizzes: 20%
- Midterm: 30%
- Final: 30%

Grading Scale:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

Edge Cases:
- Invalid input (negative, > 100)
- Non-numeric input
- Perfect score (100)
- Zero score (0)
- Boundary cases (exactly 90.0)

Implementation:

Features Built:
- Input validation with try/except
- Weighted grade calculation
- Letter grade conversion
- Multiple student support (bonus!)
- Student lookup by name (bonus!)
- Menu system (bonus!)

Functions Created:
homework() - Get and validate homework score
quiz() - Get and validate quiz score
mid_term() - Get and validate midterm score
final_score() - Get and validate final score
enter_student_info() - Collect all data and calculate
display_student_information() - Show results
main() - Menu system

Calculation:
grade = (homework * 0.2) + (quiz * 0.2) + (midterm * 0.3) + (final * 0.3)

Example:
- Homework: 80 × 0.2 = 16.0
- Quiz: 90 × 0.2 = 18.0
- Midterm: 70 × 0.3 = 21.0
- Final: 85 × 0.3 = 25.5
- Total: 80.5% → B

Challenges & Solutions:

Challenge 1: Repetitive Input Functions
- Problem: 4 nearly identical functions
- Solution: Could refactor into one get_score(type) function
- Learning: DRY principle (Don't Repeat Yourself)

Challenge 2: Dictionary Lookup Bug
# ❌ Wrong - crashes if key doesn't exist
if student[stud_name]:

# ✓ Right - checks if key exists first
if stud_name in student:

Challenge 3: Input Validation
- Problem: Need to handle invalid and non-numeric input
- Solution: while loop + try/except + range check
- Learning: Validate early, validate thoroughly

Testing:
✅ Valid input (50, 75, 80, 90)
✅ Invalid input (-5, 150)
✅ Non-numeric input ("abc")
✅ Boundary cases (exactly 90.0)
✅ Perfect score (100)
✅ Zero score (0)
✅ Multiple students
✅ Student lookup (existing and non-existing)

- - -

Skills Reinforced:

Technical Skills:
✅ Data structure selection - Choosing right tool for job
✅ Structure integration - Combining multiple structures
✅ Input validation - try/except, range checking
✅ Error handling - Graceful failure
✅ Dictionary operations - Key checking, lookup
✅ Weighted calculations - Mathematical operations
✅ Conditional logic - if/elif chains
✅ Code organization - Functions and classes

Problem-Solving Skills:
✅ Requirements gathering - Asking right questions
✅ Customer communication - Non-technical language
✅ System design - Planning before coding
✅ Incremental development - Build piece by piece
✅ Testing strategy - Test as you go
✅ Debugging - Finding and fixing issues
✅ Code refactoring - Identifying improvements

Soft Skills:
✅ Self-assessment - Identifying knowledge gaps
✅ Learning strategy - Adjusting approach
✅ Persistence - Working through challenges
✅ Communication - Asking clarifying questions

- - -

Statistics:
Time spent: ~6-7 hours
Projects completed: 2 (Restaurant System, Grade Calculator)
Structures reviewed: 5 (all current structures)
Methods practiced: 5 (warm-up)
Lines of code: ~250+ (both projects)
Bugs fixed: 2 (dictionary lookup, input validation)
Typing practice: 30.1 WPM, 95.57% accuracy

- - -

Key Achievements:
🏆 Completed comprehensive morning warm-up
🏆 Built Restaurant System combining 4 structures
🏆 Learned systematic problem-solving framework
🏆 Gathered requirements like a professional
🏆 Built Grade Calculator independently
🏆 Handled all edge cases properly
🏆 Debugged and fixed issues
🏆 Went beyond requirements (bonus features!)

- - -

Key Insights:

On Structure Selection:
- BST for sorted data
- Queue for FIFO processing
- Stack for LIFO/undo
- Dictionary for fast lookup
- The right structure makes code simpler!

On Problem-Solving:
- Ask questions BEFORE coding
- Understand requirements fully
- Plan the solution first
- Build incrementally
- Test continuously
- Process matters more than code!

On Requirements Gathering:
- Use customer-friendly language
- Ask about inputs and outputs
- Clarify constraints and rules
- Identify edge cases early
- Better questions = better solutions!

On Learning:
- Warm-ups work! Brain gets in "coding mode"
- Building from scratch reveals gaps
- Making mistakes is valuable
- Fixing bugs teaches debugging
- Independent practice builds confidence!

- - -

Challenges Faced:
1. Structure selection - Which to use when?
        - Solved: Framework for choosing structures
2. Requirements gathering - What questions to ask?
        - Solved: Learned customer-friendly questions
3. Dictionary lookup - Checking key existence
        - Solved: Use in operator before accessing
4. Code repetition - 4 similar functions
        - Identified: Could refactor with parameters
5. Independent building - Confidence in solo work
        - Addressed: Problem-solving framework provides structure

All challenges led to valuable learning!

- - -

Roadmap Status:

AHEAD OF SCHEDULE! 🚀
Current: Day 17 (Oct 24)
Original plan: Should be finishing Week 1-2 (Fundamentals)
Actual progress: Halfway through Week 5-6 (Data Structures)!
Ahead by: ~2-3 weeks

Data Structures Progress:
1. ✅ Stacks (Day 13) - MASTERED
2. ✅ Queues (Day 13) - MASTERED
3. ✅ Singly Linked Lists (Day 14) - MASTERED
4. ✅ Doubly Linked Lists (Day 14) - MASTERED
5. ✅ Binary Search Trees (Day 16) - MASTERED
6. ⬜ Hash Tables (after camp)
7. ⬜ Graphs (after camp)

5 out of 7 data structures complete!

- - -

Updated Learning Strategy:

New Focus: Retention & Application

Daily Routine:

1. Morning (30 min):
    - Typing practice (15 min)
    - Mini "Wax On Wax Off" (15 min) - Last 3 days
2. Learning (2-4 hours):
    - Four-step process (Learn → Example → Practice → Apply)
3. End of Day (5-10 min):
    - Reflection and planning

Weekly:
- Comprehensive "Wax On Wax Off" (30 min)
- Application practice (2-3 times)
- One major topic per week (not per day!)

Goal:

Deep understanding over speed

- - -

Tomorrow's Plan:

Church Camp! 🏕️ (Oct 25-26)
- 2-day break
- Rest and recharge
- Come back refreshed

When You Return (Day 18 - Monday, Oct 27):
- Morning warm-up routine
- Review all 5 structures
- Problem-solving practice
- Possibly start Hash Tables

- - -

Reflections:

Today was transformative! Learning the problem-solving framework filled a critical gap - I now know HOW to approach any project systematically.

The morning warm-up routine worked perfectly. Starting with typing practice, then reviewing previous structures got my brain in "coding mode" before tackling new material. This will be my daily routine going forward.

Building the Restaurant System showed me how to choose and combine structures effectively. Each structure had a clear purpose:
- BST for sorted menu
- Queue for order processing
- Stack for history
- Dictionary for lookups

The Grade Calculator was the real test - building from requirements to working code independently. The problem-solving framework guided me through:
1. Asked the right questions
2. Gathered complete requirements
3. Designed the solution
4. Built incrementally
5. Tested and fixed bugs

I went beyond requirements by adding multiple student support and a menu system. This shows I'm thinking about real-world usability, not just meeting specs.

The dictionary lookup bug taught me about key existence checking - a valuable lesson that will prevent future crashes.

Identifying that I need better retention and application skills was honest self-assessment. The updated learning strategy addresses this with daily reviews and slower pacing. Quality over speed!

The problem-solving framework is now my guide for every project. It transforms vague ideas into concrete steps. This is the skill that separates beginners from professionals.

Ready for church camp break, then back to continue building on this solid foundation!

- - -

Personal Notes:
Typing: 30.1 WPM, 95.57% accuracy
Identified weak keys: 'a' (26 WPM), 'r' (21 WPM)
Strong keys: 'l', 'i', 'o' (30+ WPM)
Keybr will focus on weak keys automatically
Morning warm-up routine is perfect
Problem-solving framework is game-changing
Independent building builds confidence
Ahead of schedule but focusing on depth
Church camp this weekend!

- - -

Resources Used:
Mini "Wax On Wax Off" review
Restaurant System project (guided)
Problem-solving framework (new!)
Grade Calculator (independent)
Requirements gathering practice
Customer-friendly communication
Debugging and testing

- - -

Next Session Preview:
Church camp break (2 days)
Return Monday refreshed
Continue with retention-focused strategy
More problem-solving practice

- - -

Total Days Completed: 17/60 (Phase 1)
Progress: Ahead of schedule ✓
Confidence Level: Very High 💪
Data Structures: 5/7 mastered
Problem-Solving: Framework learned ✓
Independent Building: Confidence growing ✓

- - -

End of Day 17 Summary