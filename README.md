# Graphical Node Builder

A web-based application for creating and visualizing acyclic graphs with custom node parameters.

## Features

- Create nodes with custom ID, condition, and behavior
- Connect nodes to create an acyclic graph
- Modern and responsive UI
- Interactive graph visualization
- Real-time updates

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Add a new node:
   - Fill in the Node ID, Condition, and Behavior in the form
   - Click "Add Node" to create the node

2. Create connections:
   - Click on two nodes in sequence to create a connection between them
   - The connection will be created from the first clicked node to the second

3. View node details:
   - Hover over a node to see its behavior
   - The node's ID and condition are displayed on the node itself

## Note

The graph data is stored in memory and will be reset when the server restarts. 