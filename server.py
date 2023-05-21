import flask, os, json
from flask import app, request

X = 'x'
Y = 'y'

app = flask.Flask(__name__)


class Server():
    def __init__(self):
        self.users = []
        self.data = {}

    def addUser(self, user, color):
        print('add', user, color)
        if user in self.users:
            print('add error')
            return {'code': -1, 'error': 'user already exists'}

        self.users.append(user)
        self.data[user] = {'pos': [500, 500], 'color': color}
        print('add sacc')
        return {'code': 200, 'error': ''}

    def delUser(self, user):
        if user not in self.users:
            return {'code': -1, 'error': 'user not exists'}
        self.users.remove(user)
        del self.data[user]
        return {'code': 200, 'error': ''}

    def move(self, user, pos):
        if user not in self.users:
            return {'code': -1, 'error': 'user not exists'}

        self.data[user]['pos'] = pos
        return {'code': 200, 'error': ''}

    def getData(self):
        return self.data


serv = Server()


@app.route('/add', methods=['POST'])
def addUser():
    data = request.get_json()
    if type(data) == str:
        data = json.loads(data)
    resp = serv.addUser(data['name'], data['color'])
    return json.dumps(resp)


@app.route('/del', methods=['POST'])
def delUser():
    data = request.get_json()
    if type(data) == str:
        data = json.loads(data)

    resp = serv.delUser(data['name'])
    return json.dumps(resp)


@app.route('/tick', methods=['POST'])
def tick():
    data = request.get_json()
    if type(data) == str:
        data = json.loads(data)
    resp = serv.move(data['name'], data['pos'])
    return json.dumps(resp)


@app.route('/stat', methods=['GET'])
def stat():
    return json.dumps(serv.getData())

@app.route('/ping', methods=['GET'])
def ping():
    return json.dumps({'code': 200, 'error': ''})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)
