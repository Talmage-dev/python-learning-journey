"""Comprehensive test suite for temperature converter."""

import pytest
from exercises.temp_converter import(celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin, kelvin_to_fahrenheit, convert_temperature)

class TestBasicConversions:
    """Test individual conversion functions."""

    def test_celsius_to_fahrenheit(self):
        """Test C to F conversion."""
        assert celsius_to_fahrenheit(0) == 32
        assert celsius_to_fahrenheit(100) == 212
        assert celsius_to_fahrenheit(-40) == -40
        assert abs(celsius_to_fahrenheit(37) - 98.6) < 0.1

    def test_fahrenheit_to_celsius(self):
        """Test F to C conversion."""
        assert fahrenheit_to_celsius(32) == 0
        assert fahrenheit_to_celsius(212) == 100
        assert fahrenheit_to_celsius(-40) == -40

    def test_celsius_to_kelvin(self):
        """Test C to K conversion."""
        assert celsius_to_kelvin(0) == 273.15
        assert celsius_to_kelvin(-273.15) == 0
        assert celsius_to_kelvin(100) == 373.15

    def test_kelvin_to_celsius(self):
        """Test K to C conversion."""
        assert kelvin_to_celsius(273.15) == 0
        assert kelvin_to_celsius(0) == -273.15
        assert kelvin_to_celsius(373.15) == 100

    def test_fahrenheit_to_kelvin(self):
        """Tesk F to K conversion."""
        assert abs(fahrenheit_to_kelvin(32) - 273.15) < 0.01
        assert abs(fahrenheit_to_kelvin(212) - 373.15) < 0.01

    def test_kelvin_to_fahrenheit(self):
        """Test K to F conversion."""
        assert abs(kelvin_to_fahrenheit(273.15) - 32) < 0.01
        assert abs(kelvin_to_fahrenheit(373.15) - 212) < 0.01

class TestConvertTemperature:
    """Test the main convert_temperature function."""

    def test_same_unit_conversion(self):
        """Test conversion to same unit returns original value."""
        assert convert_temperature(100, 'C', 'C') == 100
        assert convert_temperature(100, 'F', 'F') == 100
        assert convert_temperature(100, 'K', 'K') == 100

    def test_celsius_conversions(self):
        """Test conversions from Celsius."""
        assert convert_temperature(0, 'C', 'F') == 32
        assert convert_temperature(100, 'C', 'F') == 212
        assert convert_temperature(0, 'C', 'K') == 273.15
        assert  convert_temperature(100, 'C', 'K') == 373.15

    def test_fahrenheit_conversions(self):
        """Test conversions from Fahrenheit."""
        assert convert_temperature(32, 'F', 'C') == 0
        assert convert_temperature(212, 'F', 'C') == 100
        assert abs(convert_temperature(32, 'F', 'K') - 273.15) < 0.01

    def test_kelvin_conversions(self):
        """Test conversions from Kelvin."""
        assert kelvin_to_celsius(273.15) == 0
        assert abs(convert_temperature(273.15, 'K', 'F') - 32) < 0.01

    def test_case_insensitive(self):
        """Test that unit inputs are case-insensitive."""
        assert convert_temperature(0, 'c', 'f') == 32
        assert convert_temperature(0, 'C', 'f') == 32
        assert convert_temperature(0, 'c', 'F') == 32

    def test_invalid_source_unit(self):
        """Test that invalid source unit raises ValueError."""
        with pytest.raises(ValueError, match="Invalid source unit"):
            convert_temperature(100, 'X', 'C')

    def test_invalid_target_unit(self):
        """Test that invalid target unit raises ValueError."""
        with pytest.raises(ValueError, match="Invalid target unit"):
            convert_temperature(100, 'C', 'Z')

    def test_both_invalid_units(self):
        """Test that both invalid units raise ValueError."""
        with pytest.raises(ValueError):
            convert_temperature(100, 'X', 'Y')

class  TestEdgeCases:
    """Test edge cases and special values."""

    def test_absolute_zero(self):
        """Test absolute zero conversions."""
        assert celsius_to_kelvin(-273.15) == 0
        assert abs(celsius_to_fahrenheit(-273.15) - (-459.67)) < 0.01

    def test_negative_temperatures(self):
        """Test negative temperature conversions."""
        assert celsius_to_fahrenheit(-40) == -40 # Special point
        assert abs(celsius_to_kelvin(-100) - 173.15) < 0.01

    def test_large_values(self):
        """Test with large temperature conversions."""
        assert celsius_to_fahrenheit(1000) == 1832
        assert celsius_to_kelvin(1000) == 1273.15

# Parametrized tests for common conversions
@pytest.mark.parametrize("celsius,fahrenheit",[(0,32),(100,212),(-40,-40),(37,98.6),(-273.15,-459.67),])
def test_celsius_fahrenheit_pairs(celsius, fahrenheit):
    """Test common C/F conversion pairs."""
    assert abs(celsius_to_fahrenheit(celsius) - fahrenheit) < 0.01
    assert abs(fahrenheit_to_celsius(fahrenheit) - celsius) < 0.01

@pytest.mark.parametrize("celsius,kelvin",[(0,273.15),(100,373.15),(-273.15,0),(27,300.15),])
def test_celsius_kelvin_pairs(celsius, kelvin):
    """Test common C/K conversion pairs."""
    assert abs(celsius_to_kelvin(celsius) - kelvin) < 0.01
    assert abs(kelvin_to_celsius(kelvin) - celsius) < 0.01