# Import necessary modules and packages
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import io
import numpy as np
import pandas as pd
from typing import List, Dict

# Import custom modules
from preprocessing import GraphData
from graph_functions import *

# Create a FastAPI instance
app = FastAPI()

# Add CORS middleware to handle Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define an API endpoint for generating plots
@app.post("/generate_plot")
async def generate_plot(graph_data: GraphData):
    """
    Generate a plot based on the provided graph data.

    Args:
        graph_data (GraphData): An instance of the GraphData class containing 'x' and 'y' data
                                along with the 'plot_type' specifying the type of plot.

    Returns:
        FileResponse: A FastAPI FileResponse containing the generated plot file.
                      Raises HTTPException with appropriate status code and details for errors.
    """
    # Extract data from the incoming request
    data = graph_data.data
    plot_type = graph_data.plot_type
    x = data['x']
    y = data['y']
    
    try:
        # Generate plot based on the specified plot type
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
            data = np.array(df, dtype=float)  # (Note: df is not defined in the code. It might be a typo.)
            fig = generate_heatmap(data, "Heatmap")
        else:
            # Raise an exception for an invalid plot type
            raise HTTPException(status_code=400, detail="Invalid plot type")

        # Save the generated plot to a file
        fpath = save_plot_to_file(fig)

        # Return the plot as a FileResponse
        return FileResponse(fpath)

    # Handle HTTPExceptions and other general exceptions
    except HTTPException as e:
        return e
    except Exception as e:
        # Raise a 500 Internal Server Error with a detailed message
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
