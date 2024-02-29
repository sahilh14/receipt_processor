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

docker pull sahilh14/work:receipt_processor_v1

Run the command to start the web server -

docker run -p 8000:8000 sahilh14/work

Please open one of the following urls in the browser to access the web service -

http://localhost:8000 or http://127.0.0.1:8000

- PS - The server will NOT be accessible on 0.0.0.0:8000 -
