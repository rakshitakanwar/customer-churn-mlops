# Customer-churn-pipeline

An end-to-end **Machine Learning Operations (MLOps)** project that predicts customer churn using **Scikit-learn** and deploys the model on **Amazon SageMaker**. The project includes data preprocessing with **AWS Glue Visual ETL**, model deployment, serverless inference using **AWS Lambda**, API exposure through **Amazon API Gateway**, a **Flask** web application, and **Docker** containerization.

---

## Project Overview

Customer churn prediction helps organizations identify customers who are likely to discontinue a service. This project demonstrates the complete lifecycle of a machine learning application on AWS—from data ingestion and preprocessing to model deployment and real-time prediction.

The dataset is cleaned using **AWS Glue Visual ETL**, stored in **Amazon S3**, used to train a **Random Forest Classifier**, deployed to **Amazon SageMaker**, and served through **Lambda** and **API Gateway**. A Flask web application provides an easy-to-use interface for prediction.

---

## Architecture

```
                    Customer Churn Dataset
                             │
                             ▼
                      Amazon S3 (Raw Data)
                             │
                             ▼
                  AWS Glue Visual ETL
                             │
                             ▼
                   Amazon S3 (Clean Data)
                             │
                             ▼
               Scikit-learn Model Training
                             │
                             ▼
            model.joblib + model.tar.gz
                             │
                             ▼
                 Amazon SageMaker Endpoint
                             │
                             ▼
                    AWS Lambda Function
                             │
                             ▼
                  Amazon API Gateway
                             │
                             ▼
                Flask Web Application
                             │
                             ▼
                    Docker Container
```

---

# Features

- End-to-End MLOps Workflow
- Data preprocessing using AWS Glue Visual ETL
- Data storage using Amazon S3
- Machine Learning with Scikit-learn
- Model deployment using Amazon SageMaker
- Serverless inference with AWS Lambda
- REST API using Amazon API Gateway
- Interactive Flask Web Application
- Dockerized Deployment

---

# Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS
- Bootstrap
- Docker
- AWS S3
- AWS Glue
- Amazon SageMaker
- AWS Lambda
- Amazon API Gateway
- IAM
- Git
- GitHub
---

# Workflow

## Step 1 – Upload Dataset

Upload the Customer Churn dataset to an Amazon S3 bucket.

---

## Step 2 – Data Preprocessing

Use AWS Glue Visual ETL to:

- Read the dataset from Amazon S3
- Clean and transform the data
- Handle missing values
- Save the processed dataset back to Amazon S3

---

## Step 3 – Model Training

Load the cleaned dataset from Amazon S3.

Preprocessing includes:

- Feature Selection
- Label Encoding
- Train-Test Split

Train a Random Forest Classifier using Scikit-learn.

Save the trained model as:

```
model.joblib
```

Compress the model into:

```
model.tar.gz
```

Upload the compressed model to Amazon S3.

---

## Step 4 – Model Deployment

Deploy the model on Amazon SageMaker using a custom inference script.

The inference script performs:

- Model Loading
- Input Processing
- Prediction
- Output Formatting

---

## Step 5 – Lambda Function

AWS Lambda receives prediction requests from API Gateway and forwards them to the SageMaker endpoint.

---

## Step 6 – API Gateway

Amazon API Gateway exposes a REST endpoint that allows external applications to request predictions.

---

## Step 7 – Flask Application

The Flask application provides a user-friendly interface.

Input Features:

- Customer Tenure
- Monthly Charges
- Contract Type

The application sends these values to API Gateway and displays the prediction result.

---

## Step 8 – Docker

Containerize the Flask application using Docker for easy deployment.

---

# Machine Learning Model

**Algorithm**

Random Forest Classifier

### Input

- Tenure
- Monthly Charges
- Contract Type

### Output

- Yes (Customer will churn)
- No (Customer will not churn)

---

# Installation

Clone Repository

```bash
git clone https://github.com/your-username/customer-churn-mlops-pipeline.git
```

Move into the project

```bash
cd customer-churn-mlops-pipeline
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Flask

```bash
python app.py
```

Open your browser

```
http://localhost:5000
```

---

# Docker

Build Docker Image

```bash
docker build -t customer-churn .
```

Run Container

```bash
docker run -d -p 5000:5000 customer-churn
```

---

# Sample API Request

```json
{
    "tenure":72,
    "monthlycharges":42.1,
    "contract":"Two year"
}
```

---

# Sample API Response

```json
{
    "Churn Prediction":"No"
}
```

---

# AWS Services Used

- Amazon S3
- AWS Glue (Visual ETL)
- Amazon SageMaker
- AWS Lambda
- Amazon API Gateway
- AWS IAM

---

# Future Enhancements

- MLflow Experiment Tracking
- CI/CD using GitHub Actions
- Amazon ECR
- Kubernetes Deployment
- CloudWatch Monitoring
- Model Versioning
- Automated Retraining Pipeline

---

# Screenshots

Add screenshots of:

- Home Page
- Prediction Result
- AWS Glue Visual ETL Job
- Amazon S3 Bucket
- SageMaker Endpoint
- Lambda Function
- API Gateway
- Docker Container

---

# Author

**Rakshita Kanwar**

B.Tech – Computer Science (Artificial Intelligence)

Arya College of Engineering, Jaipur

---

# License

This project is developed for educational and learning purposes.
