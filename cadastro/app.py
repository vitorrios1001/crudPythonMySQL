from flask import Flask, render_template, request, url_for, redirect

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='Templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/crud'

db = SQLAlchemy(app)

class Produto(db.Model):
    __tablename__='produto'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc = db.Column(db.String(50))
    qtdEstoque = db.Column(db.Integer)
    vlr = db.Column(db.Float)


    def __init__(self, desc, qtdEstoque, vlr):
        self.desc = desc
        self.qtdEstoque = qtdEstoque
        self.vlr = vlr

db.create_all()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/insert")
def insert():
    return render_template("insert.html")

@app.route("/newInsert", methods=['GET','POST'])
def newInsert():
    if request.method == 'POST':
        desc = (request.form.get("desc"))
        qtdEstoque = (request.form.get("qtdEstoque"))
        vlr = (request.form.get("vlr"))

        if desc and qtdEstoque and vlr:
            p = Produto(desc,qtdEstoque,vlr)
            db.session.add(p)
            db.session.commit()

    return redirect(url_for("list"))

@app.route("/list")
def list():
    produto = Produto.query.all()

    return render_template("list.html", produtos=produto)

@app.route("/delete", methods=['GET', 'POST'])
def delete():
    if request.method == "POST": 

        id = (request.form.get("_id")) 

        if id:
            p = Produto.query.filter_by(_id=id).first()
            db.session.delete(p)
            db.session.commit()   
           
        prod = Produto.query.all()
    return redirect(url_for("list")) 

    return render_template("list.html",produtos=prod)
    
    

if __name__ == "__main__":
    app.run(debug=True)

