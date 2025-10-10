"""
Comprehensive tests for word frequency counter.

TEST CATEGORIES GUIDE:
- 🟢 HAPPY PATH: Normal, expected usage
- 🔵 EDGE CASES: Boundaries, empty, single items
- 🔴 ERROR CASES: Invalid input, exceptions
- 🟡 SPECIAL VALUES: Domain-specific cases
- 🟣 SYMMETRY: Reversibility checks
- 🟠 CONSISTENCY: Related operations agree
"""

import pytest
from exercises.word_frequency import (
    tokenize,
    count_words,
    top_n_words,
    clean_text
)


# ============================================================================
# TOKENIZE TESTS
# ============================================================================

class TestTokenize:
    """Test text tokenization."""
    
    # 🟢 HAPPY PATH
    def test_simple_text(self):
        """🟢 HAPPY PATH: Basic tokenization with normal input."""
        assert tokenize("hello world") == ["hello", "world"]
    
    # 🟡 SPECIAL VALUES
    def test_punctuation_removal(self):
        """🟡 SPECIAL VALUES: Punctuation should be removed."""
        assert tokenize("Hello, world!") == ["hello", "world"]
        assert tokenize("one-two-three") == ["one", "two", "three"]
    
    def test_multiple_spaces(self):
        """🟡 SPECIAL VALUES: Multiple spaces should be handled."""
        assert tokenize("hello    world") == ["hello", "world"]
    
    # 🔵 EDGE CASES
    def test_empty_string(self):
        """🔵 EDGE CASE: Empty string should return empty list."""
        assert tokenize("") == []
    
    def test_whitespace_only(self):
        """🔵 EDGE CASE: Whitespace-only string should return empty list."""
        assert tokenize("   \n\t  ") == []
    
    # 🟡 SPECIAL VALUES
    def test_case_normalization(self):
        """🟡 SPECIAL VALUES: Text should be normalized to lowercase."""
        assert tokenize("HELLO World") == ["hello", "world"]
    
    def test_numbers(self):
        """🟡 SPECIAL VALUES: Numbers should be included as words."""
        assert tokenize("test123 456") == ["test123", "456"]
    
    def test_special_characters(self):
        """🟡 SPECIAL VALUES: Various punctuation marks should be removed."""
        text = "Hello! How are you? I'm fine, thanks."
        result = tokenize(text)
        assert "hello" in result
        assert "how" in result
        assert "i" in result
        assert "m" in result
        assert "fine" in result


# ============================================================================
# COUNT WORDS TESTS
# ============================================================================

class TestCountWords:
    """Test word counting functionality."""
    
    # 🟢 HAPPY PATH
    def test_simple_count(self):
        """🟢 HAPPY PATH: Basic word counting with unique words."""
        result = count_words("hello world")
        assert result == {"hello": 1, "world": 1}
    
    def test_repeated_words(self):
        """🟢 HAPPY PATH: Counting repeated words."""
        result = count_words("hello hello world")
        assert result == {"hello": 2, "world": 1}
    
    # 🟡 SPECIAL VALUES
    def test_case_insensitive(self):
        """🟡 SPECIAL VALUES: Counting should be case-insensitive."""
        result = count_words("Hello HELLO hello")
        assert result == {"hello": 3}
    
    def test_punctuation_ignored(self):
        """🟡 SPECIAL VALUES: Punctuation shouldn't affect counting."""
        result = count_words("hello, hello! hello?")
        assert result == {"hello": 3}
    
    # 🔵 EDGE CASES
    def test_empty_string(self):
        """🔵 EDGE CASE: Empty string should return empty dict."""
        assert count_words("") == {}
    
    def test_single_word(self):
        """🔵 EDGE CASE: Single word should work correctly."""
        assert count_words("hello") == {"hello": 1}
    
    # 🟢 HAPPY PATH
    def test_multiple_occurrences(self):
        """🟢 HAPPY PATH: Text with varying word frequencies."""
        text = "apple banana apple cherry banana apple"
        result = count_words(text)
        assert result["apple"] == 3
        assert result["banana"] == 2
        assert result["cherry"] == 1
    
    def test_real_sentence(self):
        """🟢 HAPPY PATH: Real sentence with repeated words."""
        text = "The quick brown fox jumps over the lazy dog"
        result = count_words(text)
        assert result["the"] == 2
        assert result["quick"] == 1
        assert len(result) == 8  # 8 unique words


# ============================================================================
# TOP N WORDS TESTS
# ============================================================================

class TestTopNWords:
    """Test top N words functionality."""
    
    # 🟢 HAPPY PATH
    def test_top_n_basic(self):
        """🟢 HAPPY PATH: Getting top N most frequent words."""
        counts = {"apple": 5, "banana": 3, "cherry": 8}
        result = top_n_words(counts, 2)
        assert result == [("cherry", 8), ("apple", 5)]
    
    # 🔵 EDGE CASES
    def test_top_n_all(self):
        """🔵 EDGE CASE: N larger than dict size should return all."""
        counts = {"a": 3, "b": 1, "c": 2}
        result = top_n_words(counts, 10)
        assert len(result) == 3
        assert result[0] == ("a", 3)
    
    # 🟠 CONSISTENCY
    def test_top_n_order(self):
        """🟠 CONSISTENCY: Results should be sorted by count descending."""
        counts = {"a": 1, "b": 5, "c": 3, "d": 4}
        result = top_n_words(counts, 4)
        assert result[0][1] >= result[1][1]  # First >= second
        assert result[1][1] >= result[2][1]  # Second >= third
    
    # 🟡 SPECIAL VALUES
    def test_top_n_ties(self):
        """🟡 SPECIAL VALUES: Tied counts should be alphabetically ordered."""
        counts = {"zebra": 5, "apple": 5, "banana": 5}
        result = top_n_words(counts, 3)
        # With same count, should be alphabetical
        words = [word for word, count in result]
        assert words == ["apple", "banana", "zebra"]
    
    # 🔵 EDGE CASES
    def test_empty_dict(self):
        """🔵 EDGE CASE: Empty dictionary should return empty list."""
        assert top_n_words({}, 5) == []
    
    def test_top_1(self):
        """🔵 EDGE CASE: Getting only the single top word."""
        counts = {"a": 1, "b": 5, "c": 3}
        result = top_n_words(counts, 1)
        assert result == [("b", 5)]


# ============================================================================
# CLEAN TEXT TESTS
# ============================================================================

class TestCleanText:
    """Test text cleaning."""
    
    # 🟢 HAPPY PATH
    def test_lowercase_conversion(self):
        """🟢 HAPPY PATH: Convert mixed case to lowercase."""
        assert clean_text("HELLO World") == "hello world"
    
    # 🔵 EDGE CASES
    def test_already_lowercase(self):
        """🔵 EDGE CASE: Already lowercase text should be unchanged."""
        assert clean_text("hello world") == "hello world"
    
    def test_empty_string(self):
        """🔵 EDGE CASE: Empty string should remain empty."""
        assert clean_text("") == ""


# ============================================================================
# INTEGRATION TESTS
# ============================================================================

class TestIntegration:
    """Integration tests combining multiple functions."""
    
    # 🟢 HAPPY PATH (Integration)
    def test_full_pipeline(self):
        """🟢 HAPPY PATH: Complete analysis pipeline end-to-end."""
        text = "Python is great. Python is powerful. I love Python!"
        
        # Count words
        counts = count_words(text)
        assert counts["python"] == 3
        assert counts["is"] == 2
        
        # Get top words
        top = top_n_words(counts, 2)
        assert top[0] == ("python", 3)
        assert top[1] == ("is", 2)
    
    # 🟠 CONSISTENCY
    def test_consistency(self):
        """🟠 CONSISTENCY: Total counts should match word list length."""
        text = "one two three one two one"
        words = tokenize(text)
        counts = count_words(text)
        
        # Sum of all counts should equal number of words
        assert sum(counts.values()) == len(words)
    
    def test_unique_words(self):
        """🟠 CONSISTENCY: Unique word count should match dict size."""
        text = "apple banana apple cherry"
        counts = count_words(text)
        assert len(counts) == 3  # 3 unique words


# ============================================================================
# PARAMETRIZED TESTS
# ============================================================================

# 🔵 EDGE CASES (Parametrized)
@pytest.mark.parametrize("text,expected_count", [
    ("hello", 1),                    # Single word
    ("hello hello", 1),              # Repeated word (1 unique)
    ("hello world hello", 2),        # 2 unique words
    ("", 0),                         # Empty string
])
def test_unique_word_count(text, expected_count):
    """🔵 EDGE CASES: Various inputs for unique word counting."""
    counts = count_words(text)
    assert len(counts) == expected_count


# 🟢 HAPPY PATH (Parametrized)
@pytest.mark.parametrize("text,word,expected", [
    ("hello world", "hello", 1),           # Single occurrence
    ("hello hello world", "hello", 2),     # Multiple occurrences
    ("Hello HELLO hello", "hello", 3),     # Case-insensitive
])
def test_specific_word_count(text, word, expected):
    """🟢 HAPPY PATH: Counting specific words in various texts."""
    counts = count_words(text)
    assert counts.get(word, 0) == expected


# ============================================================================
# SUMMARY OF TEST CATEGORIES
# ============================================================================
"""
TEST CATEGORY BREAKDOWN:

🟢 HAPPY PATH (10 tests):
   - Normal, expected usage
   - Basic functionality with typical inputs
   
🔵 EDGE CASES (11 tests):
   - Empty strings, single items
   - Boundary conditions
   - N larger than available items
   
🔴 ERROR CASES (0 tests):
   - None needed for current implementation
   - Could add: None input, invalid types
   
🟡 SPECIAL VALUES (8 tests):
   - Punctuation handling
   - Case sensitivity
   - Whitespace handling
   - Tied counts
   
🟣 SYMMETRY (0 tests):
   - Not applicable to this problem
   - (Would be relevant for conversions)
   
🟠 CONSISTENCY (3 tests):
   - Total counts match word list
   - Sorting order maintained
   - Unique counts match dict size

TOTAL: 32 tests
"""