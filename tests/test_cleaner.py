import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from cleaner import LoadData, DataCleaner

# Load Data
loader = LoadData("input/data.csv")
df = loader.load_data()

# Clean Data
cleaner = DataCleaner(df)

df = cleaner.remove_duplicate()
df = cleaner.fill_missing()
df = cleaner.remove_whitespace()
df = cleaner.clean_invalid_email()

# Check Missing Values
assert cleaner.missing_value().sum() == 0

print("All tests passed successfully!")