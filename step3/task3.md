# Task 3 - Filtering Data

Of course, we don’t need all the data contained in this file. Some information about video games is irrelevant, and there are games on platforms we don’t intend to analyze. So, we need an efficient way to filter the data, keeping only what’s essential.

The pandas library allows us to manipulate our data structure that we previously loaded from the CSV file. We can filter the data in several ways:

For example, you can access only a specific column of our data structure:
```python
filtered_data = data['column name']
```
or multiple columns:
```python
filtered_data = data[['column1', 'column2']]
```
This way, we can filter irrelevant columns.

Using the `isin` function, we can also create a simple query to keep only the rows where a column has values of interest:
```python
array = ['value 1', 'value 2', 'value 3']
filtered_data = data[data['column name'].isin(array)]
```

By combining the functions above, we can filter our data structure by both rows and columns. Try filtering the data so that only the columns with game names, platforms, and genres remain for the platforms we’re interested in for this task.

With this cleaned data, we’re ready for the next step!