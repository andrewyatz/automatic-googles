from flask import Flask
import datetime
from flask import jsonify
from tzlocal import get_localzone
app = Flask(__name__)

@app.route("/date")
def hello():
    now = datetime.datetime.now(tz=get_localzone())
    dateformat = "%a %b %d %H:%M:%S %Z %Y";
    # { "date": "Wed Sep 20 15:32:35 BST 2017" }
    return jsonify({"date" : now.strftime(dateformat)})
