# Diamond Price Prediction Machine
![Diamond](/images/blue.jpg)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Data Version Control (DVC)](#data-version-control-dvc)
- [Running the Flask Web App](#running-the-flask-web-app)
- [Usage](#usage)
- [Project Demo](#project-demo)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Introduction

Diamond Price Prediction is a machine learning project that predicts the price of diamonds based on various features like carat, cut, color, clarity, depth, table, and dimensions (x, y, z). This project combines data version control (DVC) to manage datasets, a machine learning model for predictions, and a Flask web application for easy interaction.

## Features

- Predicts the price of diamonds using a machine learning model.
- Manages datasets and model versions with DVC.
- Provides a user-friendly web interface to input diamond features and get price predictions.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

   - git clone https://github.com/Fortunatetech/Diamond-Price-Prediction-with-DVC-Flask-Streamlit.git
   - cd diamond-price-prediction

2. Create a virtual environment and install dependencies:

   - python -m venv venv
   - source venv/bin/activate # On Windows, use `venv\Scripts\activate`
   - pip install -r requirements.txt

3. [Optional] Install DVC and set up DVC remotes for dataset version control.

## Getting Started

Before running the Flask web application, you'll need to follow these steps:

## Data Version Control (DVC)

1. Initialize DVC and set up DVC remotes for data storage:
   'dvc init'
2. Add your data source (e.g., a URL or local path) to DVC:
   dvc add data/diamonds.csv
3. Commit your code:
   dvc commit -m "Add dataset"
4. Push the data to a DVC remote (e.g., AWS S3 or Google Cloud Storage):
   dvc push

## Running the Flask Web App

python app.py
The web app should now be running locally. Access it in your web browser at http://localhost:5000.

## Usage

1. Access the Flask web application via your browser.

2. Enter the diamond's features: carat, cut, color, clarity, depth, table, x, y, and z.

3. Click the "Get Prediction" button to obtain the predicted diamond price.

## Project Demo
[diamond price prediction.webm](https://github.com/Fortunatetech/Diamond-Price-Prediction-with-DVC-Flask-Streamlit/assets/104451288/572d6e4c-dcb7-41da-bfe6-628e7361b2d0)

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow the contribution guidelines.

## License

This project is licensed under the MIT License.

## Contact Information

For any questions or inquiries, feel free to reach out:

- GitHub: [GitHub](https://github.com/Fortunatetech)
- LinkedIn: [LinkedIn](https://www.linkedin.com/in/ayo-ayodeji/)
- Email: ayodeleayode250@gmail.com
