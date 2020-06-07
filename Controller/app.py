import os
import webbrowser
from threading import Timer
from flask import Flask, render_template, url_for, request, jsonify
import sqlite3
import time

# SETUP -------------------------------------------------------------------------------------

app=Flask(__name__)
app.config["DEBUG"]=True
HOST="192.168.1.63"
PORT="8080"
TEMPLATES_PATH=os.path.join(os.getcwd(), "View")
DATABASE='databaseBig.db'
# print(TEMPLATES_PATH)

# SETUP -------------------------------------------------------------------------------------

# UTILS ----------------------------------------------------------------

def calcAvgSum(rows):
    result = 0
    divideBy=len(rows)

    # Edge Case: Database with no records
    if (len(rows) < 1):
        divideBy=1
    
    for row in rows:
    #    print(row.keys()) # DEBUG
       result += float(row['weight'])
    result = result / divideBy
    result = round(result, 2)
    return result

# UTILS ----------------------------------------------------------------

# DATA STUFF -------------------------------------------------------------------------------------


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# DATA STUFF -------------------------------------------------------------------------------------
conn = sqlite3.connect(DATABASE, check_same_thread=False)



# ROUTES -------------------------------------------------------------------------------------

@app.route('/', methods = ['POST', 'GET'])
def index():
    con = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()
    cur.execute("select * from weights")
   
    rows = cur.fetchall()
    # avgSum = calcAvgSum(rows)
    avgSum = 0

    msg = ""
    if request.method == 'POST':
      try:
         weightValue = request.form['weight']
         timeStamp = time.time()
         cur.execute("INSERT INTO weights (WEIGHT, TIMESTAMP) VALUES(?, ?)",(weightValue, timeStamp) )
         conn.commit()
         msg = "Record successfully added"
      except:
         conn.rollback()
         msg = "error in insert operation"
      finally:
         conn.close()

    return render_template("index.html", rows=rows, avgSum=avgSum, msg = msg)


# ROUTES (JSON ENDPOINTS) -------------------------------------------------------------------------------------

@app.route('/api/json/all', methods=['GET'])
def api_all():
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM weights;').fetchall()
    return jsonify(all_books)


# Example use: http://127.0.0.1:8080/api/items?id=1
# Example use: http://127.0.0.1:8080/api/items?weight=70,21
@app.route('/api/json', methods=['GET'])
def api_filter():
    query_parameters = request.args
    id = query_parameters.get('id')
    weight = query_parameters.get('weight')
    date_time = query_parameters.get('timestamp')
    query = "SELECT * FROM weights WHERE"
    to_filter = []
    if id:
        query += ' ID=? AND'
        to_filter.append(id)
    if weight:
        query += ' WEIGHT=? AND'
        to_filter.append(weight)
    if date_time:
        query += ' TIMESTAMP=? AND'
        to_filter.append(date_time)
    if not (id or weight or date_time):
        return page_not_found(404)
    query = query[:-4] + ';'
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()
    return jsonify(results)

# ROUTES (JSON ENDPOINTS) -------------------------------------------------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# ROUTES -------------------------------------------------------------------------------------

app.run(host=HOST, port=PORT)

# def open_browser():
      # webbrowser.open_new('http://127.0.0.1:' + PORT + '/')

# if __name__ == "__main__":
#       app.config['TEMPLATES_AUTO_RELOAD']=True
#       app.run(port=PORT, debug=True,use_reloader=True, host="0.0.0.0")
#       Timer(1, open_browser).start()

