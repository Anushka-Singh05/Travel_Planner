🚗 Travel Planner – Shortest Path Finder using Dijkstra’s Algorithm
-----
📌 Project Overview

This project is a web-based Travel Planner application built using Flask and NetworkX.

The system calculates the shortest path between Indian cities using Dijkstra’s Algorithm.

Cities are represented as graph nodes and travel time (in hours) is used as weighted edges.

The application also estimates travel distance assuming an average speed of 60 km/h.
----
📊 Graph Information

Total Cities: 20

Graph Type: Undirected Weighted Graph

Edge Weights: Travel Time (in hours)

Algorithm Used: Dijkstra’s Algorithm
------
🗺️ Supported Cities

Delhi, Mumbai, Bangalore, Kolkata, Chennai, Hyderabad, Jaipur, Pune, Ahmedabad, Lucknow, Surat, Indore, Chandigarh, Vadodara, Nagpur, Coimbatore, Patna, Bhopal, Goa, Udaipur
------
🔍 System Flow
✔ User Inputs:

Source City

Destination City

Optional Via Cities

✔ Backend Processing:

Validate input

Apply Dijkstra’s Algorithm

Calculate total travel time

Estimate total distance

Distance is calculated as:

Distance = Time × 60

(Assuming 60 km/h average speed)
-----
⚙️ Features

Shortest path calculation

Multiple via city support

Automatic distance estimation

REST API endpoint

Responsive UI

Real-time result display
----
🤖 Algorithm Used
1️⃣ Dijkstra’s Algorithm

Used to find the shortest path between two nodes in a weighted graph.

Steps:

Initialize distances

Use priority queue

Update shortest distances

Repeat until destination reached

Time Complexity:
O((V + E) log V)

Where:

V = Number of vertices (cities)

E = Number of edges (routes)

🔌 API Endpoint
GET /shortest_path
Parameters

source (Required)

target (Required)

via (Optional – comma separated cities)

Example Request

/shortest_path?source=Delhi&target=Mumbai

Example Response

{
"path": ["Delhi", "Mumbai"],
"distance": 960,
"time": 16
}
-----
🛠️ Technologies Used

Python

Flask

NetworkX

HTML

CSS

JavaScript
----
📁 Project Structure

Travel-Planner/
│
├── app.py
├── templates/index.html
├── static/styles.css
└── README.md
----
🚀 Future Improvements

Add map visualization

Add traffic-based dynamic weights

Add transport modes (Train/Flight/Bus)

Deploy on cloud platform

Add unit testing
---
🎯 Conclusion

The project successfully implements graph theory concepts.

Dijkstra’s Algorithm efficiently computes optimal routes.

The system provides estimated time and distance instantly.

The application demonstrates backend + frontend integration.
---
⭐ "Finding the fastest route, one city at a time."
Notes:
You can customize the cities in the dropdown based on the cities you’ve added to the graph in the backend.
If you encounter issues with the OpenRouteService API, ensure that your API key is correctly set in the .env file.
If you plan to deploy the app, consider setting it up on platforms like Heroku, AWS, or PythonAnywhere.
