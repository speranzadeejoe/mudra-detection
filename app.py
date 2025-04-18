from flask import Flask, render_template, request
from inference_sdk import InferenceHTTPClient
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = os.path.join('static', 'uploaded')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Roboflow API setup
client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="XRTFbdYqMOqpnoNATZKq"  # 🔁 Replace with your actual API key from Roboflow
)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    filename = None

    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # Roboflow Prediction
                result = client.run_workflow(
                    workspace_name="mudra-detection",      # 👈 From your workflow
                    workflow_id="custom-workflow",         # 👈 From your workflow
                    images={"image": filepath},
                    use_cache=True
                )
                prediction = result
            except Exception as e:
                prediction = {"error": str(e)}

    return render_template('index.html', prediction=prediction, filename=filename)

if __name__ == '__main__':
       pass

