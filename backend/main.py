# Import necessary modules and packages
from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.responses import FileResponse
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
    labels = graph_data.labels
    title =graph_data.title
    x = data['x']
    y = data['y']
    x = [k for k in x if k is not None]
    y = [k for k in y if k is not None]
    
    try:
        # Generate plot based on the specified plot type
        if plot_type == "line":
            fig = generate_line_plot(x, y, title, labels)
        elif plot_type == "bar":
            fig = generate_bar_chart(x, y, title, labels)
        elif plot_type == "histogram":
            fig = generate_histogram(x, y, title, labels)
        elif plot_type == "scatter":
            fig = generate_scatter_plot(x, y, title, labels)
        elif plot_type == "pie":
            sizes = [str(i) for i in range(len(x))]
            fig = generate_pie_chart(y, sizes, title, labels)
        elif plot_type == "box":
            fig = generate_box_plot([y], title, labels)
        elif plot_type == "heatmap":
            df = pd.DataFrame()
            df['x'] = x
            df['y'] = y
            data = np.array(df, dtype=float)  # (Note: df is not defined in the code. It might be a typo.)
            fig = generate_heatmap(data, title, labels)
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
