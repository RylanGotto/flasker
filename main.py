from flask import Flask
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/update", methods=["POST"])
def update():
    exec(open("update.py").read())
    return json.dumps({'code': 100})
