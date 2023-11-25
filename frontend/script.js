        // Function to handle file upload and trigger plot generation
        function generatePlot(event) {
            
            const fileInput = document.getElementById("csv-input");
            const plotType = document.getElementById("plot-type").value;
            const plotTitle = document.getElementById("plot-title").value;

            const reader = new FileReader();

            // Set up the FileReader to read the file as text
            reader.onload = function (event) {
                const fileContent = event.target.result;

                // Convert CSV data to array of arrays
                const csvData = fileContent.split('\n').map(row => row.split(','));
                const csvHeaders = csvData[0];
                const data = csvData.slice(1).map(row => row.map(parseFloat));
                // Extract X and Y data from CSV
                const x = data.map(row => parseFloat(row[0]));
                const y = data.map(row => parseFloat(row[1]));

                // Create a JSON object with the X and Y data and plot type
                const jsonData = {
                    labels: csvHeaders,
                    title: plotTitle,
                    data: {
                        x: x,
                        y: y,
                    },
                    plot_type: plotType,
                };

                // Make a POST request to the backend to generate the plot
                fetch("http://localhost:8000/generate_plot", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(jsonData),
                })
                .then(response => response.blob())
                .then(blob => {
                    // Display the generated plot in the "plot-area" div
                    const plotArea = document.getElementById("plot-area");
                    plotArea.innerHTML = `<img src="${URL.createObjectURL(blob)}" alt="Generated Plot">`;

                    // Display the download button
                    const downloadButton = document.getElementById("download-button");
                    downloadButton.style.display = "block";

                    // Save the blob locally for download
                    window.generatedBlob = blob;
                    
                })
                .catch(error => console.error("Error:", error));
            };

            // Read the file as text
            reader.readAsText(fileInput.files[0]);
        }

        // Function to trigger the download of the generated image
        function downloadImage() {
            const downloadButton = document.getElementById("download-button");
            const generatedBlob = window.generatedBlob;

            if (generatedBlob) {
                // Create a temporary link element
                const link = document.createElement('a');
                link.href = URL.createObjectURL(generatedBlob);
                link.download = 'generated_plot.png';

                // Append the link to the document and trigger a click event
                document.body.appendChild(link);
                link.click();

                // Remove the link from the document
                document.body.removeChild(link);
            }
        }