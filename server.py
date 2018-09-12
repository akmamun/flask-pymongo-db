from flask import Flask, request
import db as d

app = Flask(__name__)


@app.route('/add/camera', methods=['GET', 'POST'])
def add_camera():
    camera = d.mongo.db.cameras
    add = {
        'ip': request.json['ip'],
        'username': request.json['username'],
        'password': request.json['password'],
    }
    camera.insert({'add': add})
    return 'Insert Camera Successfully'


if __name__ == '__main__':
    app.run(debug=True)
