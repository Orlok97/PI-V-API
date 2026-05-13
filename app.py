from flask import Flask, jsonify, render_template
from flask_cors import CORS
from config import Config
from routes import Router
from models import db

app = Flask(__name__, template_folder='views',static_folder='static')
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
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True)