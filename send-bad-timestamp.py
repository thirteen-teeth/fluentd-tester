import requests
import time
import json
# ignore insecure request warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Variables
OPENSEARCH_URL = "http://localhost:80/_bulk"
INDEX_NAME = "my-test-error"
TIMESTAMP = int(time.time())  # Current Unix timestamp
MESSAGE = "This is a test message with a bad timestamp"
USERNAME = "admin"
PASSWORD = "admin"


# Create the index if it doesn't exist
def create_index():
    create_index_url = f"http://localhost:80/{INDEX_NAME}"
    headers = {"Content-Type": "application/json"}
    data = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "@timestamp": {
                    "type": "date"
                },
                "message": {
                    "type": "text"
                }
            }
        }
    }
    response = requests.put(create_index_url, headers=headers, data=json.dumps(data), auth=(USERNAME, PASSWORD), verify=False)
    print(f"Create index response: {response.status_code} - {response.text}")

# Uncomment the following line to create the index
# create_index()
# Create the JSON payload with a bad timestamp
# The timestamp is intentionally set to a string to simulate a bad timestamp
payload = (
    f'{{ "index": {{ "_index": "{INDEX_NAME}" }} }}\n'
    f'{{ "@timestamp": "abc123", "message": "{MESSAGE}" }}\n'
)

# Send the request
response = requests.post(
    OPENSEARCH_URL,
    auth=(USERNAME, PASSWORD),
    headers={"Content-Type": "application/json"},
    data=payload,
    verify=False  # Disable SSL verification
)

# Print the response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")