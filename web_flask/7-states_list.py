#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
# storage_type
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def n_template():
    """Render a template"""
    states = list(storage.all(State).values())
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close_session(self):
    """This method remove the current SQLAlchemy close_session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
