from flask import Flask, request, jsonify
import requests
import uuid
import os

app = Flask(__name__)
# app.config.from_object('config')
from flask_cors import CORS

CORS(app)


@app.route('/download_images', methods=['POST'])
def download_images():
    image_urls = request.json.get('image_urls', [])
    isLike = request.json.get('isLike', False)
    results = []

    # Define folders
    folder_like = '/Users/nuttawatjanwisit/Desktop/nut/ml/test'
    folder_not_like = '/Users/nuttawatjanwisit/Desktop/nut/ml/test'

    # Check and create folders if they don't exist
    if not os.path.exists(folder_like):
        os.makedirs(folder_like)
    if not os.path.exists(folder_not_like):
        os.makedirs(folder_not_like)

    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                filename = f'image_{uuid.uuid4()}.webp'
                # Choose folder based on isLike flag
                folder = folder_like if isLike else folder_not_like
                filepath = os.path.join(folder, filename)
                with open(filepath, 'wb') as file:
                    file.write(response.content)
                results.append({'url': url, 'status': 'success', 'filename': filepath})
            else:
                results.append({'url': url, 'status': 'error', 'reason': 'Non-200 response'})
        except requests.RequestException as e:
            results.append({'url': url, 'status': 'error', 'reason': str(e)})
    
    return jsonify(results)

app.run(debug=True)
