Travel Planner App
Overview
The Travel Planner App is a web application that helps users find the shortest path between two cities in India, along with the travel distance (in kilometers) and estimated travel time. The app uses a Flask backend with NetworkX to calculate the shortest path and OpenRouteService for route calculations. The frontend is built using HTML and CSS, providing an intuitive user interface.

Features
Shortest Path Calculation: The app calculates the shortest path between any two cities in India.
Distance and Time Estimation: The total distance (in kilometers) and estimated time (in hours) are displayed.
Via Option: Users can optionally add a "via" location to pass through during their journey.
Responsive UI: The app's UI is responsive, providing a smooth experience on both desktop and mobile devices.
Interactive Design: With advanced CSS and interactive JavaScript features, users get an intuitive experience.
Technologies Used
Backend:

Python
Flask
NetworkX (for graph-based shortest path calculations)
OpenRouteService API (for routing and distance calculation)
Frontend:

HTML5
CSS3 (with advanced features)
JavaScript (for AJAX requests)
Installation
Follow the steps below to set up the app on your local machine.

Prerequisites
Python 3.x (Install from python.org)
pip (Python package installer)
Anaconda (Optional, for managing environments)
Step 1: Clone the Repository
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/travel-planner-app.git
cd travel-planner-app
Step 2: Install Required Python Packages
It's recommended to use a virtual environment. If you are using Anaconda, you can create a new environment as follows:
conda create --name travel-planner python=3.8
conda activate travel-planner
Then, install the required Python packages:

pip install -r requirements.txt
Alternatively, install the necessary packages manually using pip:


pip install Flask networkx openrouteservice
Step 3: Create a .env File for Configuration (Optional)
In case you are using OpenRouteService API, create a .env file to store your API key:

makefile
OPENROUTESERVICE_API_KEY=your_api_key_here
Make sure to replace your_api_key_here with your actual API key from OpenRouteService.

Step 4: Run the Flask Server
To start the Flask backend, run the following command:

python app.py
By default, the app will be accessible at http://127.0.0.1:5000.

Step 5: Access the Web App
Open a web browser and go to:
http://127.0.0.1:5000
You should see the Travel Planner App homepage.

Usage
Select a source and destination city from the dropdown menus.
Optionally, enter a via city (a city you want to pass through).
Click the "Find Shortest Path" button.
The app will display the shortest path, distance in km, and estimated time for the journey.
Example
Source City: Delhi
Destination City: Mumbai
Via City (Optional): Jaipur
The app will calculate the shortest path, distance, and time.

Folder Structure
travel-planner-app/
│
├── app.py                 # Flask backend
├── requirements.txt       # List of required Python packages
├── static/                # Static folder for CSS and JavaScript files
│   └── style.css          # Custom CSS file
├── templates/             # Folder containing HTML templates
│   └── index.html         # HTML template for the travel planner
├── .env                   # (Optional) OpenRouteService API key configuration
└── README.md              # Documentation for the app
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit (git commit -am 'Add new feature').
Push to the branch (git push origin feature-name).
Create a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
The app uses OpenRouteService for calculating the shortest path and travel distances.
Flask for serving the backend.
NetworkX for graph-based algorithms.
Notes:
You can customize the cities in the dropdown based on the cities you’ve added to the graph in the backend.
If you encounter issues with the OpenRouteService API, ensure that your API key is correctly set in the .env file.
If you plan to deploy the app, consider setting it up on platforms like Heroku, AWS, or PythonAnywhere.
