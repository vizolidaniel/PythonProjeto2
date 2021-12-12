from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
 
 
 
 
app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy conexao com Mysql
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123321@localhost/crudpython"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
 
 
#Criacao dos modelos de classe para criacao da base
class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    vendExterno = db.relationship('VendedorExterno', backref='vendedor')
    engenheiro = db.relationship('EngenheiroCivil', backref='engenheiro')
 
 
    def __init__(self, nome, cpf):
 
        self.nome = nome
        self.cpf = cpf
 
class VendedorExterno(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cnh = db.Column(db.String(100))
    vendedor_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
 
 
    def __init__(self, cnh,vendedor_id):

        self.cnh = cnh
        self.vendedor_id = vendedor_id

class EngenheiroCivil(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    crea = db.Column(db.String(100))
    engenheiro_id = db.Column(db.Integer, db.ForeignKey('funcionario.id'))
 
 
    def __init__(self, crea,engenheiro_id):

        self.crea = crea
        self.engenheiro_id = engenheiro_id
 
 
 

#query utilizada para filtrar, foi utilizado texto puro pois não achei como utilizar da outra forma com 2 join
@app.route('/')
def Index():
    all_data = db.session.execute("""
        select  funcionario.id, funcionario.nome,funcionario.cpf, vendedor_externo.cnh, engenheiro_civil.crea
        from funcionario
        left outer join vendedor_externo on funcionario.id = vendedor_externo.vendedor_id
        left outer join engenheiro_civil on funcionario.id = engenheiro_civil.engenheiro_id""")

    return render_template("index.html", funcionarios = all_data)
 
 
 
# inserir Funcionario com mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():
 
    if request.method == 'POST':
 
        nome = request.form['nome']
        cpf = request.form['cpf']
        cnh = request.form['cnh']
        crea = request.form['crea']

        my_Funcionario = Funcionario(nome, cpf)
        db.session.add(my_Funcionario)
        db.session.flush()

        funcionario_id = db.session.query(Funcionario).filter_by(nome=nome).first().id
        

        if(crea and (not cnh) ):
            my_Engenheiro = EngenheiroCivil(crea, funcionario_id)
            my_Funcionario = Funcionario(nome, cpf)
            db.session.add(my_Engenheiro)
        elif(cnh and (not crea) ):
             my_Vendedor = VendedorExterno(cnh, funcionario_id)
             my_Funcionario = Funcionario(nome, cpf)
             db.session.add(my_Vendedor)
    
        db.session.commit()
 
        flash("funcionario inserido com Sucesso!")
 
        return redirect(url_for('Index'))
 
 
#em desenvolvimento
@app.route('/update', methods = ['GET', 'POST'])
def update():
 
    if request.method == 'POST':
        my_Funcionario = Funcionario.query.get(request.form.get('id'))
 
        my_Funcionario.nome = request.form['nome']
        my_Funcionario.cpf = request.form['cpf']
 
        db.session.commit()
        flash("funcionario atualizado com Sucesso!")
 
        return redirect(url_for('Index'))
 
 
 
 
#em desenvolvimento
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_Funcionario = Funcionario.query.get(id)
    db.session.delete(my_Funcionario)
    db.session.commit()
    flash("funcionario deletado com Sucesso!")
 
    return redirect(url_for('Index'))
 
 
 
 
 
 
if __name__ == "__main__":
    app.run(debug=True)