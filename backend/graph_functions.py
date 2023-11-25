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


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def gen_random_str(N: int) -> str:
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789') for _ in range(N))

def save_plot_to_file(fig: plt.Figure):
    print("check")
    os.makedirs('../outputs', exist_ok=True)
    fpath = "../outputs/" + gen_random_str(32) + ".png"
    fig.savefig(fpath, format="png")
    return fpath

def validate_csv_file(file: UploadFile) -> pd.DataFrame:
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(io.StringIO(file.file.read().decode('utf-8')))
        return df
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV file. Error: {str(e)}")

def validate_json_content(json_content: Dict[str, List[float]]) -> List[List[float]]:
    try:
        x = json_content.get('x', [])
        y = json_content.get('y', [])

        if not x or not y:
            raise ValueError("X-axis and Y-axis data must be provided.")

        return list(zip(x, y))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON content. Error: {str(e)}")

def generate_line_plot(x: List[float], y: List[float], title: str) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Line Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_bar_chart(x: List[float], y: List[float], title: str) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.bar(x, y, label='Bar Chart')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_histogram(data: List[float], title: str) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.hist(data, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    return fig

def generate_scatter_plot(x: List[float], y: List[float], title: str) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_pie_chart(labels: List[str], sizes: List[float], title: str) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(title)
    return fig

def generate_box_plot(data: List[float], title: str) -> plt.Figure:
    fig, ax = plt.subplots()
    ax.boxplot(data)
    ax.set_xlabel('Data')
    ax.set_ylabel('Value')
    ax.set_title(title)
    return fig

def generate_heatmap(data: List[List[float]], title: str) -> plt.Figure:
    fig, ax = plt.subplots()
    cax = ax.imshow(data, cmap='viridis')
    fig.colorbar(cax)
    ax.set_title(title)
    return fig

from pydantic import BaseModel

class GraphData(BaseModel):
    data: dict
    plot_type: str


# API endpoint for generating plots
@app.post("/generate_plot")
async def generate_plot(graph_data: GraphData):
    data = graph_data.data
    plot_type = graph_data.plot_type
    x = data['x']
    y = data['y']
    
    try:
        # Generate plot based on plot type
        if plot_type == "line":
            fig = generate_line_plot(x, y, "Line Plot")
        elif plot_type == "bar":
            fig = generate_bar_chart(x, y, "Bar Chart")
        elif plot_type == "histogram":
            fig = generate_histogram(y, "Histogram")
        elif plot_type == "scatter":
            fig = generate_scatter_plot(x, y, "Scatter Plot")
        elif plot_type == "pie":
            labels = [str(i) for i in range(len(x))]
            fig = generate_pie_chart(labels, y, "Pie Chart")
        elif plot_type == "box":
            fig = generate_box_plot([y], "Box Plot")
        elif plot_type == "heatmap":
            data = np.array(df, dtype=float)
            fig = generate_heatmap(data, "Heatmap")
        else:
            raise HTTPException(status_code=400, detail="Invalid plot type")
        # Save plot to stream
        fpath = save_plot_to_file(fig)
        

        # Return the plot as a StreamingResponse
        return FileResponse(fpath)
        return StreamingResponse(content=image_stream, media_type="image/png")

    except HTTPException as e:
        return e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
