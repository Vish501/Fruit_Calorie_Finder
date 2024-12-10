# FDA FruitCal Finder
This Python script retrieves calorie information for raw fruits 
from the FDA's Raw Fruits Poster (text version).
(*Source: https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/raw-fruits-poster-text-version-accessible-version*)

**Disclaimer:**

This script is for informational purposes only and should not be considered 
medical or nutritional advice. 

**Usage:**

1. Run the script.
2. Enter the name of the fruit when prompted. 
3. The script will display the number of calories per 100 grams 
   of the specified fruit, if found in the FDA data.

**Note:**

* This script uses the `pandas` and `requests` libraries.
* This script also requries the `lxml` package installed.
* The accuracy of the results depends on the 
  correctness and consistency of the fruit names 
  in the user input and the FDA data source.

**To use this script:**

1. **Install required libraries:**
   ```bash
   pip install pandas requests lxml

2. **Run the script:**
   ```bash
    python fruit_calories.py 
