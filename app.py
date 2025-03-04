from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms 

from models import db
from models import Alumnos


app = Flask(__name__)


app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)


@app.route("/")
@app.route("/index", methods = ["GET", "POST"])
def index():
    
    create_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all() 
    return render_template("index.html", form = create_form, alumnos = alumno)


@app.route("/detalles", methods=["POST", "GET"])
def detalles():
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter_by(id=id).first()
        if alum1:
            return render_template('detalles.html', alum=alum1)
        else:
            flash("Alumno no encontrado", "error")
            return redirect(url_for('index'))

    

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()