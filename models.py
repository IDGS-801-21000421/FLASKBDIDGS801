from flask_sqlalchemy import SQLAlchemy
import datetime
db = SQLAlchemy()

class Alumnos(db.Model):
    _tablename_ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apaterno = db.Column(db.String(100))
    email = db.Column(db.String(100))
    created_date=db.Column(db.DateTime, default=datetime.datetime.now)