from flask import Flask, request, jsonify
import db as d

app = Flask(__name__)

# get data from cameras
@app.route('/cameras', methods=['GET'])
def get_camera():
    collection_camera = d.mongo.db.cameras
    camera_list = []
    for obj in collection_camera.find():
        obj.pop('_id')
        camera_list.append(obj)
        return jsonify(camera_list)


# add camera
@app.route('/add/camera', methods=['GET', 'POST'])
def add_camera():
    camera = d.mongo.db.cameras
    data = {
        'ip': request.json['ip'],
        'username': request.json['username'],
        'password': request.json['password'],
    }
    camera.insert({'data': data})
    return 'Added Camera Successfully'


# add image
@app.route('/camera/images/add', methods=['GET', 'POST'])
def add_camera_image():
    image = d.mongo.db.images
    image_data = {
        'camera_ip': request.json['camera_ip'],
        'image': request.json['image']
    }
    image.insert({'image': image_data})
    return "Image Uploaded"


# get images
@app.route('/camera/images', methods=['GET'])
def get_images():
    collection_images = d.mongo.db.images
    image_list = []
    for obj in collection_images.find():
        obj.pop('_id')
        image_list.append(obj)
        return jsonify(image_list)


if __name__ == '__main__':
    app.run(debug=True)
