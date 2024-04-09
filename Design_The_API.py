from flask import Flask, jsonify, request
from fastapi import FastAPI, UploadFile

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return 'Hello'

# http://ip:port/drinks -> {
#   "tsikoudia": "crete",
#   "vodka": "russia",
#   "whiskey": "irish"
# }

# http://ip:port/drinks?extra_drink=tekila -> {
#   "tekila": "mexico",
#   "tsikoudia": "crete",
#   "vodka": "russia",
#   "whiskey": "irish"
# }
@app.route('/drinks', methods=['GET'])
def get_drinks():
    if request.method == 'GET':
        drinks = {
            'tsikoudia':'crete',
            'vodka':'russia',
            'whiskey':'irish'
        }

        drink = request.args.get("extra_drink")
        if drink == 'tekila':
            drinks["tekila"] = 'mexico'

        return jsonify(drinks),200


@app.route('/upload_file', methods=['POST'])
def upload():
    if request.method == 'GET':
        import os
        upload_file = request.files['file']
        destination = os.path.join('uploads/',upload_file.filename)
        upload_file.save(destination)

        return {'data': 'File Uploaded '}


if __name__ == '__main__':
    app.run(debug=True)