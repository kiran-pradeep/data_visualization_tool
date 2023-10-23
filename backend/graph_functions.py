import matplotlib.pyplot as plt


def bar_plot(xs, ys, labels, colors, widths, xlabel, ylabel, title, out_path):
    """
    To create bar plots

    Args:
        xs: list of lists for the x-axis
        ys: list of lists for the y-axis
        labels: list of labels for each corresponding (x, y) pairs
        colors: list of colors for each corresponding (x, y) pairs
        widths: list of widths for each corresponding (x, y) pairs
        xlabel: label for the x-axis
        ylabel: label for the y-axis
        title: title for the graph
        out_path: path to save the  graph

    Returns:
        None
    """
    plt.figure(figsize=(10,6))
    for i, _ in enumerate(xs):
        plt.bar(xs[i], ys[i], label=labels[i], color=colors[i], width=widths[i])
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.savefig(out_path, bbox_inches='tight')



def scatter_plot(xs, ys, labels, colors, title, xlabel, ylabel, out_path):
    """
    To create scatter plots 

    Args:
        xs: list of lists for the x-axis
        ys: list of lists for the y-axis
        labels: list of labels for each corresponding (x, y) pairs
        colors: list of colors for each corresponding (x, y) pairs
        xlabel: label for the x-axis
        ylabel: label for the y-axis
        title: title for the graph
        out_path: path to save the  graph

    Returns:
        None
    """
    plt.figure(figsize=(10,6))
    for i, x in enumerate(xs):
        plt.scatter(xs[i], ys[i], label=labels[i], color=colors[i])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()

    plt.savefig(out_path, bbox_inches='tight')


def pie_plot():
    """
    To generate pie plots 

    Args:
        xs: list of lists for the x-axis
        ys: list of lists for the y-axis
        labels: list of labels for each corresponding (x, y) pairs
        colors: list of colors for each corresponding (x, y) pairs
        xlabel: label for the x-axis
        ylabel: label for the y-axis
        title: title for the graph
        out_path: path to save the  graph

    Returns:
        None
    """
    plt.figure(figsize=(10,6))

    slice = [12, 25, 50, 36, 19]
    activities = ['NLP','Neural Network', 'Data analytics', 'Quantum Computing', 'Machine Learning']
    cols = ['r','b','c','g', 'orange']
    plt.pie(slice,
    labels =activities,
    colors = cols,
    startangle = 90,
    shadow = True,
    explode =(0,0.1,0,0,0),
    autopct ='%1.1f%%')
    plt.title('Training Subjects')

    plt.savefig("output2.png", bbox_inches='tight')


def area_plot():
    plt.figure(figsize=(10,6))

    days = [1,2,3,4,5]
    age =[63, 81, 52, 22, 37]
    weight =[17, 28, 72, 52, 32]
    plt.plot([],[], color='c', label = 'Weather Predicted', linewidth=5)
    plt.plot([],[],color = 'g', label='Weather Change happened', linewidth=5)
    plt.stackplot(days, age, weight, colors = ['c', 'g'])
    plt.xlabel('Fluctuation with time')
    plt.ylabel('Days')
    plt.title('Weather report using Area Plot')
    plt.legend()

    plt.savefig("output2.png", bbox_inches='tight')


def hist_plot():
    """
    To create scatter plots 

    Args:
        xs: list of lists for the x-axis
        ys: list of lists for the y-axis
        labels: list of labels for each corresponding (x, y) pairs
        colors: list of colors for each corresponding (x, y) pairs
        xlabel: label for the x-axis
        ylabel: label for the y-axis
        title: title for the graph
        out_path: path to save the  graph

    Returns:
        None
    """
    plt.figure(figsize=(10,6))

    pop = [22,55,62,45,21,22,34,42,42,4,2,8]
    bins = [1,10,20,30,40,50]
    plt.hist(pop, bins, rwidth=0.6)
    plt.xlabel('age groups')
    plt.ylabel('Number of people')
    plt.title('Histogram')
    
    plt.savefig("output2.png", bbox_inches='tight')




