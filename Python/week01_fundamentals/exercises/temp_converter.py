""" Temperature conversion utilities. Supports conversion between Celsius (C), Fahrenheit (F), and Kelvin (K). """

# Temp formulas:
# C to F: (C x 9/5) + 32
# F to C: (F - 32) x 5/9
# C to K: C + 273.15
# K to C: K - 273.15

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit. Formula: F = (C x 9/5)+32"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius. Formula: C = (F - 32) x 5/9"""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin. Formula: C + 273.15"""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius. Formula: K - 273.15"""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin (via Celsius)."""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit(via Celsius)."""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def convert_temperature(value, from_unit, to_unit):
    """
    Convert Temperature between any two units.

    Args:
        value (float): Temperature value to convert from_unit (str):
        Source unit ('C', 'F', or 'K') to_unit (str): Target unit ('C', 'F', or 'K')

    Returns:
        float: Converted temperature value

    Raises:
        ValueError: If units are invalid

    Examples:
        >>>convert_temperature(0, 'C', 'F')
        32.0
        >>>convert_temperature(100, 'C', 'K')
        373.15
    """

    # Normalize to uppercase
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Same unit - no conversion needed
    if from_unit == to_unit:
        return value
    
    # Convert to Celsius first (as intermediate)
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == 'K':
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Invalid source unit: {from_unit}. Use C, F, or K.")
    
    # Convert from Celsius to target unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return celsius_to_fahrenheit(celsius)
    elif to_unit == 'K':
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Invalid target unit: {to_unit}. Use C, F, or K.")
    
def main():
        """Interactive temperature converter CLI."""
        print("=" * 40)
        print(" Temperature Converter")
        print("=" * 40)
        print("Supported units:")
        print(" C - Celsius")
        print(" F - Fahrenheit")
        print(" K - Kelvin")
        print()

        try:
            # Get input
            value = float(input("Enter temperature value:"))
            from_unit = input("From unit (C/F/K): ").strip()
            to_unit = input("To unit (C/F/K): ").strip()

            # Convert
            result = convert_temperature(value, from_unit, to_unit)

            # Display result
            print()
            print(f"Result: {value}°{from_unit.upper()} = {result:.2f}°{to_unit.upper()}")

        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nUnexpexted error: {e}")

if __name__ == "__main__":
    main()