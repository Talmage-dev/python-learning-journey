""" Exercise Paint Calculator (Day 3 Level) """

# Create Nic's paint calculator program:
# 1) Create a variable surface_area (in square meters) - use any value like 45.5
# 2) Assume 1 litre of paint covers 10 square meters
# 3) Calculate paint_required (litres needed)
# 4) Paint comes in 5-litre tins - calculate how many tins are needed (remember to round UP!)
# 5) Calculate the total litres you'll have after buying the tins
# 6) Calculate how much paint will be left over
# 7) Print a summary with all this information

# Loop exercise:
# 1) Uses a for loop to calculate the total paint needed for 3 boats with different surface areas
# 2) Store the surface areas  in a list: [45.5, 60.0, 32.8]
# 3) For each boat, calculate paint required and tins needed
# 4) Print details for each boat
# 5) At the end, print the total tins needed for all boats

# Functions exercise:
# 1) A function calculate_paint_required(surface_area) that returns litres needed
# 2) A function calculate_tins_needed(paint_required, tin_size=5) that returns number of tins
# 3) a Function print_boat_summary(boat_number, surface_area, paint_required, num_tins) that prints the details
# Then use these functions in your loop to calculate for multiple boats.

# Imports
import math

# Variables
surface_area = [45.5, 60.0, 32.8]
count = 1
total = 0

# Functions
def calculate_paint_required(surface_area, coverage=10):
     """
    Calculate paint required for a given surface area.
    
    Args:
        surface_area (float): Surface area in square meters
        coverage (int): Square meters covered per litre (default: 10)
    
    Returns:
        float: Litres of paint required
        
    """
     paint_required = surface_area / coverage
     return paint_required

def calculate_tins_needed(paint_required, tin_size=5):
     """
    Calculates the number of tins for a required amount of paint.
    
    Args:
        paint_required (float): Paint required 
        tin_size (int): In litres
    
    Returns:
        interger: Number of tins required
        
    """
     num_tins = math.ceil(paint_required / tin_size)
     return num_tins

def print_boat_summary(boat_number, surface_area, paint_required, num_tins, tin_word):
     """
    Prints the details.
    
    Args:
    boat_number (int):
    surface_area (float): Surface area in square meters
    paint_required (float):
    num_tins (int):
    tin_word (string):
        
    """
     print(f"Boat {boat_number} has a surface area of {surface_area} meters squared and requires {paint_required:.2f} litres of paint and {num_tins} {tin_word} of paint.")

# Loop
for boat in surface_area:
    paint_required = calculate_paint_required(boat)
    num_tins = calculate_tins_needed(paint_required)
    total += paint_required
    tin_word = "tin" if num_tins == 1 else "tins"
    print_boat_summary(count, boat, paint_required, num_tins, tin_word)
    count += 1

print(f"To paint all the boats requires {total:.2f} litres of paint, you will need {math.ceil(total / 5)} tins of paint.")

def calculate_fleet_total(surface_areas, coverage=10, tin_size=5):
    """Calculate total paint and tins for entire fleet."""
    total_paint = 0
    total_tins = 0
    
    for area in surface_areas:
        paint = calculate_paint_required(area, coverage)
        tins = calculate_tins_needed(paint, tin_size)
        total_paint += paint
        total_tins += tins
    
    return total_paint, total_tins  # Return multiple values!

# usage
paint, tins = calculate_fleet_total(surface_area)
print(f"Total: {paint:.2f} litres, {tins} tins")

print("Requires 3 tins if you share tins between boats, other wise 4 tins required")

# If leftover paint is more then 2 litres, print "Consider buying smaller tins"
# Otherwise, print "Good paint efficiency!"
#if left_over > 2:
#    print("Consider buying smaller tins")
#else:
#    print("Good paint efficiency!")