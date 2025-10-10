""" Word frequency counter. Counts how often each word appears in text. """

import re
from typing import Dict, List, Tuple

def clean_text(text:str) -> str:
    """
    Clean text by convertin to lowercase.
    
    Args:
        text: Input text 
    
    Returns:
        Cleaned text in lowercase
        
    """

    return text.lower()

def tokenize(text: str) -> List[str]:
    """
    Split text into words, removing punctuation.
    
    Args:
        text: Input text
    
    Returns:
        List of words (lowercase, no punctuation)
    
    Examples:
    >>> tokenize("Hello, world!")
    ['hello', 'world']
    >>> tokenize("ont two three")
    ['one', 'two', 'three']

    """
    # Remove punctuation and split on whitespace
    # \w+ matches word characters (letters, digits, underscore)
    words = re.findall(r'\w+', text.lower())
    return words

def count_words(text:str) -> Dict[str, int]:
    """
    Count frequency of each word in text.
    
    Args:
        text: Input text
        
    Returns:
        Dictioary mapping words to their counts
        
    Examples:
        >>>count_words("hello world hello")
        {'hello': 2, 'world': 1}
        
    """

    words = tokenize(text)
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

def top_n_words(word_count: Dict[str,int], n: int = 10) -> List[Tuple[str, int]]:
    """
    Get the top N most frequent words.
    
    Args:
        word_count: Dictionary of word frequencies
        n: Number of top words to return
        
    Returns:
        List of (word, count) tuples, sorted by count (descending)
    
    Examples:
        >>>counts = {'apple': 5, 'banana': 3, 'cherry': 8}
        >>>top_n_words(counts, 2)
        [('cherry', 8), ('apple', 5)]
    
    """

    # Sort by count (descending), then by word (ascending) for ties
    sorted_words = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))

    return sorted_words[:n]

def analyze_text(text: str, top_n: int = 10) -> None:
    """
    Analyze text and print word frequency statistics.
    
    Args:
        text: Input text to analyze
        top_n: Number of top words to display

    """

    words = tokenize(text)
    word_count = count_words(text)
    top_words = top_n_words(word_count, top_n)

    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(word_count)}")
    print(f"\nTop {top_n} most frequent words:")
    print("-" * 30)

    for i, (word, count) in enumerate(top_words, 1):
        print(f"{i:2}. {word:15} {count:5} times")

def read_file(filepath: str) -> str:
    """
    Read text from a file.
    
    Args:
        filepath: Path to text file
        
    Returns:
        FileNotFoundError: If file doesn't exist
    
    """

    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    
def main():
    """Interactive word frequency analyzer."""
    print("=" * 50)
    print("    Word Frequency Analyzer")
    print("=" * 50)
    print()

    # Option 1: Analyze sample text
    sample_text = """Python is an amazing programming language. Python is easy to learn and Python is powerful.
    many developers love Python because Python is versatile."""

    print("Analzing sample text...")
    print()
    analyze_text(sample_text, top_n=5)

    # Option 2: Analyze user input
    print("\n" + "=" * 50)
    print("\nEnter your own text (or press Enter to skip):")
    user_text = input("> ")

    if user_text.strip():
        print()
        analyze_text(user_text, top_n=5)

if __name__ == "__main__":
    main()