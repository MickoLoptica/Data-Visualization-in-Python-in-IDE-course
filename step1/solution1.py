import seaborn as sns
import matplotlib.pyplot as plt

def main1():
    df = sns.load_dataset("penguins")
    sns.pairplot(df, hue="species")
    plt.show()