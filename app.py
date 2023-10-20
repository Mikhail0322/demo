from flask import Flask, jsonify, request
# from dataclasses import dataclass, asdict

app = Flask(__name__)



class store_data:
    name: str
    posts: list = []

    def __init__(self, _name):
        self.name = _name
        self.posts = []

    def to_json(self):

        if len(self.posts) == 0:
            return '{"' + self.name + '"}'

        out = '{"' + self.name + '": ['

        for i in range(len(self.posts)):
            if i == len(self.posts) - 1:
                out = out + '"' + self.posts[i].decode() + '"'
            else:
                out = out + '"' + self.posts[i].decode() + '",'

        out = out + ']}'
        return out


users_data: list = []


def dump_all_users_data_to_json():
    if len(users_data) == 0:
        return '{}'

    out = '{'

    for i in range(len(users_data)):
        if i == len(users_data) - 1:
            out = out + '"' + users_data[i].name + '"'
        else:
            out = out + '"' + users_data[i].name + '",'

    out = out + '}'
    return out


def dump_all_post_to_json():
    out: str = ''
    for obj in users_data:
        out = out + obj.to_json()
    return out


def dump_post_to_json(_user :str):

    for obj in users_data:
        if obj.name == _user:

            if len(obj.posts) == 0:
                return '{}'
            out = '{'

            for i in range(len(obj.posts)):
                if i == len(obj.posts) - 1:
                    out = out + '"' + obj.posts[i].decode() + '"'
                else:
                    out = out + '"' + obj.posts[i].decode() + '",'

            out = out + '}'

            return out
    return '{}'


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/', methods=['GET'])
def index():
    return 'Usage: /users -list users\r\n '


@app.route('/users/<_name>', methods=['POST'])
def create_user(_name: str):
    try:
        for obj in users_data:
            if obj.name == _name:
                return jsonify({'error': 'User exist'}), 400

        users_data.append(store_data(_name))

        return jsonify({'response': 'ok'}), 201
    except Exception as ex:
        return f"Failed to CREATE with: {ex}", 404


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(dump_all_users_data_to_json())


@app.route('/users/<_name>', methods=['DELETE'])
def delete_user(_name: str):
    for i in range(len(users_data)):
        if users_data[i] == _name:
            del users_data[i]
            return jsonify({'response': 'ok'}), 200
    return jsonify({'error': 'User not found'}), 404


@app.route('/posts/<_name>', methods=['POST'])
def create_post(_name: str):
    for i in range(len(users_data)):
        if users_data[i].name == _name:
            post_data = request.get_data()
            print('User:' + users_data[i].name + ' add new post:' + post_data.decode())
            users_data[i].posts.append(post_data)
            return jsonify({'response': 'ok'}), 200

    return jsonify({'error': 'User not found'}), 404


@app.route('/posts', methods=['GET'])
def get_posts():
    #print(dump_all_post_to_json())
    return jsonify(dump_all_post_to_json())


@app.route('/posts/<_name>', methods=['GET'])
def get_post(_name: str):
    for obj in users_data:
        if obj.name == _name:
            return jsonify(dump_post_to_json(_name)), 200

    return jsonify({'error': 'Post not found'}), 404


@app.route('/posts/<_name>/<_post_id>', methods=['PUT'])
def update_post(_name: str, _post_id: str):
    for i in range(len(users_data)):
        if users_data[i].name == _name:
            post_data = request.get_data()
            for p in range(len(users_data[i].posts)):
                if p == int(_post_id):
                    users_data[i].posts[p] = post_data
                    return jsonify({'response': 'ok'}), 200

    return jsonify({'error': 'Post not found'}), 404


@app.route('/posts/<_name>/<_post_id>', methods=['DELETE'])
def delete_post(_name: str, _post_id: str):

    for i in range(len(users_data)):
        if users_data[i].name == _name:
            for p in range(len(users_data[i].posts)):
                if p == int(_post_id):
                    del users_data[i].posts[p]
                    return '', 204

    return jsonify({'error': 'Post not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
