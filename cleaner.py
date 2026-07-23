import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class LoadData:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.filepath)
            return self.df

        except Exception as e:

            print(f"Error loading file: {e}")
            return None


class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()

    def remove_duplicates(self):
        try:

            before = len(self.df)
            self.df = self.df.drop_duplicates().reset_index(drop=True)
            after = len(self.df)
            print(f"Duplicate rows removed: {before - after}")
            return self.df

        except Exception as e:
            print(f"Error removing duplicates:{e}")

    def check_missing_values(self):
        try:
            missing = self.df.isnull().sum()
            print("Missing Values:")
            print(missing)
            return self.df

        except Exception as e:
            print(f"Error checking missing values: {e}")

    def fill_missing_values(self):
        try:
            for column in self.df.columns:
                if self.df[column].isnull().all():
                    continue
                if pd.api.types.is_numeric_dtype(self.df[column]):
                    self.df[column] = self.df[column].fillna(self.df[column].median())

                else:
                    mode_value = self.df[column].mode()

                    if not mode_value.empty:
                        self.df[column] = self.df[column].fillna(mode_value[0])

            print("Missing values filled successfully.")
            return self.df

        except Exception as e:
            print(f"Error filling missing values: {e}")

    def remove_whitespaces(self):
        try:

            for column in self.df.columns:
                if self.df[column].dtype == "object":
                    self.df[column] = self.df[column].str.strip()
            print("whitespaces removed successfully.")
            return self.df

        except Exception as e:
            print(f"Error removing whitespaces: {e}")

    def clean_email(self):
        try:

            for column in self.df.columns:
                if "email" in column.lower():
                    self.df[column] = (
                        self.df[column]
                        .astype(str)
                        .str.strip()
                        .str.lower()
                        .str.replace(" ", "")
                    )

                    self.df = self.df[
                        self.df[column]
                        .astype(str)
                        .str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$")
                    ]
            return self.df

        except Exception as e:
            print(f"Error cleaning email: {e}")

    def handle_outliers(self):
        try:
            print("\n===== Outlier Detection & Handling =====")

            # Automatically select numeric columns
            numeric_columns = self.df.select_dtypes(include="number").columns

            for column in numeric_columns:

                Q1 = self.df[column].quantile(0.25)

                Q3 = self.df[column].quantile(0.75)

                IQR = Q3 - Q1

                lower = Q1 - 1.5 * IQR

                upper = Q3 + 1.5 * IQR
                outliers = self.df[
                    (self.df[column] < lower) | (self.df[column] > upper)
                ]

                print(f"{column}: {len(outliers)} Outliers")
                # Remove outliers
                self.df = self.df[
                    (self.df[column] >= lower) & (self.df[column] <= upper)
                ]

            print("Outliers Handled Successfully!")

            return self.df

        except Exception as e:
            print(f"Error handling outliers: {e}")
            return self.df

    def visualize_outliers(self, title):

        numeric_columns = self.df.select_dtypes(include="number").columns

        plt.figure(figsize=(12, 6))

        self.df[numeric_columns].boxplot()

        plt.title(title)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()


class EDAAnalysis:
    def __init__(self, df):
        self.df = df

    def preview(self):
        return self.df.head()

    def shape(self):
        return self.df.shape

    def columns(self):
        return self.df.columns.tolist()

    def info(self):
        self.df.info()

    def summary(self):
        return self.df.describe(include="all")

    def correlation_heatmap(self):
        plt.figure(figsize=(8, 6))
        sns.heatmap(self.df.corr(numeric_only=True), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()
