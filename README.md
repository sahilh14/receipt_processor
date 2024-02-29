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

### Once you have the server running, you can access the endpoints directly also through curl - 

**/receipts/process/ as Curl -**

```
curl 'http://localhost:8000/receipts/process/' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: csrftoken=YnfqKZwHSWCXQB2Pa1ZxrsgdRwA08UpB' \
  -H 'Origin: http://localhost:8000' \
  -H 'Referer: http://localhost:8000/receipt_input_page/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
  -H 'X-CSRFToken: YnfqKZwHSWCXQB2Pa1ZxrsgdRwA08UpB' \
  -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw $'{\n  "retailer": "M&M Corner Market",\n  "purchaseDate": "2022-03-20",\n  "purchaseTime": "14:33",\n  "items": [\n    {\n      "shortDescription": "Gatorade",\n      "price": "2.25"\n    },{\n      "shortDescription": "Gatorade",\n      "price": "2.25"\n    },{\n      "shortDescription": "Gatorade",\n      "price": "2.25"\n    },{\n      "shortDescription": "Gatorade",\n      "price": "2.25"\n    }\n  ],\n  "total": "9.00"\n}' \
  --compressed
```

**/receipts/{id}/points/ as curl -** 

**replace the {id} with the actual id**

```
curl 'http://localhost:8000/receipts/{id}/points/' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Cookie: csrftoken=YnfqKZwHSWCXQB2Pa1ZxrsgdRwA08UpB' \
  -H 'Referer: http://localhost:8000/id_input_page/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --compressed
  ```

