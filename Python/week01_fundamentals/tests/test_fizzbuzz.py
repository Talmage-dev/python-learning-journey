import pytest
from exercises.fizzbuzz import fizzbuzz

def test_fizzbuzz_basic():
    """Test basic FizzBuzz sequencw up to 5."""
    result = fizzbuzz(5)
    expected = ["1", "2", "Fizz", "4", "Buzz"]
    assert result == expected

def test_fizzbuzz_fifteen():
    """Test that 15 returns FizzBuzz."""
    result = fizzbuzz(15)
    assert result[14] == "FizzBuzz" # 15th element (index 14)

def test_fizzbuzz_multiples_of_three():
    """Test that multiples of 3 (not5) return Fizz."""
    result = fizzbuzz(15)
    assert result[2] == "Fizz"  #3
    assert result[5] == "Fizz"  #6
    assert result[8] == "Fizz"  #9
    assert result[11] == "Fizz" #12

def test_fizzbuzz_multiples_of_five():
    """Test that multiples of 5 (not3) return Buzz."""
    result = fizzbuzz(15)
    assert result[4] == "Buzz"  #5
    assert result[9] == "Buzz"  #10

def test_fizzbuzz_multiples_of_fifteen():
    """Test that multiples of 15 return FizzBuzz."""
    result = fizzbuzz(30)
    assert result[14] == "FizzBuzz" #15
    assert result[29] == "FizzBuzz" #30

def test_fizzbuzz_regular_numbers():
    """Test that non-multiples return the number as string."""
    result = fizzbuzz(15)
    assert result[0] == "1"
    assert result[1] == "2"
    assert result[3] == "4"
    assert result[6] == "7"

def test_fizzbuzz_length():
    """Test that result has correct length."""
    assert len(fizzbuzz(15)) == 15
    assert len(fizzbuzz(100)) == 100

def test_fizzbuzz_edge_case_onee():
    """Test edge case: n=1."""
    result = fizzbuzz(1)
    assert result == ["1"]

def test_fizzbuzz_edge_case_three():
    """Test edge case: n=3."""
    result = fizzbuzz(3)
    assert result == ["1", "2", "Fizz"]

@pytest.mark.parametrize("n,expected", [
    (3, "Fizz"),
    (5, "Buzz"),
    (15, "FizzBuzz"),
    (7, "7"),
])
def test_fizzbuzz_parametrized(n,expected):
    """Test specific values using parametrization."""
    result = fizzbuzz(n)
    assert result[-1] == expected # Check last element