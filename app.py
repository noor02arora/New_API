from flask import Flask, request, jsonify, render_template
import mimetypes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file:
        filename = uploaded_file.filename
        file_type, _ = mimetypes.guess_type(filename)
        return jsonify({
            'filename': filename,
            'info': file_type
        })
    return jsonify({'error': 'No file uploaded'})

if __name__ == '__main__':
    app.run(port=5500, debug=True)
