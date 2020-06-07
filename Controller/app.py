import os
import webbrowser
from threading import Timer
from flask import Flask, render_template, url_for

app=Flask(__name__)
PORT="8080"
TEMPLATES_PATH=os.path.join(os.getcwd(), "View")
# print(TEMPLATES_PATH)

@app.route('/')
def index(name=None):
#     return render_template('index.html', template_folder=TEMPLATES_PATH)
    return render_template('index.html')





# def open_browser():
      # webbrowser.open_new('http://127.0.0.1:' + PORT + '/')

# if __name__ == "__main__":
#       app.config['TEMPLATES_AUTO_RELOAD']=True
#       app.run(port=PORT, debug=True,use_reloader=True, host="0.0.0.0")
#       Timer(1, open_browser).start()