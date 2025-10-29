""" Day 21: Hash Table Project - Word Frequency Counter """

import sys
sys.path.append('/home/talmage/Desktop/Code/Python/Modules')
from ds_modules import HashTable 

class WordFrequencyCounter:
    def __init__(self):
        self.word_counts = HashTable(size=50)  # Bigger table for more words
    
    # Methods to implement:
    # 1. add_text(text)
    def add_text(self, text):
        words = text.lower().split()            # Split and lower case
        for word in words:
            count = self.word_counts.get(word)  # Get current count
            if count is None:
                count = 0
            self.word_counts.insert(word, count + 1)    # Increment and store

    # 2. get_count(word)
    def get_count(self, word):
        count = self.word_counts.get(word)
        return count

    # 3. display_all()
    def display_all(self):
        self.word_counts.display()

    # 4. most_common()
    def most_common(self):
        max_word = None
        max_count = 0

        for bucket in self.word_counts.table:
            for word, count in bucket:
                if count > max_count:
                    max_count = count
                    max_word = word
        return (max_word, max_count) if max_word else None

    # 5. least_common()
    def least_common(self):
        least_word = None
        least_count = float('inf')      #Inifinty

        for bucket in self.word_counts.table:
            for word, count in bucket:
                if count < least_count:
                    least_count = count
                    least_word = word
        return (least_word, least_count) if least_word else None

# Test
wfc = WordFrequencyCounter()

# Add some text
text1 = "the cat and the dog and the bird"
text2 = "the dog chased the cat and the cat ran away"

wfc.add_text(text1)
wfc.add_text(text2)

print("=== All Word Counts ===")
wfc.display_all()

print("\n=== Individual Word Counts ===")
print(f"'the': {wfc.get_count('the')}")
print(f"'cat': {wfc.get_count('cat')}")
print(f"'dog': {wfc.get_count('dog')}")
print(f"'bird': {wfc.get_count('bird')}")

print("\n=== Most Common Word ===")
most = wfc.most_common()
if most:
    print(f"{most[0]}: {most[1]} times")

print("\n=== Least Common Word ===")
least = wfc.least_common()
if least:
    print(f"{least[0]}: {least[1]} time(s)")
