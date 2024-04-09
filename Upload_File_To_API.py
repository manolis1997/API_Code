import requests

api_endpoint = 'url'
excel_file_path = "File Path"

files = {'file': open(excel_file_path, 'rb')}

# Send the request to the API
response = requests.post(api_endpoint, files=files)

if response.status_code == 200:
    print("Excel file successfully sent to the API!")
else:
    print("Failed to send Excel file. Status code:", response.status_code)