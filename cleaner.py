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

    def remove_duplicate(self):
        self.df = self.df.drop_duplicates().copy()
        return self.df

    def missing_value(self):
        return self.df.isnull().sum()

    def fill_missing(self):
        self.df["Age"] = self.df["Age"].fillna(self.df["Age"].mean())
        self.df["Fare"] = self.df["Fare"].fillna(self.df["Fare"].mean())
        self.df = self.df.fillna("Unknown")
        return self.df

    def remove_whitespace(self):
        self.df = self.df.apply(
            lambda x: x.str.strip() if x.dtype == "object" else x
        )
        return self.df

    def clean_invalid_email(self):
        self.df["Email"] = self.df["Email"].fillna("unknown@gmail.com")

        self.df["Email"] = self.df["Email"].apply(
            lambda x: x if ("@" in str(x) and "." in str(x))
            else "unknown@gmail.com"
        )

        return self.df


class EDAanalysis:
    def __init__(self, df):
        self.df = df

    def preview(self):
        return self.df.head()

    def shape(self):
        return self.df.shape

    def columns(self):
        return self.df.columns

    def info(self):
        return self.df.info()

