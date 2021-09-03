from flask import Flask, request

app = Flask(__name__)


@app.route('/api/v3/client', methods=['GET'])
    def hello_world():
        if lToken != '':
            return 'entered client api'
        else: 
            return 'you dont have clearence, sign in first'






 @app.route('/login', methods=['POST'])
    def login():
        error = None
        if request.method == 'POST':
            if valid_login(request.form['email'],
                    request.form['password']):
                return log_the_user_in(request.form['username'])
            else:
                error = 'Invalid username/password'
  


