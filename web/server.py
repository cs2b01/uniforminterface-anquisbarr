from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.usuarios)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_users', methods = ['GET'])
def create_users():
    db_session = db.getSession(engine)
    users = entities.usuarios(codigo=201810253, nombre="Juan", apellido="Davila", password="9874")
    db_session.add(users)
    db_session.commit()
    return "An user has been created"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('localhost'))
