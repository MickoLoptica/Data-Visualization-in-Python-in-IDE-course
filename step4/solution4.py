import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def main4():
    data = pd.read_csv("../dataset.csv")
    platforms = ['PS4', 'XOne', 'PC', 'WiiU']
    data = data[data['platform'].isin(platforms)][['name', 'platform', 'genre']]
    data = data.groupby(['platform', 'genre']).size().unstack(fill_value=0)
    return data
