# Advanced Fake Job Post Prediction Using Machine Learning for Online Recruitment Scam Detection

## Project Overview
The rapid growth of online recruitment platforms has led to a significant increase in fake job postings. These fraudulent advertisements cause financial loss, emotional stress, and loss of trust among job seekers. Manual identification of such fake job posts is time-consuming and inefficient. This project proposes a machine learning–based solution to automatically detect fraudulent job postings and help users make safer career decisions.

## Objective
The main objective of this project is to develop a web-based application that uses machine learning and natural language processing techniques to classify job postings as either **Real** or **Fake**, thereby preventing online recruitment scams.

## Abstract
With the increasing use of online job portals, recruitment scams have become more common. This project uses supervised machine learning algorithms and NLP techniques to analyze job descriptions and related features. Multiple classifiers are trained and evaluated to identify fraudulent postings effectively. Model performance is measured using accuracy, precision, recall, and F1-score. The results demonstrate that advanced classification techniques can significantly improve fraud detection accuracy and enhance trust in online job platforms.

## Existing System
Existing systems rely on basic machine learning models to detect fake job postings using job-related textual and categorical data. Although these approaches provide reasonable accuracy, they often lack proper optimization, comparative analysis of models, and scalability. This creates a need for a more efficient and reliable detection system.

## Proposed System
The proposed system introduces an intelligent fake job detection framework using Python, machine learning, and NLP techniques. The system analyzes job posting content and predicts whether it is legitimate or fraudulent. Multiple classification models are implemented and compared to improve prediction accuracy. The system is deployed as a web application using Flask, making it easy for users to test job descriptions in real time.

## Machine Learning Models Used
- MLP Classifier (High training and testing accuracy)
- Passive Aggressive Classifier
- Gradient Boosting Classifier
- K-Nearest Neighbors Classifier

Among these, the MLP Classifier is used for final deployment due to its superior performance.

## Dataset
The model is trained using a real-world employment scam dataset containing thousands of job postings. The dataset includes features such as job title, company profile, job description, employment type, required experience, required education, and fraud status.

## Data Preprocessing
Data preprocessing includes:
- Handling missing values
- Removing duplicate records
- Text cleaning and normalization
- Feature selection
- Train-test data splitting

Only important features such as job description and employment-related attributes are used for prediction.

## Exploratory Data Analysis (EDA)
EDA is performed to understand the dataset structure and identify patterns. Various statistical and visualization techniques are applied to analyze feature distributions, correlations, and fraud trends.

## Data Visualization
Data visualization techniques such as bar charts, histograms, and heatmaps are used to clearly represent the distribution of real and fake job postings and the relationship between different features.

## Project Modules
- Data Collection
- Data Preprocessing
- Exploratory Data Analysis
- Model Training and Evaluation
- Web Application Development
- Deployment

## System Architecture
1. User inputs job description through the web interface
2. Input is processed using NLP techniques
3. Trained machine learning model predicts the result
4. Prediction is displayed as Real or Fake job post

## Technologies Used
- Python 3
- Flask
- Machine Learning (Scikit-learn)
- NLP (NLTK / SpaCy)
- Pandas, NumPy
- HTML, CSS

## Project Structure

## Installation and Execution
1. Install required dependencies:
2. Run the Flask application:
3. Open a browser and navigate to:

## Deployment
The application is deployed on a live server to allow public access. The live hosted link can be used to test the prediction system in real time.

Live URL: https://your-live-link-here

## GitHub Repository
Repository Link: https://github.com/your-username/your-repository-name

## Evaluation Metrics
The model performance is evaluated using:
- Accuracy
- Precision
- Recall
- F1-score

## Conclusion
This project successfully demonstrates the use of machine learning and NLP techniques to detect fake job postings. The system helps job seekers avoid recruitment scams and improves trust in online recruitment platforms by providing accurate and reliable predictions.

## Author
Name: G. Harika  
College: ANITS  
Department: B.Tech Information Technology
