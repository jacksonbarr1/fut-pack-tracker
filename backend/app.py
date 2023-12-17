import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT', 3306)
db_name = os.environ.get('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Pack(db.Model):
    pack_id = db.Column(db.Integer, primary_key=True)
    pack_name = db.Column(db.String(64))
    coin_value = db.Column(db.Integer)
    fcp_value = db.Column(db.Integer)
    item_count = db.Column(db.Integer)
    rare_item_count = db.Column(db.Integer)
    player_count = db.Column(db.Integer)

    def __repr__(self):
        return f'<Pack {self.pack_name}>'


@app.route('/packs')
def get_packs():
    packs = Pack.query.all()
    return jsonify([{
        'pack_id': pack.pack_id,
        'pack_name': pack.pack_name,
        'coin_value': pack.coin_value,
        'fcp_value': pack.fcp_value,
        'item_count': pack.item_count,
        'rare_item_count': pack.rare_item_count,
        'player_count': pack.player_count
    } for pack in packs])
