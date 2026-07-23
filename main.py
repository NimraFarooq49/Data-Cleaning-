import pandas as pd
from cleaner import LoadData, DataCleaner, EDAAnalysis
from exporter import ExportData
from model import ModelTraining

try:

    # Load Data
    # loader = LoadData("input/train.csv")
    # loader = LoadData("input/test.csv")
    # loader = LoadData("input/Student_Performance_Dataset.csv")
    loader = LoadData("input/energy_efficiency.csv")
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

    print("\nBefore Removing Outliers")
    cleaner.visualize_outliers("Before Outlier Removal")

    df = cleaner.handle_outliers()

    cleaner.df = df

    print("\nAfter Removing Outliers")
    cleaner.visualize_outliers("After Outlier Removal")

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

print("\nCorrelation Heatmap:")
eda.correlation_heatmap()


# Export Cleaned Data
export = ExportData(df)

# export.save_csv("output/train_cleaned.csv")
# export.save_json("output/train_cleaned.json")
# export.save_csv("output/test_cleaned.csv")
# export.save_json("output/test_cleaned.json")
# export.save_csv("output/student_performance_cleaned.csv")
# export.save_json("output/student_performance_cleaned.json")
export.save_csv("output/energy_efficiency_cleaned.csv")
export.save_json("output/energy_efficiency_cleaned.json")

print("\nCleaned dataset exported successfully!")


# Model Training
model = ModelTraining()
model.train()
