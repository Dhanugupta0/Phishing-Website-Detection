Phishing Website Detection 🛡️

A machine learning-powered web application for detecting phishing websites. This project automates data ingestion, validation, transformation, model training, and prediction, providing a FastAPI interface for both training and inference.

🚀 Features

Automated Data Ingestion: Connects to MongoDB, extracts website/network data, and stores it locally.

Data Validation & Transformation: Ensures data quality and prepares it for modeling.

Model Training Pipeline: Trains and saves machine learning models for phishing detection.

Prediction API: Upload CSV files to get phishing predictions via a web interface.

HTML Results: Returns predictions in a clean, styled HTML table.

CORS Enabled: Accessible from any origin.

Cloud Ready: Artifacts and models can be synced to AWS S3.

Docker Compatible: Easily containerize and deploy.

🛠️ Installation
1. Clone the Repository
git clone https://github.com/Dhanugupta0/phishing-website-detection.git
cd phishing-website-detection

2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Set up Environment Variables

Create a .env file in the root directory and add your configuration, for example:

MONGO_URI=<your_mongodb_connection_string>
AWS_ACCESS_KEY_ID=<your_aws_key>
AWS_SECRET_ACCESS_KEY=<your_aws_secret>

⚡ Usage
Start the FastAPI Server
uvicorn main:app --reload


Visit: http://127.0.0.1:8000/docs to access the interactive API documentation.

Make Predictions

Upload a CSV file containing website URLs to the /predict endpoint to get phishing detection results.
```bash
📁 Project Structure
├── app.py                # FastAPI application entry
├── main.py               # Server main script
├── final_model/          # Saved ML models
├── networksecurity/      # Feature extraction scripts
├── templates/            # HTML templates for results
├── valid_data/           # Validated dataset for training
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── Dockerfile            # Containerization setup
```
🤖 Model & Data

Machine Learning Model: Random Forest / XGBoost (configurable)

Data Source: Website and network features from MongoDB

Prediction: Classifies URLs as Phishing or Legitimate

📦 Docker Deployment

Build the Docker image:

docker build -t phishing-detector .


Run the container:

docker run -p 8000:8000 phishing-detector

🌐 Cloud Integration

AWS S3 sync for models and artifacts

Can be deployed to any cloud provider supporting Docker

✨ Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
