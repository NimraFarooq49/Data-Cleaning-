import pandas as pd
from cleaner import LoadData, DataCleaner, EDAAnalysis
from exporter import ExportData
from model import ModelTraining

try:

    # Load Data
    loader = LoadData("input/train.csv")
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

export.save_csv("output/train_cleaned.csv")
export.save_json("output/train_cleaned.json")

print("\nCleaned dataset exported successfully!")


print("\nSelect Model")
print("1. Logistic Regression")
print("2. Decision Tree")
print("3. Random Forest")
print("4. Linear Regression")

choice = int(input("Enter your choice: "))

trainer = ModelTraining(choice)
trainer.load_data()