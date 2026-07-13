import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from cleaner import LoadData, DataCleaner

# Load Data
loader = LoadData("input/data.csv")
df = loader.load_data()

# Clean Data
cleaner = DataCleaner(df)

df = cleaner.remove_duplicates()
df = cleaner.fill_missing_values()
df = cleaner.remove_whitespaces()
df = cleaner.clean_email()

# Test Missing Values
assert df.isnull().sum().sum() == 0

# Test Duplicate Rows
assert df.duplicated().sum() == 0

print("All tests passed successfully!")
