from flask import Flask, request, redirect, render_template, jsonify, url_for
from BD.DaoUser import DatabaseUser
from modelo.User import User

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        free = request.form.get('free')
        passwordUser = request.form.get('password')

        try:
            freeInt = int(free)
        except ValueError:
            return render_template('login.html',error=True)

        db = DatabaseUser()
        user = db.searchUserByFree(freeInt)
        if user:
            if user.free != freeInt or user.password != passwordUser:
                return render_template('login.html', error=True)
            else:
                return redirect('/home')
        else:
            return render_template('login.html', error=True)

@app.route('/cadastrarUser', methods=['GET'])
def cadastrarUserPage():
    return render_template('cadastrarUser.html')


@app.route('/cadastrarUser' , methods=['POST'])
def cadastrarUser():
    if request.method == 'POST':
        free = request.form.get('free')
        name = request.form.get('nome')
        email = request.form.get('email')
        password = request.form.get('password')


        try:
            newUser = User(free, name, email, password)
            # Successfully created user, proceed with database insertion or other logic
        except ValueError as e:
            return render_template('cadastrarUser.html', errorCadastro=True, errorMessage=str(e))

        db = DatabaseUser()
        AllUsers = db.searchAllUsers()

        for user in AllUsers:
            if user.free == int(free):
                return render_template('cadastrarUser.html', errorCadastro=True)


        db.insertUser(newUser)
        return redirect('/')


@app.route('/home')
def homeProducao():

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)