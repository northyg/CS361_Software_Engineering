import requests

IP = "127.0.0.1"
PORT = 8081
SERVICE_URL = "http://%s:%d" % (IP, PORT)

# POST an image to the image service
response_store = requests.post(SERVICE_URL + "/store_data", json={
    "image_name": "rooster",
    "image_path": "http://www.google.com/sad.png"
})

response_store_json = response_store.json()
response_store_success = response_store_json["success"]
if response_store_success:
    print("Successfully added a new image to the image service! id is:", response_store_json["image_id"])
else:
    print("Problem storing a new image to the image service! error message is: \n    \"" + response_store_json["error_message"] + "\"")

# GET an image path from the image service
response_get = requests.get(SERVICE_URL + "/get_data", json={
    "image_name": "rooster",
})
response_get_json = response_get.json()
fetched_image_path = response_get_json["image_path"]
print("fetched image path:", fetched_image_path)

# PATCH an image path from the image service
response_update = requests.patch(SERVICE_URL + "/update_data", json={
    "image_name": "rooster",
    "image_path": "https://www.bing.com/happy.jpg"
})

response_change_json = response_get.json()
response_change_success = response_change_json["success"]
print("Image Path change successful?", response_change_success)