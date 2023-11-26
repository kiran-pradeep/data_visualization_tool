import argparse
import pandas as pd
from graph_functions import *
import csv

def parse_args():
    parser = argparse.ArgumentParser(description="Generate a graph from a CSV file.")
    parser.add_argument("--csv_file", type=str, help="Path to the CSV file with 'x' and 'y' columns", required=True)
    parser.add_argument("--plot_type", choices=["line", "bar", "histogram", "scatter", "pie", "box", "heatmap"],
                        help="Type of plot to generate", required=True)
    parser.add_argument("--title", type=str, help="Title of the plot", default="Generated Plot")
    return parser.parse_args()

def main():
    args = parse_args()

    try:
        data = pd.read_csv(args.csv_file, index_col=False)
        labels = list(data.columns)
        print("data:", data)
        print("labels: ", labels)
        print(list(data.columns))
        x = data[labels[0]].tolist()
        y = data[labels[1]].tolist()
        print(x)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    if args.plot_type == "line":
        fig = generate_line_plot(x, y, args.title, labels)
    elif args.plot_type == "bar":
        fig = generate_bar_chart(x, y, args.title, labels)
    elif args.plot_type == "histogram":
        fig = generate_histogram(x, y, args.title, ["Value", "Frequency"])
    elif args.plot_type == "scatter":
        fig = generate_scatter_plot(x, y, args.title, labels)
    elif args.plot_type == "pie":
        labels = [str(i) for i in range(len(x))]
        fig = generate_pie_chart(labels, y, args.title, labels)
    elif args.plot_type == "box":
        fig = generate_box_plot([y], args.title, ["Data", "Value"])
    elif args.plot_type == "heatmap":
        data = [list(map(float, x)), list(map(float, y))]
        fig = generate_heatmap(data, args.title, labels)
    else:
        print("Invalid plot type. Please choose from 'line', 'bar', 'histogram', 'scatter', 'pie', 'box', 'heatmap'.")
        return

    plt.show()

if __name__ == "__main__":
    main()
