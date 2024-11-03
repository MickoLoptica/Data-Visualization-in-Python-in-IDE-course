import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def main2():
    data = pd.read_csv("../dataset.csv")
    print(data.head(10))
    return data