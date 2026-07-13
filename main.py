import pandas as pd
from cleaner import LoadData, DataCleaner, EDAAnalysis
from exporter import ExportData

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
eda = EDAAnalysis(df)

print("\nPreview:")
print(eda.preview())

print("\nShape:")
print(eda.shape())

print("\nColumns:")
print(eda.columns())

print("\nInfo:")
eda.info()

print("\nSummary:")
print(eda.summary())


# Export Cleaned Data
export = ExportData(df)

export.save_csv("output/cleaned_data.csv")
export.save_json("output/cleaned_data.json")

print("\nCleaned dataset exported successfully!")
