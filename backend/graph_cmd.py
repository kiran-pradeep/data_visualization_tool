import argparse
from graph_functions import *
import matplotlib.pyplot as plt

def parse_args():
    parser = argparse.ArgumentParser(description="Generate different types of plots.")
    parser.add_argument("--plot_type", choices=["line", "bar", "histogram", "scatter", "pie", "box", "heatmap"],
                        help="Type of plot to generate", required=True)
    parser.add_argument("--x", type=float, nargs="+", help="X-axis data", required=True)
    parser.add_argument("--y", type=float, nargs="+", help="Y-axis data", required=True)
    parser.add_argument("--title", type=str, help="Title of the plot", default="Generated Plot")
    return parser.parse_args()

def main():
    args = parse_args()

    if args.plot_type == "line":
        fig = generate_line_plot(args.x, args.y, args.title)
    elif args.plot_type == "bar":
        fig = generate_bar_chart(args.x, args.y, args.title)
    elif args.plot_type == "histogram":
        fig = generate_histogram(args.y, args.title)
    elif args.plot_type == "scatter":
        fig = generate_scatter_plot(args.x, args.y, args.title)
    elif args.plot_type == "pie":
        labels = [str(i) for i in range(len(args.x))]
        fig = generate_pie_chart(labels, args.y, args.title)
    elif args.plot_type == "box":
        fig = generate_box_plot([args.y], args.title)
    elif args.plot_type == "heatmap":
        data = [[float(value) for value in args.x], [float(value) for value in args.y]]
        fig = generate_heatmap(data, args.title)

    plt.show()

if __name__ == "__main__":
    main()
