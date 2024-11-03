import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def main5():
    data = pd.read_csv("../dataset.csv")
    platforms = ['PS4', 'XOne', 'PC', 'WiiU']
    data = data[data['platform'].isin(platforms)][['name', 'platform', 'genre']]
    data = data.groupby(['platform', 'genre']).size().reset_index(name='counts')

    return data
