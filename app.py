from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# In-memory storage for the graph
graph_data = {
    "nodes": [],
    "edges": []
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/nodes', methods=['GET'])
def get_nodes():
    return jsonify(graph_data["nodes"])

@app.route('/api/edges', methods=['GET'])
def get_edges():
    return jsonify(graph_data["edges"])

@app.route('/api/node', methods=['POST'])
def add_node():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Validate required fields
        required_fields = ['id', 'condition', 'behavior']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Check if node ID already exists
        if any(node['id'] == data['id'] for node in graph_data["nodes"]):
            return jsonify({"error": "Node ID already exists"}), 400

        node = {
            "id": data['id'],
            "condition": data['condition'],
            "behavior": data['behavior'],
            "connections": data.get('connections', [])
        }
        
        graph_data["nodes"].append(node)
        return jsonify({"message": "Node added successfully", "node": node}), 200

    except Exception as e:
        print(f"Error adding node: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500

@app.route('/api/edge', methods=['POST'])
def add_edge():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Validate required fields
        if 'source' not in data or 'target' not in data:
            return jsonify({"error": "Missing source or target node"}), 400

        # Check if nodes exist
        source_exists = any(node['id'] == data['source'] for node in graph_data["nodes"])
        target_exists = any(node['id'] == data['target'] for node in graph_data["nodes"])
        
        if not source_exists or not target_exists:
            return jsonify({"error": "Source or target node does not exist"}), 400

        # Check if edge already exists
        if any(edge['source'] == data['source'] and edge['target'] == data['target'] 
               for edge in graph_data["edges"]):
            return jsonify({"error": "Edge already exists"}), 400

        edge = {
            "source": data['source'],
            "target": data['target']
        }
        
        graph_data["edges"].append(edge)
        return jsonify({"message": "Edge added successfully", "edge": edge}), 200

    except Exception as e:
        print(f"Error adding edge: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500

@app.route('/api/graph', methods=['GET'])
def get_graph():
    return jsonify(graph_data)

if __name__ == '__main__':
    app.run(debug=True)
