"""
Power BI Graphs - Flask Web Application
---------------------------------------
This is a simple Flask application that serves a webpage displaying Power BI graphs.
It renders the `graphs.html` template, which dynamically loads images from a specified folder.

Features:
- Uses Flask to serve the webpage.
- Loads and displays Power BI graph images in an interactive layout.
- Designed to be easily extendable.

Routes:
- `/` : Serves the `graphs.html` template.

Usage:
Run the script and access the application at `http://127.0.0.1:5000/`.

"""

import os
from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    image_folder = "static/Plots"
    images = [
        f for f in os.listdir(image_folder) if f.endswith(("png", "jpg", "jpeg", "gif"))
    ]
    return render_template("index.html", images=images)


if __name__ == "__main__":
    app.run()
