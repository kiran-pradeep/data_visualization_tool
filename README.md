# Data Visualization Tool

This is a versatile data visualization tool that allows users to generate various types of plots and graphs based on their input data. The tool provides a web interface for easy interaction and visualization.

## Features

- Upload a CSV file containing data.
- Select the type of graph or plot to generate.
- Generate visually appealing and informative data visualizations.
- Download the generated plots for further use or sharing.

## Technologies Used

- **Backend:**
  - FastAPI: A modern, fast web framework for building APIs with Python.
  - Matplotlib: A popular Python plotting library for creating static, animated, and interactive visualizations.
  - Pandas: A powerful data manipulation and analysis library for Python.

- **Frontend:**
  - HTML, CSS, JavaScript: For building a simple and user-friendly web interface.

## Getting Started

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd data-visualization-tool
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:

    ```bash
    uvicorn main:app --reload
    ```

4. Open VSCode and install the LiveServer extension by Ritwick Dey and click on Go Live on the bottom right of VSCode.

5. Open your browser and navigate to [http://127.0.0.1:5500](http://127.0.0.1:5500) to access the web interface.

## Usage

1. Upload a CSV file containing your data.
2. Select the type of graph or plot you want to generate.
3. Click on the "Generate Graph" button.
4. View the generated plot on the page.
5. Click on the "Download Graph" button to download the generated plot.

## Deployment

To deploy this data visualization tool, you can follow these general steps:

1. Choose a hosting service (e.g., AWS, Heroku, or your preferred provider).
2. Set up the necessary environment variables for your deployment environment.
3. Deploy the FastAPI application.

For detailed deployment instructions, refer to the documentation of your chosen hosting service.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the FastAPI, Matplotlib, and Pandas communities for providing powerful tools for web development and data visualization in Python.
