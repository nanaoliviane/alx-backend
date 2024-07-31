#!/usr/bin/env python3

"""
Basic Flask app setup
"""

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page

    Returns:
        str: The rendered template for the index page.
    """
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)



