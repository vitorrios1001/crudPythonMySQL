from flask import Flask, render_template, request, url_for, redirect

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/crud'

db = SQLAlchemy(app)

class Produto(db.Model):
    __tablename__='produto'

    _id = db.Column('id',db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome',db.String(50))

    def __init__(self, nome):
        self.nome = nome

db.create_all()

@app.route("/")
@app.route("/index")

def index():
    return "<h1>Ta funcinando</h1>"

if __name__ == "__main__":
    app.run(debug=True)

