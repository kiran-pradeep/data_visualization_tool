import matplotlib.pyplot as plt

# Function to create a line plot
def create_line_plot(x_values, y_values, x_label, y_label, title, label):
    """
    Create and display a line plot.

    Args:
    x_values (list): X-axis values.
    y_values (list): Y-axis values.
    x_label (str): Label for the X-axis.
    y_label (str): Label for the Y-axis.
    title (str): Title of the plot.
    label (str): Label for the line in the legend.
    """
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label=label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()

# Function to create a bar plot
def create_bar_plot(categories, values, x_label, y_label, title, label):
    """
    Create and display a bar plot.

    Args:
    categories (list): Category names for the bars.
    values (list): Values corresponding to each category.
    x_label (str): Label for the X-axis.
    y_label (str): Label for the Y-axis.
    title (str): Title of the plot.
    label (str): Label for the bars in the legend.
    """
    fig, ax = plt.subplots()
    ax.bar(categories, values, label=label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()

# Function to create a scatter plot
def create_scatter_plot(x_values, y_values, x_label, y_label, title, label):
    """
    Create and display a scatter plot.

    Args:
    x_values (list): X-axis values.
    y_values (list): Y-axis values.
    x_label (str): Label for the X-axis.
    y_label (str): Label for the Y-axis.
    title (str): Title of the plot.
    label (str): Label for the points in the legend.
    """
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, label=label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()

# Function to create a histogram
def create_histogram(data, bins, x_label, y_label, title, label):
    """
    Create and display a histogram.

    Args:
    data (list): Data points for the histogram.
    bins (int): Number of bins for the histogram.
    x_label (str): Label for the X-axis.
    y_label (str): Label for the Y-axis.
    title (str): Title of the plot.
    label (str): Label for the histogram in the legend.
    """
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, edgecolor='black', alpha=0.7, label=label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()

# Function to create a pie chart
def create_pie_chart(sizes, labels, title):
    """
    Create and display a pie chart.

    Args:
    sizes (list): Sizes (values) for each slice of the pie.
    labels (list): Labels for each slice.
    title (str): Title of the pie chart.
    """
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.
    ax.set_title(title)

# Function to create a box plot
def create_box_plot(data, labels, x_label, y_label, title):
    """
    Create and display a box plot.

    Args:
    data (list of lists): List of data for each box plot.
    labels (list): Labels for each box plot.
    x_label (str): Label for the X-axis.
    y_label (str): Label for the Y-axis.
    title (str): Title of the plot.
    """
    fig, ax = plt.subplots()
    ax.boxplot(data, labels=labels)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

# Function to create an area plot (stacked line plot)
def create_area_plot(x_values, y_values, x_label, y_label, title, labels):
    """
    Create and display an area plot (stacked line plot).

    Args:
    x_values (list): X-axis values.
    y_values (list of lists): List of Y-axis values for each series.
    x_label (str): Label for the X-axis.
    y_label (str): Label for the Y-axis.
    title (str): Title of the plot.
    labels (list): Labels for each series in the legend.
    """
    fig, ax = plt.subplots()
    ax.stackplot(x_values, y_values, labels=labels)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend(loc='upper left')

# Function to save a plot as an image
def save_plot(figure, filename):
    """
    Save a plot as an image file.

    Args:
    figure (matplotlib.figure.Figure): The Matplotlib figure to save.
    filename (str): The filename (including extension) to save the plot as.
    """
    figure.savefig(filename)
    plt.close(figure)
