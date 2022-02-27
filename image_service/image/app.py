from flask import Flask, request, jsonify
import csv

filename = "images.csv"
fields = ['image_id', 'image_name', 'image_path']

IP = "127.0.0.1"
PORT = 8081

"""
data = {
    0:
        {
            "image_id": 0,
            "image_name": "Cat",
            "image_path": "https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-superJumbo.jpg",
        }
}
"""


def _get_image_data():
    image_data = {}
    with open(filename, 'r') as file:
        # reading the CSV file
        for row in csv.DictReader(file):
            image_data[row["image_id"]] = row

    return image_data


def _write_image_data(image_data):
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        for row in image_data.values():
            writer.writerow(row)


def find_image_path(image_name):
    """
    Reads the data from images.csv and returns the image path
    :return:
    """

    # 1. get the image data
    image_data = _get_image_data()

    # 2. find the row with this image name, and then return the path\
    for row in image_data.values():
        if row["image_name"] == image_name:
            return row["image_path"]

    return ""


def update_image(image_name, new_image_path):
    # 1. get the image data
    image_data = _get_image_data()

    # 2. update the row that has the same image name to now
    # have the new value for its image_path
    result = None
    for row in image_data.values():
        if row["image_name"] == image_name:
            row["image_path"] = new_image_path
            result = row

    # write out the database again
    _write_image_data(image_data)
    return result


def add_image(new_image_row):
    """
    Writes the data received to the csv file images.csv
    :return:
    """

    # 1. read all existing data
    image_data = _get_image_data()

    # 2. check to make sure this image is not already in the db
    for row in image_data.values():
        if row["image_name"] == new_image_row["image_name"]:
            return None

    # 3. add the new row
    new_id = str(len(image_data))
    new_image_row["image_id"] = new_id
    image_data[new_id] = new_image_row

    # 4. write out the whole db again
    _write_image_data(image_data)
    return new_id


app = Flask('app')


@app.route('/store_data', methods=['POST'])
def store_data():
    """
    Store data for an image path

    input: json object with image_name and image_path
    returns an OK response or an error

    :return:
    """

    params = request.get_json()
    image_name = params.get('image_name')
    image_path = params.get('image_path')

    if image_name is None or image_path is None:
        response_data = {
            "success": False
        }
        return jsonify(response_data), 400

    image_data = {
        "image_name": image_name,
        "image_path": image_path
    }

    new_image_id = add_image(image_data)
    if new_image_id is not None:
        image_data["image_id"] = new_image_id
        response_data = {
            "success": True,
            "data": image_data
        }

        return jsonify(response_data), 201
    else:
        response_data = {
            "success": False,
            "error_message": "image_name '%s' already exists" % image_name
        }

        return jsonify(response_data), 400


@app.route('/get_data', methods=['GET'])
def get_data():
    """
    GET
    receives the image name
    :return:
    """

    params = request.get_json()
    image_name = params.get('image_name')
    found_image_path = find_image_path(image_name)

    if found_image_path:
        response_data = {
            "success": "true",
            "image_path": found_image_path
        }

        return jsonify(response_data), 201

    else:
        response_data = {
            "success": "false"
        }

        return jsonify(response_data), 401


@app.route('/update_data', methods=['PATCH'])
def update_data():
    """
    PATCH
    changes the image_path
    :return:
    """

    params = request.get_json()
    image_name = params.get('image_name')
    new_image_path = params.get('image_path')
    image_data = update_image(image_name, new_image_path)

    if image_data is not None:
        response_data = {
            "success": "true",
            "image_data": image_data
        }

        return jsonify(response_data), 201

    else:
        response_data = {
            "success": "false"
        }

        return jsonify(response_data), 400


app.run(host=IP, port=PORT, debug=True)
