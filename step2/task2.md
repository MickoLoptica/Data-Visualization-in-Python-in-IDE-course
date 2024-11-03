# Task 2 - Loading and Reading Data

To create a plot, we first need to format the data in a way that’s suitable for us. The game data is provided in CSV format, where the information is separated by commas. The first row usually contains the column names, while each subsequent row represents individual games. You can open the dataset you downloaded in a program like Excel to see what it looks like.

To begin, we need to open this data file within our project and read its contents. For this, we’ll need another library – `pandas`. Import it the same way as the previous libraries. The common alias for this library is `pd`.

Some functions in this library include:
1) `read_csv(path)` – loads data from a CSV file at the given path
2) `head(n)` – reads the first n rows of the loaded CSV file, default n value is 5
3) `tail(n)` – reads the last n rows of the loaded CSV file, default n value is 5
4) `info()` – displays basic information about the loaded file, like the number of rows and the data type in each column

Try to load the data from the CSV file, and then print the first 10 rows.

