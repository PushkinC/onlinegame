import flask, os, json
import threading
from flask import app, request

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

X = 'x'
Y = 'y'

app = flask.Flask(__name__)


class Server():
    def __init__(self):
        self.players = {}  # {id: {name, pos, color, size, hp, deleted_bullets: [], bullets: {id: {color, size, damage, pos})}}

    def add_User(self, data):
        if data['id'] in self.players:
            return {'code': -1, 'error': 'user already exists'}

        self.players[data['id']] = {
            'name': data['name'],
            'pos': [500, 500],
            'color': data['color'],
            'bullets': data['bullets'],
            'size': data['size'],
            'hp': data['hp'],
            'deleted_bullets': data['deleted_bullets']
        }
        return {'code': 200, 'error': ''}

    def del_User(self, id):
        if id not in self.players:
            return {'code': -1, 'error': 'user not exists'}
        del self.players[id]
        return {'code': 200, 'error': ''}

    def update(self, data):
        if data['id'] not in self.players:
            return {'code': -1, 'error': 'user not exists'}

        self.players[data['id']]['pos'] = data['pos']
        self.players[data['id']]['bullets'] = data['bullets']
        for i in self.players[data['id']]['deleted_bullets']:
            if i in self.players[data['id']]['bullets'].keys():
                del self.players[data['id']]['bullets'][i]
        return self.get_Data()

    def get_Data(self):
        return self.players

    def heal(self, data):
        self.players[data['id']]['hp'] += data['heal']

    def collision(self, data: dict):  # {player: {damage, bullets: []}}
        for i in data.keys():
            if i not in self.players.keys():
                print('ААААААААААААААААААААААААААААААААААААААААААААА' * 10)
                return

            self.players[i]['hp'] = max(self.players[i]['hp'] - data[i]['damage'], 0)

            for j in data[i]['bullets']:
                if j in self.players[i]['bullets']:
                    del self.players[i]['bullets'][j]
                    self.players[i]['deleted_bullets'].append(j)








serv = Server()


@app.route('/add', methods=['POST'])
def addUser():
    data = request.get_json()
    if type(data) == str:
        data = json.loads(data)
    resp = serv.add_User(data)
    return json.dumps(resp)


@app.route('/del', methods=['POST'])
def delUser():
    data = request.get_json()
    if type(data) == str:
        data = json.loads(data)

    resp = serv.del_User(data['id'])
    return json.dumps(resp)


@app.route('/tick', methods=['POST'])
def tick():
    data = request.get_json()
    if type(data) == str:
        data = json.loads(data)
    resp = serv.update(data)
    return json.dumps(resp)


@app.route('/stat', methods=['GET'])
def stat():
    return json.dumps(serv.get_Data())

@app.route('/collision', methods=['POST'])
def collision():
    data = request.get_json() # {player: {damage, bullets: []}}
    if type(data) == str:
        data = json.loads(data)

    serv.collision(data)
    return '200'
@app.route('/heal', methods=['POST'])
def heal():
    data = request.get_json()
    if type(data) == str:
        data = json.loads(data)

    serv.heal(data)
    return '200'


@app.route('/ping', methods=['GET'])
def ping():
    return json.dumps({'code': 200, 'error': ''})



def start_collision():
    import CheckerCollision


if __name__ == '__main__':
    th = threading.Thread(target=start_collision)
    th.start()
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)

