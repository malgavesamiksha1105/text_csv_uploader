# 📊 Review Analytics Dashboard

A web-based application to perform **Sentiment Analysis** on text and
CSV review data.\
It classifies reviews into **Positive, Negative, Neutral, and Spam** and
visualizes results using charts.

------------------------------------------------------------------------

## 🚀 Features

-   📂 Upload CSV file with reviews\
-   🤖 Real-time Sentiment Analysis\
-   📊 Dashboard with:
    -   Positive, Negative, Neutral, Spam counts\
    -   Table preview of reviews\
-   📈 Data Visualization:
    -   Pie Chart\
    -   Bar Graph

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Frontend: HTML, CSS, JavaScript\
-   Backend: Python (Flask)\
-   Libraries:
    -   pandas
    -   textblob / nltk
    -   flask-cors
    -   chart.js

------------------------------------------------------------------------

## 📁 Project Structure

    review-dashboard/
    │
    ├── app.py
    ├── index.html
    ├── analytics.html
    ├── charts.html
    ├── style.css
    ├── README.md

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### Install Libraries

    pip install flask pandas textblob nltk flask-cors

### Download Data

    python -m textblob.download_corpora

------------------------------------------------------------------------

## ▶️ Run Project

    py app.py

Open:

    index.html

------------------------------------------------------------------------

## 📂 CSV Format

    review
    This product is amazing
    Worst experience ever

------------------------------------------------------------------------

## 👩‍💻 Author

Samiksha Malgave
