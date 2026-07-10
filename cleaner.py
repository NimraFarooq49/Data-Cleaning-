import pandas as pd


class LoadData:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.filepath)
        return self.df


class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()

    def remove_duplicates(self):
        before = len(self.df)

        self.df = self.df.drop_duplicates().reset_index(drop=True)

        after = len(self.df)

        print(f"Duplicate rows removed: {before - after}")

        return self.df

    def check_missing_values(self):
        missing = self.df.isnull().sum()

        print("Missing Values:")
        print(missing)

        return self.df

    def fill_missing_values(self):
        for column in self.df.columns:

            if self.df[column].isnull().all():
                continue
            if pd.api.types.is_numeric_dtype(self.df[column]):
                self.df[column] = self.df[column].fillna(self.df[column].median())
            else:
                self.df[column] = self.df[column].fillna(self.df[column].mode().iloc[0])

        print("Missing values filled successfully.")

        return self.df

    def remove_whitespaces(self):
        for column in self.df.columns:
            if self.df[column].dtype == "object":
                self.df[column] = self.df[column].str.strip()
        print("whitespaces removed successfully.")

        return self.df

    def clean_email(self):
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
                    self.df[column].astype(str).str.match(r"^[\w\.-]+@[\w\.-]+\.\w+$")
                ]

        return self.df


# class EDAanalysis:
#     def __init__(self, df):
#         self.df = df

#     def preview(self):
#         return self.df.head()

#     def shape(self):
#         return self.df.shape

#     def columns(self):
#         return self.df.columns

#     def info(self):
#         return self.df.info()
