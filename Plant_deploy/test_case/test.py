import requests
import base64
import json

url = "https://endpt-plant-dis-03251606792664.westus.inference.ml.azure.com/score"

aml_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjU3RDM5QjFFRjkzRDg0NTRGMkMzQjcyNUE1NDRDQzk0NzA5MUFGNDYiLCJ0eXAiOiJKV1QifQ.eyJjYW5SZWZyZXNoIjoiRmFsc2UiLCJ3b3Jrc3BhY2VJZCI6IjNiNGFlMmFlLTUzMGEtNDcwNi1iNDg4LWExODhhNDEwNDkyZSIsInRpZCI6ImM3YjAwZDdmLWFkOTktNDQyYS1iMTJmLWMyYzkxMjA0NGZkYyIsIm9pZCI6IjY3OTljOGM3LWE4YmYtNDAyMC1hZTY4LTgxNWM1ZTJhMDdiMiIsImFjdGlvbnMiOiJbXCJNaWNyb3NvZnQuTWFjaGluZUxlYXJuaW5nU2VydmljZXMvd29ya3NwYWNlcy9vbmxpbmVFbmRwb2ludHMvc2NvcmUvYWN0aW9uXCJdIiwiZW5kcG9pbnROYW1lIjoiZW5kcHQtcGxhbnQtZGlzLTAzMjUxNjA2NzkyNjY0Iiwic2VydmljZUlkIjoiZW5kcHQtcGxhbnQtZGlzLTAzMjUxNjA2NzkyNjY0IiwiZXhwIjoxNzQyOTg3NDAwLCJpc3MiOiJhenVyZW1sIiwiYXVkIjoiYXp1cmVtbCJ9.tlYcLXvgAKnFSFJE2nBxNTR7iQDRZvkC75Ng5cZyk3bqHnn7AkSIJOxnXPXIUNaZqKG-TUVgd45bHLAJdxiXxsuG1fvtq1PsjmXPdySxJPcNDz2jdHCdcm7Ug2MgtOFpVMZ1X6HQlv0zeO68_lRT7ZZRo87Sdnnnnc6mI4t89yHQ8cc17KluEC4dHBeL6HNtoNcKjCazoPAAr-cPq00z4TwiO7mzEcXT3k58VKbBO1Vcya40h6eRV9fZ_zw8zBwQGYyDQucllgv4RYDIW_vXAQtD7dEiyV4NbVtgI5tUMHXa5UPoykfPFOZ9fN6pLT7EbNUriwPMpXsq7DNFB2he9Q"


# Create headers with the API key
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {aml_token}"
}

# Read the image
# with open('test_apple_black_rot.jpeg', 'rb') as image_file:
#     image_data = image_file.read()

with open('test_blueberry_healthy.jpg', 'rb') as image_file:
    image_data = image_file.read()
    

# Convert image to base64
image_base64 = base64.b64encode(image_data).decode('utf-8')

# Construct the JSON payload
json_payload = {
    "data": image_base64
}

# Send the POST request with the JSON payload
response = requests.post(url, json=json_payload, headers=headers)

# Convert the string to a dictionary
prediction = json.loads(response.json())

# Now dict_data is a Python dictionary
print(prediction)