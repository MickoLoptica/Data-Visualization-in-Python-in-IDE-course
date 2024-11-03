# Task 4 - Aggregating and Analyzing Data

Now that we’ve successfully loaded and filtered the data, we need to extract the specific information required for our graph. To create a chart, we need to know the number of games by genre, and that information isn’t directly available in our file! Therefore, we must generate this information from the data we already have.

Some useful methods in the pandas library include `groupby`:
```python
grouped_data = data.groupby(['column 1', 'column 2'])
```
which allows us to group data by the values in columns. That is, if we have two columns, we get a new structure where a new group of data is created for each unique combination of column 1 and column 2 values.

The structure produced by this method is not easily readable, so we can further process it, for example, with:
```python
grouped_data = data.groupby(['column 1', 'column 2']).size()
```
which gives us the count of rows matching each combination of column 1 and column 2 values.

We can also organize this structure by setting one of the columns as a row, resulting in an even more readable format:
```python
grouped_data = data.groupby(['column 1', 'column 2']).size().unstack(fill_value=0)
```
The fill_value parameter specifies the value to fill cells when there is no data matching a specific column combination.

For this task, try to write code that extracts all combinations of platforms and genres from our filtered data structure, then calculates how many games match each combination.

Once you’ve confirmed everything works correctly, we can move on to the next step.