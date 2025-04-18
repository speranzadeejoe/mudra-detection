# mudra-detection
---

# Mudra Detection Web App

This is a **Mudra Detection Web Application** built with **Flask**, where users can upload images of mudras, and the app predicts the mudra using a trained model via **Roboflow**. The app is deployed on **Render** and is publicly accessible.

[Check out the live app here!](https://mudrarecognition.onrender.com/)

---

## Features

- **Upload Image**: Users can upload an image of a mudra.
- **Prediction**: Once the image is uploaded, the app predicts the mudra and provides the prediction confidence.
- **Image Preview**: Shows the uploaded image once it's uploaded successfully.
- **Publicly Accessible**: The app is deployed on Render and is accessible to anyone.

---

## Technologies Used

- **Flask**: A lightweight Python web framework for building web apps.
- **Gunicorn**: A WSGI HTTP Server for running Python web applications in production.
- **Roboflow**: Used for mudra recognition (image classification).
- **Render**: Platform for deploying web services.

---

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/mudra-detection.git
cd mudra-detection
```

### 2. Create a Virtual Environment

It is recommended to create a virtual environment to manage your dependencies.

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Running Locally

To run the app locally, execute the following command:

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000/`.

### 5. Environment Variables (Optional)

If you are using **Roboflow** or other external APIs, store your API keys in a `.env` file:

```
ROBOFLOW_API_KEY=your_roboflow_api_key
```

Ensure you have the `python-dotenv` package in `requirements.txt`.

---

## Deployment

This app is deployed on **Render**.

1. Go to [Render](https://render.com).
2. Connect your GitHub repository to Render.
3. Choose a **Python Web Service**.
4. Set the **Build Command** (Render auto-detects it):
   - `pip install -r requirements.txt`
5. Set the **Start Command**:
   - `gunicorn app:app`
6. Click **Create Web Service**.

Once deployed, Render will provide a public URL where your app will be accessible.

---

## Folder Structure

```
mudra-detection/
├── app.py                    # Main Flask app
├── static/
│   └── uploaded/
│       └── .gitkeep          # Placeholder for empty uploaded folder
├── templates/
│   └── index.html            # HTML page for the web interface
├── requirements.txt          # Dependencies
├── Procfile                  # Render configuration
├── .gitignore                # Ignore unnecessary files
└── .env                      # (Optional) For API keys and environment variables
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
