from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

from controllers.players import *
from utils.events import *

# Iniciar app flask
app = Flask(__name__)

# Configuracion necesaria para la app flask
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

# Añadiendo Cors a la app
CORS(app, resources={r"/*": {"origins": "*"}})

# Añadiendo socketio a la app y cors a los socket
socketio = SocketIO(app, cors_allowed_origins='*')

#Ruta Inicial del servidor Flask
@app.route('/')
def index():
    return 'Server running'


@socketio.on_error()      
def error_handler(e):
    print(e)

#Eventos Sockets

@socketio.on('connect')
def on_connect():
    print('Someone has been connected')
    
    @socketio.on('join')
    def on_join(name, id):
        join(name, id)

    @socketio.on('start')
    def on_start():
        start()

    @socketio.on('vote')
    def on_vote(id):
        vote(id)

    @socketio.on('end')
    def on_end():
        end_game()

    @socketio.on('clear')
    def on_clear():
        clear()

    @socketio.on('disconnect')
    def on_disconnect():
        print('User has been disconnected')


# Método principal main (Inicializando servidor)
if __name__ == '__main__':
    socketio.run(app)