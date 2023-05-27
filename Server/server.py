import flask, os, json
from flask import app, request

X = 'x'
Y = 'y'

app = flask.Flask(__name__)


class Server():
    def __init__(self):
        self.players = {}

    def add_User(self, id, color):
        print('add', id, color)
        if id in self.players:
            print('add error')
            return {'code': -1, 'error': 'user already exists'}

        self.players[id] = {'pos': [500, 500], 'color': color}
        print('add sacc')
        return {'code': 200, 'error': ''}

    def del_User(self, id):
        if id not in self.players:
            return {'code': -1, 'error': 'user not exists'}
        del self.players[id]
        return {'code': 200, 'error': ''}

    def move(self, id, pos):
        if id not in self.players:
            return {'code': -1, 'error': 'user not exists'}

        self.players[id]['pos'] = pos
        return {'code': 200, 'error': ''}

    def get_Data(self):
        return self.players


serv = Server()


@app.route('/add', methods=['POST'])
def addUser():
    data = request.get_json()
    if type(data) == str:
        data = json.loads(data)
    resp = serv.add_User(data['id'], data['color'])
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
    resp = serv.move(data['id'], data['pos'])
    return json.dumps(resp)


@app.route('/stat', methods=['GET'])
def stat():
    return json.dumps(serv.get_Data())

@app.route('/ping', methods=['GET'])
def ping():
    return json.dumps({'code': 200, 'error': ''})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)
