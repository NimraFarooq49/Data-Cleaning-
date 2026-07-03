import pandas as pd
import numpy as np

df = pd.read_csv("C:\Users\user\Desktop\Data Cleaning\input")

class LoadData:
    def __init__(self,filepath):
        self.filepath=filepath
        self.df=None

    def load_data(self):
        self.df=pd.read_csv(self.filepath)
        return self.df


class DataCleaner:
    def __init__(self,df):
        self.df=df

    def remove_duplicate(self):
        pass

    def missing_value(self):
        pass



class EDAanalysis:
    def __init__(self,df):
        self.df=df





