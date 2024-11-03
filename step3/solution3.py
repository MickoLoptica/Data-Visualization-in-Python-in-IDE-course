import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main3():
    data = pd.read_csv("../dataset.csv")
    platforms = ['PS4', 'XOne', 'PC', 'WiiU']
    data = data[data['platform'].isin(platforms)][['name', 'platform', 'genre']]
    return data