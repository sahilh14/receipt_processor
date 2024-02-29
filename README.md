# receipt_processor

### 2 ways to start the server -

**1. Build the image using the dockerfile and start the server :-**

Run the following commands -

docker build -t receipt_processor_ubuntu .

docker run -p 8000:8000 receipt_processor_ubuntu

Please open one of the following urls in the browser to access the web service -

http://localhost:8000 or http://127.0.0.1:8000

- PS - The server will NOT be accessible on 0.0.0.0:8000 -


**2. Download the docker image that has been built for this web service :-**

Run the command to pull the image -

docker pull sahilh14/receipt_processor:latest

Run the command to start the web server -

docker run -p 8000:8000 sahilh14/receipt_processor:latest

Please open one of the following urls in the browser to access the web service -

http://localhost:8000 or http://127.0.0.1:8000

- PS - The server will NOT be accessible on 0.0.0.0:8000 -


### About the Project - 

This is a simple web service to accept a receipt as input and generate points based on the receipt data.
The apis are exposed through 2 simple UI forms. 

#### Apis :
**POST /receipts/process/**

Description - Takes a json as input and returns a uuid.

**GET /receipts/{id}/points/**

Description - Takes the id of type string as parameter and returns the points for the receipt with this id

