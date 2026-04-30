import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'sqlite:///fishdb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    pass


@app.route("/api/status", methods=["GET"])
def get_status():
    return jsonify({
        "status": "online",
    })


@app.route('/api/login', methods=['POST'])
def login():
    pass


@app.route('/api/upload', methods=['POST'])
def upload_image():
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("資料庫初始化完成！")
    app.run(port=8000, debug=True)
