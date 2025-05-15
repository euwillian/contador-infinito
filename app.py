from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ranking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    clicks = db.Column(db.Integer)
    score = db.Column(db.Integer)
    date = db.Column(db.Date)

db.create_all()

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/media')
def media():
    today = datetime.now().date()
    scores = Score.query.filter_by(date=today).all()
    if not scores:
        return jsonify({"media": 50})
    avg = sum(s.clicks for s in scores) // len(scores)
    return jsonify({"media": avg})

@app.route('/enviar', methods=['POST'])
def enviar():
    data = request.get_json()
    name = data.get('name', 'Anônimo')
    clicks = data['clicks']
    media = media().get_json()['media']
    score_val = max(0, 100 - abs(clicks - media) * 10)
    new_score = Score(name=name, clicks=clicks, score=score_val, date=datetime.now().date())
    db.session.add(new_score)
    db.session.commit()
    return '', 204

@app.route('/ranking')
def ranking():
    today = datetime.now().date()
    scores = Score.query.filter_by(date=today).order_by(Score.score.desc()).limit(10).all()
    return jsonify([{"name": s.name, "score": s.score} for s in scores])

if __name__ == '__main__':
    app.run(debug=True)
