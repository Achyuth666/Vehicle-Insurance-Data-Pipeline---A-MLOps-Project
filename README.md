# 🚗💼 **Vehicle Insurance MLOps Project**

### **End-to-End Production-Ready ML Pipeline | Cloud Integrated | CI/CD Automated**

> A complete MLOps implementation showcasing how machine learning systems are built, validated, versioned, containerized, and deployed in real-world environments.

Designed to demonstrate **production engineering skills** expected from an **MLOps Engineer**.

---

# 🏗️ **System Architecture**

```
MongoDB Atlas (Cloud Database)
        ↓
Data Ingestion Pipeline
        ↓
Data Validation (Schema-Based)
        ↓
EDA & Feature Engineering
        ↓
Data Transformation Pipeline
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Registry (Amazon S3)
        ↓
Dockerized Flask API
        ↓
CI/CD via GitHub Actions
        ↓
Deployment on EC2
```

This architecture ensures:

* 🔁 Reproducibility
* 📦 Artifact tracking
* ☁️ Cloud-native deployment
* ⚙️ Automation-first workflow

---

# 🛠️ **Tech Stack & Tools**

| Category           | Tools & Services                  |
| ------------------ | --------------------------------- |
| Database           | MongoDB Atlas                     |
| Programming        | Python 3.10                       |
| Cloud Platform     | Amazon Web Services               |
| Model Registry     | Amazon S3                         |
| Compute            | Amazon EC2                        |
| Containerization   | Docker                            |
| CI/CD              | GitHub Actions                    |
| Container Registry | Amazon ECR                        |
| Version Control    | GitHub                            |
| API Framework      | FastAPI                           |

---

# 🎯 **Project Objective**

Build a **_robust, modular, and cloud-integrated ML pipeline_** for Vehicle Insurance data that covers:

* Data ingestion from cloud database
* Validation & transformation
* Model training & evaluation
* Cloud model registry
* Dockerized deployment
* CI/CD automation
* AWS infrastructure integration

---

# 📁 **Project Setup & Environment**

## 🧩 Step 1: Project Template

* Executed `template.py` to generate scalable folder structure.

## 📦 Step 2: Package Management

* Configured `setup.py` and `pyproject.toml`
* Local package import enabled

## 🐍 Step 3: Virtual Environment & Dependencies

```bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt
```

Verified installation:

```bash
pip list
```

---

# 📊 **MongoDB Setup & Data Management**

## ☁️ Step 4: MongoDB Atlas Configuration

* Created project & M0 cluster in
  MongoDB Atlas
* Configured database user
* Enabled IP access (`0.0.0.0/0`)
* Stored secure connection string

## 📤 Step 5: Pushing Data to MongoDB

* Created `notebook/mongoDB_demo.ipynb`
* Uploaded dataset to MongoDB
* Verified collections in Atlas dashboard

---

# 📝 **Logging, Exception Handling & EDA**

## ⚙️ Step 6: Logging & Exception Handling

* Custom logging module
* Centralized exception handling
* Tested via `demo.py`

---

## 📈 Step 7: EDA & Feature Engineering

Performed structured EDA to:

* Analyze feature distributions
* Detect missing values
* Identify correlations
* Study target imbalance
* Engineer relevant features

All learnings converted into a **reproducible transformation pipeline** for training & inference consistency.

---

# 📥 **Data Ingestion Pipeline**

## 🔄 Step 8: Data Ingestion

* MongoDB connection via environment variables
* Config-driven ingestion logic
* Artifact generation
* Raw → processed dataset flow

### 🔐 **Environment Variable Setup**

**Bash**

```bash
export MONGODB_URL="mongodb+srv://<username>:<password>...."
```

**PowerShell**

```powershell
$env:MONGODB_URL="mongodb+srv://<username>:<password>...."
```

---

# 🔍 **Data Validation, Transformation & Training**

## ✅ Step 9: Data Validation

* YAML-based schema (`config.schema.yaml`)
* Structural & column validation
* Fail-fast validation checks

---

## 🔄 Step 10: Data Transformation

* Feature engineering logic
* Preprocessing pipeline
* Serialized transformation object
* Estimator integration

---

## 🧠 Step 11: Model Training

* Modular training component
* Train-test split
* Model artifact creation
* Evaluation-based selection

---

# ☁️ **AWS Model Registry & Deployment**

## 🔐 Step 12: AWS Setup

Configured infrastructure on
Amazon Web Services

* IAM User with permissions
* Access keys as environment variables

```bash
export AWS_ACCESS_KEY_ID="YOUR_AWS_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_AWS_SECRET_ACCESS_KEY"
```

---

## 📦 Step 13: Model Evaluation & S3 Push

* Created S3 bucket
* Implemented push/pull logic via `s3_estimator.py`
* Model versioning enabled

Using:
Amazon S3

---

# 🚀 **Prediction Pipeline & API**

## 🔎 Step 14: Model Evaluation & Pusher

* Performance comparison
* Conditional deployment
* Model registry update

## 🌐 **Prediction Pipeline**

* Flask-based REST API
* Real-time predictions
* Web UI support via `static` & `templates`

Run locally:

```bash
python app.py
```

---

# 🔄 **CI/CD with Docker & GitHub Actions**

## 🐳 Step 16: Docker Setup

* Created `Dockerfile`
* Optimized `.dockerignore`
* Containerized application

Using:
Docker

---

## ⚙️ **GitHub Actions Workflow**

Automated:

* Docker image build
* Push to ECR
* Deployment to EC2

Using:
**_GitHub Actions_**

Secrets configured in GitHub:

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_DEFAULT_REGION
* ECR_REPO
* MONGODB_URL

---

# 🖥️ **AWS EC2 & ECR Deployment**

## ☁️ Step 17: EC2 & ECR

* EC2 instance setup
* Docker installed on EC2
* Self-hosted GitHub runner
* Image pulled from ECR

Using:
Amazon EC2

---

## 🌍 Step 18: Final Deployment

* Opened port **5000**
* Application accessible at:

```
http://<public_ip>:5000
```

---

# 🔄 **Complete Workflow Overview**

```
Data Ingestion
      ↓
Data Validation
      ↓
EDA & Feature Engineering
      ↓
Data Transformation
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Registry (S3)
      ↓
Dockerization (Docker and ECR)
      ↓
CI/CD Automation (Github Actions)
      ↓
Deployment (EC2)
```

---

## ⭐ **Built with an MLOps-First Mindset**

Production-ready. Cloud-integrated. Deployment-automated.

---

## 💬 **_Connect_**
If you found this project helpful or have any questions, feel free to reach out!