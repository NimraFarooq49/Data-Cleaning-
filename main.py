from cleaner import LoadData, DataCleaner, EDAanalysis
from exporter import ExportData


# Load Data
loader = LoadData("input/data.csv")
df = loader.load_data()


# EDA
eda = EDAanalysis(df)

print(eda.preview())
print("Shape:", eda.shape())
print("Columns:", eda.columns())

eda.info()


# Cleaning
cleaner = DataCleaner(df)

print("Missing Values:\n")
print(cleaner.missing_value())

df = cleaner.remove_duplicate()
df = cleaner.fill_missing()
df = cleaner.remove_whitespace()
df = cleaner.clean_invalid_email()

print("\nCleaning Done")

cleaner = DataCleaner(df)

print("\nMissing Values:\n")
print(cleaner.missing_value())

print("\nFirst 5 Rows After Cleaning:")
print(df.head())


# Export Cleaned Data
export = ExportData(df)

export.save_data()
export.save_json()

print("\nCleaned dataset exported successfully!")