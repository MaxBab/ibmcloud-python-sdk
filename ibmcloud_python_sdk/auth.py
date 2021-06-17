import http.client
import gzip
import json

def get_token(url, key):
    # URL for token
    conn = http.client.HTTPSConnection(url)

    # Payload for retrieving token
    payload = f"grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey={key}"

    # Required headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
    }

    try:
        # Connect to endpoint for retrieving a token
        conn.request("POST", "/identity/token", payload, headers)

        # Get and read response data
        res = conn.getresponse().read()
        data = res.decode("utf-8")

        # Format response in JSON
        json_res = json.loads(data)

        # Concatenate token type and token value
        return json_res['token_type'] + ' ' + json_res['access_token']

    # If an error happens while retrieving token
    except Exception as error:
        print(f"Error getting token. {error}")
        raise
