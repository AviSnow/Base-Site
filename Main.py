from flask import Flask, Blueprint
from waitress import serve

app = Flask(__name__)
app.config['SECRET_Key'] = 'I love Canes'
@app.route('/')

def this_Works():
    return 'This totally works!!'

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
    app.run()