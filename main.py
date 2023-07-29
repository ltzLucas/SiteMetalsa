from flask import Flask, request, redirect, render_template, jsonify, url_for
from BD.DaoUser import ItemDatabaseUser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        db = ItemDatabaseUser()
        free = request.form.get('free')
        passwordUser = request.form.get('password')
        try:
            freeInt = int(free)
        except ValueError:
            return render_template('login.html',error=True)

        result = db.procuraUserFree(freeInt)

        if result[0]["Free"] != freeInt or result[0]["Password"] != passwordUser:
            return render_template('login.html', error=True)
        else:
            return redirect('/home')

@app.route('/cadastrarUser', methods=['GET'])
def cadastrarUserPage():
    return render_template('cadastrarUser.html')


@app.route('/cadastrarUser' , methods=['POST'])
def cadastrarUser():
    if request.method == 'POST':

        nome = request.form.get('nome')
        email = request.form.get('email')
        free = request.form.get('free')
        passwordUser = request.form.get('password')

        try:
            freeInt = int(free)
            if nome == '' or email == '' or passwordUser == '':
                return render_template('cadastrarUser.html', errorCadastro=True)
        except ValueError:
            return render_template('cadastrarUser.html', errorCadastro=True)

        db = ItemDatabaseUser()
        result = db.procuraTodosIDUser()

        for freeBD in result:
            if freeBD["Free"] == freeInt:
                return render_template('cadastrarUser.html', errorCadastro=True)

        db.criaUsuario(freeInt,nome,email,passwordUser,"User")

        return redirect('/')


@app.route('/home')
def homeProducao():

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)