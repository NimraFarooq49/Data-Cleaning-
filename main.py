import pandas as pd
from cleaner import LoadData, DataCleaner

try:

    # Load Data
    loader = LoadData("input/data.csv")
    df = loader.load_data()

    # Cleaning
    cleaner = DataCleaner(df)

    df = cleaner.remove_duplicates()

    print("\nDataset After Removing Duplicates:")
    print(df)

    df = cleaner.check_missing_values()

    df = cleaner.fill_missing_values()
    df = cleaner.check_missing_values()

    df = cleaner.remove_whitespaces()

    print("\nDataset After Removing Whitespaces:")
    print(df)

    df = cleaner.clean_email()
    print("\nDataset After Email Cleaning:")

    print(df)

except FileNotFoundError:
    print("Error: File not found.")

except pd.errors.EmptyDataError:
    print("Error: CSV file is empty.")

except Exception as e:
    print("Error:", e)


# EDA
# eda = EDAanalysis(df)

# print(eda.preview())
# print("Shape:", eda.shape())
# print("Columns:", eda.columns())

# eda.info()


# Cleaning


# print("Missing Values:\n")
# print(cleaner.missing_value())

#  df = cleaner.remove_duplicates()
# df = cleaner.fill_missing()
# df = cleaner.remove_whitespace()
# df = cleaner.clean_invalid_email()

# print("\nCleaning Done")

# cleaner = DataCleaner(df)

# print("\nMissing Values:\n")
# print(cleaner.missing_value())

# print("\nFirst 5 Rows After Cleaning:")
# print(df.head())


# Export Cleaned Data
# export = ExportData(df)

# export.save_data()
# export.save_json()

# print("\nCleaned dataset exported successfully!")
