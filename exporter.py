class ExportData:
    def __init__(self, df):
        self.df = df

    def save_data(self):
        self.df.to_csv("output/cleaned_data.csv", index=False)

    def save_json(self):
        self.df.to_json("output/cleaned_data.json", orient="records", indent=4)