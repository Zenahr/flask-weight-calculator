import os
import webbrowser
from threading import Timer
from flask import Flask, render_template, url_for, request, jsonify
import sqlite3

# SETUP -------------------------------------------------------------------------------------

app=Flask(__name__)
app.config["DEBUG"]=True
PORT="8080"
TEMPLATES_PATH=os.path.join(os.getcwd(), "View")
# print(TEMPLATES_PATH)

# SETUP -------------------------------------------------------------------------------------

# DATA STUFF -------------------------------------------------------------------------------------


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'weight': '70.20',
     'date_time': '20.06.2020',
     },
    {'id': 1,
     'weight': '70.80',
     'date_time': '20.06.2020',
     },
    {'id': 2,
     'weight': '69.90',
     'date_time': '20.06.2020',
     },
    
]

# DATA STUFF -------------------------------------------------------------------------------------



# ROUTES -------------------------------------------------------------------------------------

@app.route('/')
def index(name=None):
#     return render_template('index.html', template_folder=TEMPLATES_PATH)
    return render_template('index.html')

@app.route('/api/list', methods=['GET'])
def api_all():
    return jsonify(books)

# Example use: http://127.0.0.1:8080/api/items?id=1
@app.route('/api/items', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# ROUTES -------------------------------------------------------------------------------------

app.run(port=PORT)



# def open_browser():
      # webbrowser.open_new('http://127.0.0.1:' + PORT + '/')

# if __name__ == "__main__":
#       app.config['TEMPLATES_AUTO_RELOAD']=True
#       app.run(port=PORT, debug=True,use_reloader=True, host="0.0.0.0")
#       Timer(1, open_browser).start()