# Task 5 - Drawing the Chart

We’ve reached the final part of this tutorial — actually drawing the chart! Now that all the data is organized and ready, we just need to present it visually.

We can open the chart window with:
```python
plt.figure(figsize=(x, y))
```
where x is the width, and y is the height of the window.

The function used for plotting bar charts is:
```python
sns.barplot(data=your_data, x=x_data, y=y_data, hue=some_data)
```
and it has several parameters:
* data: specifies the data used in the chart,
* x: specifies data for the x-axis,
* y: specifies data for the y-axis, and
* hue: colors the data according to values in another column, adding more information to the chart.

Some additional useful functions are:
1) `plt.title()` - adds the chart title,
2) `plt.xlabel()` - labels the x-axis,
3) `plt.ylabel()` - labels the y-axis, and
4) `plt.legend()` - adds a legend to the chart.

Finally, to display the chart, use:
`plt.show()`

In this task, try to implement code that draws the chart based on the processed data from the previous steps. Add a title, axis labels, and a legend to make the chart more informative.

Congratulations on completing this tutorial on data manipulation and visualization! Now you’re ready to explore and create your own charts!