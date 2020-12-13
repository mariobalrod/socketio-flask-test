from models.player import Player
from utils.events import *
from utils.random import *

players = []
colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']

def join(name, socketId):
    color = get_random_color(colors)
    colors.remove(color)
    newPlayer = Player(name, color, socketId)
    players.append(newPlayer.__dict__)

    emitAll('players', players)

def start():
    if len(players) > 0:
        impostor = get_random_impostor(players)
        impostor['role'] = 'impostor'
    
    emitAll('players', players)

def vote(id):
    for player in players:
        if player['id'] == id:
            player['voting'] = player['voting'] + 1

    emitAll('players', players)

def end_game():
    max_voting = players[0]
    for player in players:
        if player['voting'] > max_voting['voting']:
            max_voting = player

    for player in players:
        if player['id'] == max_voting['id']:
            player['alive'] = False

    emitAll('players', players)
    

def clear():
    players = []
    colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']

    emitAll('players', players)
    
