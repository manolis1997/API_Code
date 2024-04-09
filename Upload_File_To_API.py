import requests

# API endpoint where you want to send the Excel file
api_endpoint = 'http://127.0.0.1:5000/upload_file'  # Replace with your API endpoint
excel_file_path = "C:\\Users\\M.Zacharioudakis\\Desktop\\Unknown Words.xlsx"

# Prepare the files to send
files = {'file': open(excel_file_path, 'rb')}

# Send the request to the API
response = requests.post(api_endpoint, files=files)

# Check the response
if response.status_code == 200:
    print("Excel file successfully sent to the API!")
else:
    print("Failed to send Excel file. Status code:", response.status_code)