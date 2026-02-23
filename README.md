# 🚗 Travel Planner – Shortest Path Finder

> ⭐ *"Finding the fastest route, one city at a time."*

---

## 📌 Project Overview

This is a **web-based Travel Planner application** built using **Flask** and **NetworkX**. The system calculates the shortest path between major Indian cities using **Dijkstra’s Algorithm**.

- **Cities** are represented as graph nodes.
- **Travel time** (in hours) is used as weighted edges.
- **Distance** is estimated assuming an average speed of 60 km/h.

---

## 📊 Graph Information

| Feature | Details |
| :--- | :--- |
| **Total Cities** | 20 |
| **Graph Type** | Undirected Weighted Graph |
| **Edge Weights** | Travel Time (hours) |
| **Algorithm Used** | Dijkstra’s Algorithm |
| **Time Complexity** | $O((V + E) \log V)$ |

Where:
- **V** = Number of vertices (cities)
- **E** = Number of edges (routes)

---

## 🗺️ Supported Cities

The graph includes the following 20 major Indian hubs:

> Delhi, Mumbai, Bangalore, Kolkata, Chennai, Hyderabad, Jaipur, Pune, Ahmedabad, Lucknow, Surat, Indore, Chandigarh, Vadodara, Nagpur, Coimbatore, Patna, Bhopal, Goa, Udaipur.

---

## 🔍 System Flow

### ✔ User Inputs
1. **Source City:** The starting point of the journey.
2. **Destination City:** The final stop.
3. **Optional Via Cities:** Intermediate locations to be visited.

### ✔ Backend Processing
- **Validation:** Ensures the cities exist in the dataset.
- **Dijkstra’s Algorithm:** Computes the path with the minimum cumulative weight (time).
- **Calculation:** Derives total distance using the formula:
  $$\text{Distance} = \text{Time} \times 60$$

---

## ⚙️ Features

- ✅ **Shortest Path Calculation:** Efficiently finds the quickest route.
- ✅ **Multiple "Via" Support:** Plan trips with multiple stops.
- ✅ **Automatic Estimation:** Instant time and distance readouts.
- ✅ **REST API Endpoint:** Backend can be queried via HTTP requests.
- ✅ **Responsive UI:** Clean, mobile-friendly interface.

---

## 🔌 API Documentation

### `GET /shortest_path`

**Parameters:**

| Parameter | Required | Description |
| :--- | :--- | :--- |
| `source` | **Yes** | Starting city name |
| `target` | **Yes** | Destination city name |
| `via` | No | Comma-separated list of intermediate cities |

## 📥 Example Request

`GET /shortest_path?source=Delhi&target=Mumbai`

---

## 📤 Example Response

`'json
{
  "path": ["Delhi", "Jaipur", "Ahmedabad", "Mumbai"],
  "distance": 840,
  "time": 14,
  "status": "success"
}``

---
##🛠️ Technologies Used

Python – Core logic and data processing

Flask – Lightweight web framework for API and routing

NetworkX – Graph theory library for implementing Dijkstra’s Algorithm

HTML / CSS / JavaScript – Responsive frontend user interface
---
##📁 Project Structure
``text
Travel-Planner/
│
├── app.py              # Flask server & Dijkstra logic 
├── templates/  :---
│   └── index.html      # Frontend structure (Jinja2)  
├── static/ :---
│   └── styles.css      # Custom UI styling & layout 
└── README.md           # Project documentation  
---
##🚀 Future Improvements
🌍 Map Visualization: Integrate Leaflet.js or Mapbox for visual routes.

🚦 Real-time Traffic: Add dynamic edge weights based on live API data.

🚆 Multi-modal Transport: Options for Train, Flight, or Bus routes.

🧪 Unit Testing: Implement PyTest for algorithm validation.
---
##🚀 Future Improvements
🌍 Map Visualization: Integrate Leaflet.js or Mapbox for visual routes.

🚦 Real-time Traffic: Add dynamic edge weights based on live API data.

🚆 Multi-modal Transport: Options for Train, Flight, or Bus routes.

🧪 Unit Testing: Implement PyTest for algorithm validation
---
##🎯 Conclusion
This project successfully implements graph theory concepts in a real-world scenario. By leveraging Dijkstra’s Algorithm, the application provides optimal routes and estimated logistics instantly, demonstrating a seamless integration between Python backend logic and a modern web frontend.
