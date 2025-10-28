# Day 18 Summary - Targeted Practice & Application Projects

---

## **Date:** October 26, 2025 (Sunday - After Church Camp)

---

## **Main Achievements:**

1. **Morning Warm-Up** - Mini "Wax On Wax Off" review (5 exercises)
2. **Targeted Practice** - 22 exercises on BST & Doubly Linked List
3. **Product Comparison Tool** - Complete application using BST
4. **Library Book Tracker** - Independent project (in progress)

---

## **Morning Session: Warm-Up & Assessment**

### **Typing Practice:**
- **Speed:** 32.7 WPM
- **Accuracy:** 95.49%
- **Weak keys identified:** 'a' (26 WPM), 'r' (21 WPM)
- **Strong keys:** 'l', 'i', 'o' (30+ WPM)
- **Status:** Consistent, no regression from 2-day break

### **Mini "Wax On Wax Off" (5 exercises):**

**Results:**
- Stack: `pop()` ✓
- Queue: `front()` ✓
- Singly Linked List: `search()` ✓
- Doubly Linked List: `append()` ✓ (after fixing missing return)
- Binary Search Tree: `search()` ✓ (after fixing missing self.)

**Self-Assessment:**
- Stack/Queue: Solid
- Singly Linked List: Good (just needed safety check reminder)
- Doubly Linked List: Okay (pointer order confusion)
- **BST: Went blank, needed refresher** ⚠️

**Decision:** Focus on BST and Doubly Linked List today

---

## **Targeted Practice Session**

### **Goal:**
Master BST and Doubly Linked List through intensive practice

### **Methods Practiced:**

**Binary Search Tree (7 methods):**
1. TreeNode `__init__`
2. BST `__init__`
3. `insert`
4. `_insert_recursive`
5. `search`
6. `_search_recursive`
7. `inorder`

**Doubly Linked List (4 methods):**
1. `append`
2. `prepend`
3. `delete`
4. `display_forward`

### **Results:**

**Total Exercises:** 22 (11 methods × 2 times each)

**All 11 methods mastered!** ✓✓

### **Common Mistakes Corrected:**

**BST Mistakes:**
1. **TreeNode parameters** - Passing two parameters instead of one
   ```python
   # ❌ Wrong
   TreeNode(node, data)
   # ✓ Right
   TreeNode(data)

1. Missing self. - Forgetting self. when calling methods
# ❌ Wrong
return _search_recursive(self.root, data)
# ✓ Right
return self._search_recursive(self.root, data)

2. Wrong node check - Checking self.root instead of node parameter
# ❌ Wrong
if self.root is None:
# ✓ Right
if node is None:

3. Missing empty tree check - Not handling empty tree in insert
# ❌ Wrong
def insert(self, data):
    self._insert_recursive(self.root, data)

# ✓ Right
def insert(self, data):
    if self.root is None:
        self.root = TreeNode(data)
    else:
        self._insert_recursive(self.root, data)

4. Typos - "inorder" instead of "inorder of "inorder", "recursive" instead of "recursive"

DLL Mistakes:

1. Missing return - Not returning after empty list case
# ❌ Wrong
if self.head is None:
    self.head = new_node
    self.tail = new_node
# Code continues...

# ✓ Right
if self.head is None:
    self.head = new_node
    self.tail = new_node
    return

2. Wrong method name - Writing "prepend" when implementing "append"

3. Redundant head check - Special casing head deletion when loop handles it

Progress Tracking:

Before targeted practice:
- BST made me go blank
- Doubly LL pointer order confused me

After targeted practice:
- Wrote all BST methods twice correctly
- Wrote all DLL methods twice correctly
- Confidence restored!

- - -

Project 1: Product Price Comparison Tool

Overview:

Built a system to compare product prices from different stores using BST for sorted price display.

Classes Implemented:

Product:
class Product:
    def __init__(self, name, price, store):
        self.name = name
        self.price = price
        self.store = store
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} at {self.store}"

ProductComparison:
add_product(name, price, store) - Add product to system
find_by_price(price) - Find all products at specific price
show_all_sorted() - Display all products sorted by price
find_cheapest() - Find lowest priced product(s)
find_most_expensive() - Find highest priced product(s)

Data Structures Used:
1. Binary Search Tree - Store prices for sorted operations
2. Dictionary - Fast lookup: price → list of products

How It Works:

Adding Products:
- Insert price into BST
- Add product to dictionary (price as key)
- Multiple products can have same price (stored in list)

Finding Products:
- By price: O(1) dictionary lookup
- Sorted display: Sort dictionary keys
- Min/max: Use Python's min()/max() on keys

Test Results:
=== All Products (Sorted by Price) ===
Google Pixel - $699.99 at Google Store
OnePlus 12 - $799.99 at OnePlus Store
Samsung Galaxy - $899.99 at Samsung Store
iPhone 15 - $949.99 at Best Buy
iPhone 15 - $949.99 at Amazon
iPhone 15 - $999.99 at Apple Store

=== Products at $949.99 ===
iPhone 15 - $949.99 at Best Buy
iPhone 15 - $949.99 at Amazon

=== Cheapest Product(s) ===
Google Pixel - $699.99 at Google Store

=== Most Expensive Product(s) ===
iPhone 15 - $999.99 at Apple Store

Perfect output! ✓

Key Learning:
- BST provides natural sorting
- Dictionary provides fast lookup
- Combining structures leverages strengths of each
- Real-world application solidifies understanding

- - -

Project 2: Library Book Tracker (In Progress)

Requirements Gathered:

Used problem-solving framework:
1. ✅ Asked about main goal/purpose
2. ✅ Asked about users
3. ✅ Asked about inputs/outputs
4. ✅ Asked about constraints/rules/edge cases

Purpose:

Track library books and checkouts

Users:

Librarian (non-technical, needs simple interface)

Inputs:
- Book info (title, author, ISBN)
- Borrower names
- Search queries

Outputs:
- Book lists with status
- Availability information
- Confirmation messages

Rules:
- Unique book titles
- One borrower per book at a time
- Can't check out already checked out book
- Can't return available book

Edge Cases:
- Empty library
- Book not found
- Duplicate books
- Already checked out
- Not checked out
- Empty input

Implementation (So Far):

Book Class:

python

class Book:
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrower = None
    
    def is_available(self):
        return self.borrower is None

Library Class:
- add_book(title, author) ✓
- check_out(title, borrower) ✓
- return_book(title) ✓
- search_book(title) ✓
- list_books() ✓

Data Structure:

Dictionary (title → Book object)

What Works:
✅ Add books with duplicate detection
✅ Check out books with validation
✅ Return books with validation
✅ Search by title
✅ List all books
✅ All edge cases handled
✅ Clear error messages

To Complete Tomorrow:

[ ] Add str method to Book class
[ ] Fix check_out error message (shows wrong borrower)
[ ] Remove broken display() method
[ ] Add menu system for user interaction
[ ] Add view available books only
[ ] Add view checked out books only
[ ] Add search by author
[ ] Test all features

Independent Work Assessment:

Strengths:
- Used problem-solving framework correctly
- Asked all the right questions
- Designed clean class structure
- Handled all edge cases
- Good error messages
- Tested as I built

Areas for Improvement:
- Small bugs (wrong variable in error message)
- Missing str method
- Need to remove unused code

Overall:

Excellent independent work! 💪

- - -

Skills Reinforced:

Technical Skills:
✅ BST mastery - All methods from memory
✅ DLL mastery - All methods from memory
✅ Recursive thinking - Natural for trees
✅ Pointer manipulation - Doubly linked list updates
✅ Dictionary operations - Fast lookups
✅ Class design - Clean, focused classes
✅ Error handling - All edge cases covered
✅ Method design - Clear, single responsibility

Problem-Solving Skills:
✅ Requirements gathering - Asked right questions
✅ System design - Chose appropriate structures
✅ Incremental development - Built piece by piece
✅ Testing - Tested as I built
✅ Debugging - Fixed issues independently
✅ Self-assessment - Identified weak areas

Learning Skills:
✅ Targeted practice - Focused on weak areas
✅ Repetition - Built muscle memory
✅ Application - Used knowledge in projects
✅ Independence - Built project solo
✅ Framework usage - Applied problem-solving process

- - -

Statistics:
Time spent: ~7-8 hours
Typing practice: 32.7 WPM, 95.49% accuracy
Warm-up exercises: 5
Targeted practice exercises: 22
Methods mastered: 11 (BST + DLL)
Projects started: 2
Projects completed: 1 (Product Comparison)
Projects in progress: 1 (Library System)
Lines of code: ~300+
Bugs fixed: Multiple (typos, logic errors, missing checks)

- - -

Key Achievements:
🏆 Completed morning warm-up routine
🏆 Identified weak areas (BST, DLL)
🏆 Targeted practice on weak areas
🏆 Mastered all 11 methods (22 exercises)
🏆 Built Product Comparison Tool (complete)
🏆 Started Library System independently
🏆 Used problem-solving framework correctly
🏆 BST confidence fully restored
🏆 No regression from 2-day break

- - -

Key Insights:

On Targeted Practice:
- Focusing on weak areas works!
- 22 exercises in one session built solid muscle memory
- Writing methods twice ensures mastery
- Immediate feedback catches mistakes
- BST went from "blank" to "mastered" in one session!

On Application Projects:
- Real projects solidify understanding
- Combining structures shows their strengths
- Product Comparison showed BST's natural sorting
- Library System showed dictionary's fast lookup
- Building something useful is motivating

On Independent Work:
- Problem-solving framework guides the process
- Asking right questions gets right requirements
- Can design and build systems independently now
- Small bugs are normal and fixable
- Testing as you build catches issues early

On Learning Strategy:
- Morning warm-up works perfectly
- Targeted practice addresses weak spots
- Application projects cement knowledge
- Independent work builds confidence
- The retention-focused strategy is working!

- - -

Challenges Faced:

1. BST went blank in warm-up
- Solved: Targeted 22-exercise practice session
- Result: Full mastery restored

2. DLL pointer order confusion
- Solved: Repeated practice with both pointers
- Result: Can write delete() perfectly now

3. Typos in method names
- Pattern: "inoder", "recusive", missing self.
- Solution: Slow down, double-check

4. Missing return statements
- Pattern: Forgetting return after special cases
- Solution: Always check control flow

5. Library System bugs
- Small issues (wrong variable, missing str)
- Normal for independent work
- Will fix tomorrow

All challenges overcome through practice and persistence!

- - -

Roadmap Status:

AHEAD OF SCHEDULE! 🚀
Current: Day 18 (Oct 26)
Original plan: Should be finishing Week 1-2 (Fundamentals)
Actual progress: Week 5-6 (Data Structures) - deep practice
Ahead by: ~2-3 weeks

Data Structures Progress:
1. ✅ Stacks (Day 13) - MASTERED
2. ✅ Queues (Day 13) - MASTERED
3. ✅ Singly Linked Lists (Day 14) - MASTERED
4. ✅ Doubly Linked Lists (Day 14) - MASTERED TODAY
5. ✅ Binary Search Trees (Day 16) - MASTERED TODAY
6. ⬜ Hash Tables (next)
7. ⬜ Graphs (after Hash Tables)

5 out of 7 data structures complete and SOLID!

- - -

Updated Learning Strategy Working:

Daily Routine (Implemented Today):

Morning (30 min):
1. ✅ Typing practice (15 min) - 32.7 WPM
2. ✅ Mini "Wax On Wax Off" (15 min) - Identified weak areas

Learning (7-8 hours):
1. ✅ Targeted practice on weak areas (BST, DLL)
2. ✅ Application project (Product Comparison)
3. ✅ Independent project (Library System)

Result: Weak areas became strong areas in one day!

- - -

Tomorrow's Goals (Day 19 - Oct 27):

Morning:
- Typing practice
- Mini warm-up (last 3 days)

Main Session:
- Finish Library Book Tracker
- Add str method
- Fix bugs
- Add menu system
- Add remaining features
- Test thoroughly

If Time:
- Start Hash Tables (6th data structure)
- Or build another application project

- - -

Reflections:

Today was incredibly productive! The targeted practice session was exactly what I needed. Going from "BST makes me go blank" to "mastered all 7 BST methods" in one session proves the power of focused, repetitive practice.

The 22-exercise session was intense but effective. Writing each method twice from memory built solid muscle memory. The mistakes I made (typos, missing self., wrong checks) were caught immediately and corrected, which reinforced the right patterns.

The Product Comparison Tool showed me how BST naturally provides sorted data. Seeing the prices display in order (699.99, 799.99, 899.99...) made the value of BST concrete. The combination of BST and Dictionary leveraged the strengths of both structures.

Starting the Library System independently was a big confidence builder. Using the problem-solving framework, I asked the right questions and gathered complete requirements before coding. The design came naturally - Book class for data, Library class for operations, Dictionary for fast lookup.

The small bugs in the Library System (wrong variable in error message, missing str) are normal for independent work. The important thing is that the core logic is solid and all edge cases are handled. I'll fix the bugs tomorrow and add the remaining features.

The morning warm-up routine is working perfectly. It identified my weak areas (BST, DLL) immediately, which let me focus my practice where it was needed most. This is much more efficient than practicing everything equally.

No regression from the 2-day church camp break! My typing speed held steady at 32.7 WPM, and the structures I had mastered (Stack, Queue, Singly LL) were still solid. This shows the retention strategy is working.

Ready to finish the Library System tomorrow and possibly start Hash Tables!

- - -

Personal Notes:
- Typing: 32.7 WPM, 95.49% accuracy (consistent!)
- Weak keys: 'a' and 'r' improving with Keybr focus
- Church camp break didn't hurt progress
- Targeted practice is incredibly effective
- BST confidence fully restored
- Can build systems independently now
- Problem-solving framework guides the process
- Small bugs are normal and fixable
- Retention strategy working perfectly

- - -

Resources Used:
- Morning warm-up routine
- Targeted "Wax On Wax Off" (22 exercises)
- Problem-solving framework
- Application projects (Product Comparison)
- Independent project (Library System)
- Requirements gathering practice
- System design practice

- - -

Next Session Preview:
- Finish Library Book Tracker
- Add menu system and remaining features
- Possibly start Hash Tables
- Continue retention-focused strategy

- - -

Total Days Completed: 18/60 (Phase 1)
Progress: Ahead of schedule ✓
Confidence Level: Very High 💪
Data Structures: 5/7 mastered (2 SOLID today!)
Independent Building: Confidence high ✓
Retention Strategy: Working perfectly ✓

- - -

End of Day 18 Summary