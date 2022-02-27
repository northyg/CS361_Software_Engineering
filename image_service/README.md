
### Author: Giselle Northy
###### CS 361 Image Microservice

### Description

This is a Python Flask app service that serves up image data. It has 3 values and accepts JSON requests (image ID, name, URL/path)
These values are then stored in a local CSV file. 
You can opt to either create entries with image URLs or store images locally in a directory.


### JSON Parameters

* Parameters and their types
  ```json
  {
    "image_id": 1,   // Type Int(UNIQUE): Image ID automatically set when new entry is added (immutable)
    "image_name": "rooster",   // Type String(UNIQUE): Name is set when new entry is added. Query value sent to service to retrieve image path
    "image_path": "https://www.bing.com/happy.jpg"   // Type String: Path is set when new entry added. Value returned by service. Can be either URL or local directory path
  }
  ```

### Endpoints

- POST
  `/store_data`
  ```json
  // example POST request - add new image name and URL
  {  
    "image_name": "rooster",
    "image_path": "https://www.bing.com/happy.jpg"
  }
  
  // returns either:
  201 Success
  {
    'image_name': 'rooster', 'image_path': 'https://www.bing.com/happy.jpg', 'image_id': '0'
  }
  
  400 Bad request
  ```
- GET
  `/get_data`
  ```json
  // example GET request - get image URL
  {
    "image_name": "rooster"
  }
  
  // returns either:
  201 Success
  {
    'image_path': 'https://www.bing.com/happy.jpg'
  }
  
  401 Unauthorized
    ```
- PATCH
  `/update_data`
  ```json
  // example PATCH request - pass the name of an existing entry and the new URL
  {
    "image_name": "rooster",
    "image_path": "https://www.bing.com/updated_image_url.jpg"
  }
  
  // returns either:
  201 Success
  {
    'image_id': '0', 'image_name': 'rooster', 'image_path': 'https://www.bing.com/updated_image_url.jpg'
  }

  400 Bad request
    ```
  
### Required to Run
#### Files:
- `app.py`: This is the 'main' image service file 
- `images.csv`: This stores the image data in rows. Install in same directory as `app.py`
#### Optional:
- Add a local directory for storing images in the same directory as `app.py`
- `scratch_1.py`: Use as reference for formatting requests in your own application and testing the app.py image service.
- Postman test collection: May need to update the request URL as needed


#### Python Modules, etc:
- Flask
- Python3
- Requests (needed for running the `scratch_1.py` file)
    * Example for Macs: `pip3 install Requests`
  - NOTE: If _your_ applications code is not Python, you will likely need a similar module to Requests to make requests to `app.py`
- Default URL and Port: 
  - IP = `"127.0.0.1"`
  - PORT = `8081`

### How to run

* Clone the repo from Github
* Open a new terminal and navigate to the directory
* Ensure Flask is installed
* Run app.py example:
    * `python3 app.py`
  
#### Next...
* Run your application or the included test file in a different Terminal aka process
* Pass well formed JSON requests per the examples above JSON and Endpoint examples to the `app.py` image service
  * Add some data with a POST Request
  * Test it with a GET Request
  * Test updating the image_path with a PATCH request
      
NOTE: If `image_path` is a local directory, suggested create a new image directory in the same directory as the application is running from.

### Known Limitations

* Once image data is added, image names and ID number cannot be updated in the PATCH request; only image URLs can
* Image names and ID number must be unique