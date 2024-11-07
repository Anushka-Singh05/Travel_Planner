from flask import Flask, jsonify, request, render_template
import networkx as nx

# Create Flask app
app = Flask(__name__)

# Create a graph of Indian cities with travel times (in hours)
G = nx.Graph()

# Add cities as nodes
cities = [
    'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai', 'Hyderabad', 'Jaipur', 'Pune', 'Ahmedabad',
    'Lucknow', 'Surat', 'Indore', 'Chandigarh', 'Vadodara', 'Nagpur', 'Coimbatore', 'Patna', 'Bhopal', 'Goa', 'Udaipur'
]
G.add_nodes_from(cities)

# Add edges with travel time (in hours)
edges = [
    ('Delhi', 'Mumbai', 16),
    ('Delhi', 'Bangalore', 30),
    ('Mumbai', 'Bangalore', 24),
    ('Bangalore', 'Chennai', 6),
    ('Chennai', 'Hyderabad', 10),
    ('Hyderabad', 'Mumbai', 13),
    ('Jaipur', 'Delhi', 6),
    ('Pune', 'Mumbai', 3),
    ('Ahmedabad', 'Mumbai', 8),
    ('Delhi', 'Lucknow', 6),
    ('Mumbai', 'Surat', 4),
    ('Surat', 'Ahmedabad', 3),
    ('Indore', 'Mumbai', 14),
    ('Chandigarh', 'Delhi', 5),
    ('Vadodara', 'Mumbai', 7),
    ('Nagpur', 'Hyderabad', 6),
    ('Coimbatore', 'Chennai', 6),
    ('Patna', 'Kolkata', 7),
    ('Bhopal', 'Indore', 2),
    ('Goa', 'Mumbai', 6),
    ('Udaipur', 'Jaipur', 7)
]
G.add_weighted_edges_from(edges)

# Endpoint to render the home page
@app.route('/')
def index():
    return render_template('index.html', cities=cities)

# Endpoint to calculate the shortest path
@app.route('/shortest_path', methods=['GET'])
def get_shortest_path():
    source = request.args.get('source')
    target = request.args.get('target')
    via = request.args.get('via', '').split(',')

    if not source or not target:
        return jsonify({"error": "Please provide both source and target cities"}), 400

    try:
        # Include via locations if any
        if via:
            cities_involved = [source] + via + [target]
            path = []
            total_time = 0
            for i in range(len(cities_involved) - 1):
                sub_path = nx.dijkstra_path(G, cities_involved[i], cities_involved[i + 1], weight='weight')
                path.extend(sub_path[:-1])  # Avoid duplicates for intermediate cities
                total_time += nx.dijkstra_path_length(G, cities_involved[i], cities_involved[i + 1], weight='weight')
        else:
            # If no via option, just find the direct shortest path
            path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
            total_time = nx.dijkstra_path_length(G, source=source, target=target, weight='weight')

        # Convert the time into distance (Assume 60 km/h average speed for cars)
        total_distance_km = total_time * 60  # convert hours to kilometers

        return jsonify({
            "path": path,
            "distance": total_distance_km,  # in kilometers
            "time": total_time  # in hours
        })
    except nx.NetworkXNoPath:
        return jsonify({"error": "No path found between the selected cities"}), 404

if __name__ == '__main__':
    app.run(debug=True)
