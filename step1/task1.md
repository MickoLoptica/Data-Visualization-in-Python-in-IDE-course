# Task 1 - Basic Project Setup

Before we start programming, we need to do few things. First, we need the data that we’ll analyze and plot – you can download it [here](https://drive.google.com/drive/folders/18r0XtRXZe_ljb6NfgjUdgnuuINc42SFw?usp=sharing). In this tutorial, we’ll analyze the distribution of video games by genre across different platforms. In the end, we’ll create a bar chart that shows the number of games by genre for the following platforms: PS4, XOne, PC, and WiiU.

We'll use this data throughout each step of the tutorial, so make sure to save it in the root directory of the project, i.e., the main folder where files like README.md and the tutorial folders are located.

One of Python’s strengths is its support for libraries – add-ons that extend its basic functionality. Without libraries, tasks such as processing large amounts of data and creating plots would be quite difficult.

There are several libraries for plotting ([matplotlib](https://matplotlib.org/), [plotly](https://plotly.com/python/), etc.). The library we’ll use is [seaborn](https://seaborn.pydata.org/).

Python libraries are installed using the "pip" command from the computer’s command prompt. If you’re using Windows, open the command prompt by typing “cmd” in the search bar and selecting Command Prompt.

In the command line, type:
```bash
pip install seaborn
```
And that’s it! Pip will install Seaborn for us, and we can start programming!

To use the installed libraries within our project, we need to import them. This is done with the import command; at the beginning of your project, type:
```python
import seaborn as sns
import matplotlib.pyplot as plt
```
This imports the libraries we’ll need for plotting. Additionally, we’ve set aliases – shortened names that let us avoid typing the full library name every time we use one of its functions.

Now, we just need to check if we’ve installed and imported the library correctly. Seaborn offers sample data for this purpose. Add the following to your code, in the main1 function:
```python
df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")
```

To display the plot, you’ll need to import one more library and call its function to render the plot:
```python
import matplotlib.pyplot as plt
plt.show()
```
(HINT: It’s recommended to keep library imports separate from the task code itself. Therefore, it’s better to add this second import directly after the first import and before any data processing or plotting functions.)

Run test1 – if a new window opens successfully, showing multiple charts on penguin species, you’ve done everything correctly and are ready for the next step in the tutorial!