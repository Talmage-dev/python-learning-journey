# Day 3: Lists, Dictionaries & Word Frequency

Date: 10/10/2025
Time: 2 hours
Phase: Python Week 1, Day 3

---

## 🎯 Goals Achieved

✅ Mastered list operations and comprehensions 
✅ Learned dictionary methods and patterns 
✅ Built word frequency counter 
✅ Wrote 30+ comprehensive tests 
✅ Used regex for text processing 
✅ Applied testing framework from this morning

---

## 📚 What I Learned

### Lists
- **Indexing:** `list[0]` (first), `list[-1]` (last)
- **Slicing:** `list[1:3]` (elements 1-2)
- **Methods:** `append()`, `insert()`, `remove()`, `pop()`
- **Comprehensions:** `[x**2 for x in range(5)]`
- **Useful:** `len()`, `sum()`, `max()`, `min()`, `count()`

### Dictionaries
- **Key-value pairs:** `{"name": "Alice", "age": 25}`
- **Access:** `dict["key"]` or `dict.get("key", default)`
- **Methods:** `.keys()`, `.values()`, `.items()`
- **Iteration:** `for key, value in dict.items():`
- **Counting pattern:** `dict[key] = dict.get(key, 0) + 1`

### Text Processing
- **Regex:** `re.findall(r'\w+', text)` extracts words
- **String methods:** `.lower()`, `.split()`, `.join()`
- **Type hints:** `Dict[str, int]`, `List[str]`

### Testing Insights (Applied from this morning!)
- ✅ Happy path: basic functionality
- ✅ Edge cases: empty, single item, whitespace
- ✅ Error cases: invalid input
- ✅ Special values: case sensitivity, punctuation
- ✅ Consistency: total counts match word list
- ✅ Integration: full pipeline tests

---

## 💻 What I Built
Built a word frequency counter. Counts how often each word appear in text.

### Project Structure
exercises/ word_frequency.py (150 lines)
tokenize(), count_words(), top_n_words(),
analyze_text(), main()

tests/ test_word_frequency.py (~200 lines, 30+ tests)

### Test Results
Total tests:32
passed: 32
failed: 0
coverage: 100%

---

## 🐛 Challenges & Solutions

### Challenge 1: Punctuation Handling
**Problem:** Initially used `.split()` which kept punctuation  
**Solution:** Used `re.findall(r'\w+', text)` to extract only word characters

### Challenge 2: Case Sensitivity
**Problem:** "Hello" and "hello" counted separately  
**Solution:** Convert to lowercase in `tokenize()`

### Challenge 3: Sorting with Ties
**Problem:** Words with same count had random order  
**Solution:** Used `key=lambda item: (-item[1], item[0])` for count desc, then alphabetical

---

## 💡 Key Insights

1. **Dictionaries are perfect for counting** - `.get(key, 0)` pattern is elegant
2. **List comprehensions are powerful** - more readable than loops for simple transformations
3. **Regex is useful** - `\w+` pattern handles punctuation cleanly
4. **Type hints improve clarity** - easier to understand function signatures
5. **Testing framework works!** - Asking the right questions led to comprehensive tests

---

## 🎓 Patterns Learned

### Counting Pattern

''' python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1

### Sorting by Multiple Criteria

sorted(items, key=lambda x: (-x[1], x[0]))  # Desc by count, asc by name

### List Comprehension with Filter

evens = [x for x in range(10) if x % 2 == 0]

### Dictionary Iteration

for key, value in my_dict.items():
    print(f"{key}: {value}")
    
### Commands used

# Run program
python exercises/word_frequency.py

# Run all tests
pytest tests/test_word_frequency.py -v

# Run specific test class
pytest tests/test_word_frequency.py::TestCountWords -v

# Coverage
pytest tests/test_word_frequency.py --cov=exercises.word_frequency

# Run tests matching pattern
pytest -k "count" -v
