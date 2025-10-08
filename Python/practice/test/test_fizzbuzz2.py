import pytest

def fizzbuzz(n):
    """Generator that yields FizzBuzz sequence from 1 to n."""
    for i in range(1, n + 1):
        if i % 15 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)


class TestFizzBuzz:
    """Test suite for fizzbuzz generator."""
    
    def test_returns_number_for_non_multiples(self):
        """Test that non-multiples of 3 or 5 return the number as string."""
        result = list(fizzbuzz(2))
        assert result == ["1", "2"]
    
    def test_returns_fizz_for_multiples_of_3(self):
        """Test that multiples of 3 (but not 5) return 'Fizz'."""
        result = list(fizzbuzz(9))
        assert result[2] == "Fizz"  # 3
        assert result[5] == "Fizz"  # 6
        assert result[8] == "Fizz"  # 9
    
    def test_returns_buzz_for_multiples_of_5(self):
        """Test that multiples of 5 (but not 3) return 'Buzz'."""
        result = list(fizzbuzz(10))
        assert result[4] == "Buzz"  # 5
        assert result[9] == "Buzz"  # 10
    
    def test_returns_fizzbuzz_for_multiples_of_15(self):
        """Test that multiples of both 3 and 5 return 'FizzBuzz'."""
        result = list(fizzbuzz(30))
        assert result[14] == "FizzBuzz"  # 15
        assert result[29] == "FizzBuzz"  # 30
    
    def test_first_15_numbers(self):
        """Test the complete sequence for first 15 numbers."""
        expected = [
            "1", "2", "Fizz", "4", "Buzz",
            "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        result = list(fizzbuzz(15))
        assert result == expected
    
    def test_empty_sequence_for_zero(self):
        """Test that n=0 produces empty sequence."""
        result = list(fizzbuzz(0))
        assert result == []
    
    def test_single_number(self):
        """Test with n=1."""
        result = list(fizzbuzz(1))
        assert result == ["1"]
    
    def test_generator_behavior(self):
        """Test that fizzbuzz returns a generator."""
        gen = fizzbuzz(5)
        assert next(gen) == "1"
        assert next(gen) == "2"
        assert next(gen) == "Fizz"
        assert next(gen) == "4"
        assert next(gen) == "Buzz"
        
        # Should raise StopIteration when exhausted
        with pytest.raises(StopIteration):
            next(gen)
    
    @pytest.mark.parametrize("n,index,expected", [
        (3, 2, "Fizz"),
        (5, 4, "Buzz"),
        (15, 14, "FizzBuzz"),
        (7, 6, "7"),
    ])
    def test_specific_positions(self, n, index, expected):
        """Parametrized test for specific positions."""
        result = list(fizzbuzz(n))
        assert result[index] == expected


if __name__ == "__main__":
    # Run tests with: pytest test_fizzbuzz.py -v
    pytest.main([__file__, "-v"])