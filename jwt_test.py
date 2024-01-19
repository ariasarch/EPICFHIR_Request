import jwt
import time
import requests
import uuid

# Payload Variables, Define as Needed
client_id = ""
token_endpoint = ""
private_key_file_path = ""

# Function to read the private key
def load_private_key(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Try to load the private key, handle errors if any
try:
    private_key = load_private_key(private_key_file_path)
    print("Private key successfully loaded.")
except Exception as e:
    print(f"An error occurred while loading the private key: {e}")
    exit(1)  # Exit the script if the private key cannot be loaded

# Generate a unique jti value
unique_jti = str(uuid.uuid4())

# Create the JWT payload
payload = {
    "iss": client_id,  # Issuer: Client ID
    "sub": client_id,  # Subject: Usually the same as Issuer for client credentials grant
    "aud": token_endpoint,  # Audience: Token endpoint URL
    "exp": int(time.time()) + 300,  # Expiration time (5 minutes from now)
    "jti": unique_jti  # A unique identifier for the token generated using uuid
}

# Choose the appropriate algorithm for the key (RS384 or ES384)
algorithm = "RS384"

# Encode the JWT
client_assertion = jwt.encode(payload, private_key, algorithm=algorithm)

# Prepare the data for the token request
data = {
    "grant_type": "client_credentials",
    "scope": "launch Patient.read Observation.read Observation.search ServiceRequest.read ServiceRequest.search openid profile",
    "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
    "client_assertion": client_assertion
}

# Make the request to the token endpoint
response = requests.post(token_endpoint, data=data)

# Check if the request was successful and print the response
if response.status_code == 200:
    print("Access token obtained successfully:")
    print(response.json())
else:
    print("Failed to obtain access token. Status code:", response.status_code)
    print("Response content:", response.text)
