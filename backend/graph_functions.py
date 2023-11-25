# Import necessary modules and packages
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import io
import numpy as np
import pandas as pd
from typing import List, Dict
import random
import string
import os

# Function to generate a random string of specified length
def gen_random_str(N: int) -> str:
    """
    Generate a random string of specified length.

    Args:
        N (int): Length of the random string.

    Returns:
        str: The generated random string.
    """
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789') for _ in range(N))

# Function to save a matplotlib figure to a file
def save_plot_to_file(fig: plt.Figure) -> str:
    """
    Save a Matplotlib figure to a file.

    Args:
        fig (plt.Figure): Matplotlib figure to be saved.

    Returns:
        str: File path where the figure is saved.
    """
    print("check")
    os.makedirs('../outputs', exist_ok=True)
    fpath = "../outputs/" + gen_random_str(32) + ".png"
    fig.savefig(fpath, format="png")
    return fpath

# Function to validate and read CSV file into a Pandas DataFrame
def validate_csv_file(file: UploadFile) -> pd.DataFrame:
    """
    Validate and read a CSV file into a Pandas DataFrame.

    Args:
        file (UploadFile): Uploaded CSV file.

    Returns:
        pd.DataFrame: Pandas DataFrame representing the CSV data.

    Raises:
        HTTPException: If the file is not a valid CSV file.
    """
    try:
        df = pd.read_csv(io.StringIO(file.file.read().decode('utf-8')))
        return df
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV file. Error: {str(e)}")

# Function to validate and extract data from JSON content
def validate_json_content(json_content: Dict[str, List[float]]) -> List[List[float]]:
    """
    Validate and extract data from JSON content.

    Args:
        json_content (Dict[str, List[float]]): JSON content with 'x' and 'y' lists.

    Returns:
        List[List[float]]: List of tuples representing paired 'x' and 'y' values.

    Raises:
        HTTPException: If the JSON content is invalid.
    """
    try:
        x = json_content.get('x', [])
        y = json_content.get('y', [])

        if not x or not y:
            raise ValueError("X-axis and Y-axis data must be provided.")

        return list(zip(x, y))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON content. Error: {str(e)}")

# Functions to generate various types of plots

def generate_line_plot(x: List[float], y: List[float], title: str) -> plt.Figure:
    """
    Generate a line plot.

    Args:
        x (List[float]): X-axis data.
        y (List[float]): Y-axis data.
        title (str): Title of the plot.

    Returns:
        plt.Figure: Matplotlib figure of the line plot.
    """
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Line Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_bar_chart(x: List[float], y: List[float], title: str) -> plt.Figure:
    """
    Generate a bar chart.

    Args:
        x (List[float]): X-axis data.
        y (List[float]): Y-axis data.
        title (str): Title of the plot.

    Returns:
        plt.Figure: Matplotlib figure of the bar chart.
    """
    fig, ax = plt.subplots()
    ax.bar(x, y, label='Bar Chart')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_histogram(data: List[float], title: str) -> plt.Figure:
    """
    Generate a histogram.

    Args:
        data (List[float]): Data for the histogram.
        title (str): Title of the plot.

    Returns:
        plt.Figure: Matplotlib figure of the histogram.
    """
    fig, ax = plt.subplots()
    ax.hist(data, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    return fig

def generate_scatter_plot(x: List[float], y: List[float], title: str) -> plt.Figure:
    """
    Generate a scatter plot.

    Args:
        x (List[float]): X-axis data.
        y (List[float]): Y-axis data.
        title (str): Title of the plot.

    Returns:
        plt.Figure: Matplotlib figure of the scatter plot.
    """
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_pie_chart(labels: List[str], sizes: List[float], title: str) -> plt.Figure:
    """
    Generate a pie chart.

    Args:
        labels (List[str]): Labels for the pie chart.
        sizes (List[float]): Sizes of each pie slice.
        title (str): Title of the plot.

    Returns:
        plt.Figure: Matplotlib figure of the pie chart.
    """
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(title)
    return fig

def generate_box_plot(data: List[float], title: str) -> plt.Figure:
    """
    Generate a box plot.

    Args:
        data (List[float]): Data for the box plot.
        title (str): Title of the plot.

    Returns:
        plt.Figure: Matplotlib figure of the box plot.
    """
    fig, ax = plt.subplots()
    ax.boxplot(data)
    ax.set_xlabel('Data')
    ax.set_ylabel('Value')
    ax.set_title(title)
    return fig

def generate_heatmap(data: List[List[float]], title: str) -> plt.Figure:
    """
    Generate a heatmap.

    Args:
        data (List[List[float]]): Data for the heatmap.
        title (str): Title of the plot.

    Returns:
        plt.Figure: Matplotlib figure of the heatmap.
    """
    fig, ax = plt.subplots()
    cax = ax.imshow(data, cmap='viridis')
    fig.colorbar(cax)
    ax.set_title(title)
    return fig
