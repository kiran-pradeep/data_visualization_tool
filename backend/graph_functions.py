from fastapi import FastAPI, HTTPException, Query, Path
import matplotlib.pyplot as plt
import io
from fastapi.responses import StreamingResponse
import numpy as np

app = FastAPI()

def generate_line_plot(x, y, title):
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Line Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_bar_chart(x, y, title):
    fig, ax = plt.subplots()
    ax.bar(x, y, label='Bar Chart')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_histogram(data, title):
    fig, ax = plt.subplots()
    ax.hist(data, bins='auto', color='#0504aa', alpha=0.7, rwidth=0.85)
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    return fig

def generate_scatter_plot(x, y, title):
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title(title)
    ax.legend()
    return fig

def generate_pie_chart(labels, sizes, title):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title(title)
    return fig

def generate_box_plot(data, title):
    fig, ax = plt.subplots()
    ax.boxplot(data)
    ax.set_xlabel('Data')
    ax.set_ylabel('Value')
    ax.set_title(title)
    return fig

def generate_heatmap(data, title):
    fig, ax = plt.subplots()
    cax = ax.imshow(data, cmap='viridis')
    fig.colorbar(cax)
    ax.set_title(title)
    return fig

def save_plot_to_stream(fig):
    image_stream = io.BytesIO()
    fig.savefig(image_stream, format='png')
    image_stream.seek(0)
    plt.close(fig)
    return image_stream

# API endpoints for different plot types

@app.get("/generate_line_plot/")
async def generate_line_plot_api(
    x: list = Query(..., title="X-axis data", description="X-axis values", example="[1, 2, 3, 4, 5]"),
    y: list = Query(..., title="Y-axis data", description="Y-axis values", example="[10, 12, 5, 8, 15]"),
    title: str = Query(..., title="Plot Title", description="Title of the Line Plot")
):
    fig = generate_line_plot(x, y, title)
    image_stream = save_plot_to_stream(fig)
    return StreamingResponse(content=image_stream, media_type="image/png")

@app.get("/generate_bar_chart/")
async def generate_bar_chart_api(
    x: list = Query(..., title="X-axis data", description="X-axis values", example="[1, 2, 3, 4, 5]"),
    y: list = Query(..., title="Y-axis data", description="Y-axis values", example="[10, 12, 5, 8, 15]"),
    title: str = Query(..., title="Plot Title", description="Title of the Bar Chart")
):
    fig = generate_bar_chart(x, y, title)
    image_stream = save_plot_to_stream(fig)
    return StreamingResponse(content=image_stream, media_type="image/png")

@app.get("/generate_histogram/")
async def generate_histogram_api(
    data: list = Query(..., title="Data", description="List of values for the histogram", example="[1, 2, 2, 3, 3, 3, 4, 4, 5]"),
    title: str = Query(..., title="Plot Title", description="Title of the Histogram")
):
    fig = generate_histogram(data, title)
    image_stream = save_plot_to_stream(fig)
    return StreamingResponse(content=image_stream, media_type="image/png")

@app.get("/generate_scatter_plot/")
async def generate_scatter_plot_api(
    x: list = Query(..., title="X-axis data", description="X-axis values", example="[1, 2, 3, 4, 5]"),
    y: list = Query(..., title="Y-axis data", description="Y-axis values", example="[10, 12, 5, 8, 15]"),
    title: str = Query(..., title="Plot Title", description="Title of the Scatter Plot")
):
    fig = generate_scatter_plot(x, y, title)
    image_stream = save_plot_to_stream(fig)
    return StreamingResponse(content=image_stream, media_type="image/png")

@app.get("/generate_pie_chart/")
async def generate_pie_chart_api(
    labels: list = Query(..., title="Labels", description="Labels for the Pie Chart", example='["Category A", "Category B", "Category C"]'),
    sizes: list = Query(..., title="Sizes", description="Sizes for the Pie Chart", example="[30, 40, 30]"),
    title: str = Query(..., title="Plot Title", description="Title of the Pie Chart")
):
    fig = generate_pie_chart(labels, sizes, title)
    image_stream = save_plot_to_stream(fig)
    return StreamingResponse(content=image_stream, media_type="image/png")

@app.get("/generate_box_plot/")
async def generate_box_plot_api(
    data: list = Query(..., title="Data", description="List of values for the Box Plot", example="[1, 2, 3, 4, 5]"),
    title: str = Query(..., title="Plot Title", description="Title of the Box Plot")
):
    fig = generate_box_plot(data, title)
    image_stream = save_plot_to_stream(fig)
    return StreamingResponse(content=image_stream, media_type="image/png")

@app.get("/generate_heatmap/")
async def generate_heatmap_api(
    data: list = Query(..., title="Data", description="2D array for the Heatmap", example="[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"),
    title: str = Query(..., title="Plot Title", description="Title of the Heatmap")
):
    # Convert the input data to a numpy array
    data = np.array(data, dtype=float)
    
    fig = generate_heatmap(data, title)
    image_stream = save_plot_to_stream(fig)
    return StreamingResponse(content=image_stream, media_type="image/png")
