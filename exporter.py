class ExportData:
    def __init__(self, df):
        self.df = df

    def save_csv(self, filepath):
        self.df.to_csv(filepath, index=False)
        print("CSV file saved successfully.")

    def save_json(self, filepath):
        self.df.to_json(filepath, orient="records", indent=4)
        print("JSON file saved successfully.")
