#!/bin/bash

# Create a virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
pip install Flask 

# Run the Flask application
echo "Running the Flask application..."
export FLASK_APP=app.py 
flask run &  

# Open the default web browser to the application
echo "Opening the application in the web browser..."
xdg-open http://127.0.0.1:5000
