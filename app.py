from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from routes import Router
from models import db

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
config = Config(app)
router = Router(app)


db.init_app(app)
with app.app_context():
   db.create_all()
   
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        'name':'PI-V',
        'version':'0.1.0',
        'description':''
    })

@app.route('/dashboard', methods=['GET'])
def dashboard():
    pass

if __name__ == "__main__":
    app.run(debug=True)