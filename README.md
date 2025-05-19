# Diabetes-Prediction-Web-Application

This repository contains the code for a web application that predicts whether a person has diabetes based on several health features. The application is built using Streamlit, a Python library for creating interactive web apps for machine learning.

## Overview

The project includes the following components:

* **`Deploy diabtes prediction Model using streamlit.ipynb`**: A Jupyter Notebook detailing the process of building and deploying the diabetes prediction model using Streamlit. It covers data loading, preprocessing, model training (using a Support Vector Machine), model evaluation, and saving the trained model.
* **`diabtes prediction web app.py`**: The Python script for the Streamlit web application. It loads the trained model, creates a user interface with input fields for relevant health features, and displays the prediction result.
* **`predictive system.py`**: A standalone Python script that demonstrates how to load the saved model and make predictions for sample input data.
* **`trained_model.sav`**: (This file is assumed to be present, as mentioned in the code) The saved, trained machine learning model in a pickle format.
* **`requirements.txt`**: (This file is expected) A list of Python libraries required to run the application. This allows for easy installation of dependencies.

## Setup and Usage

Follow these steps to run the diabetes prediction web application locally:

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
    Replace `<repository_url>` with the actual URL of your GitHub repository and `<repository_name>` with the name of the cloned directory.

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```
    or
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **On Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **On macOS and Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Ensure you have a `requirements.txt` file in your repository. You can generate one by running `pip freeze > requirements.txt` after installing the necessary libraries like `numpy`, `pandas`, `scikit-learn`, `streamlit`, and `pickle`.)*

5.  **Run the Streamlit Application:**
    ```bash
    streamlit run diabtes prediction web app.py
    ```
    This command will launch the web application in your default web browser.

## How to Use the Web Application

1.  Once the application is running in your browser, you will see a title "diabetes prediction web App" and input fields for various health parameters such as Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, and Age.
2.  Enter the corresponding values for each feature.
3.  Click the "Diabetes Test Result" button.
4.  The application will process the input using the loaded machine learning model and display the prediction: "The person is not diabetic" or "The person is diabetic".

## Code Highlights

* **`Deploy diabtes prediction Model using streamlit.ipynb`**:
    * Loads the diabetes dataset using pandas (`pd.read_csv()`).
    * Trains a Support Vector Machine (SVM) model using scikit-learn (`svm.SVC()`).
    * Saves the trained model to a file named `trained_model.sav` using the `pickle` library (`pickle.dump()`).
* **`diabtes prediction web app.py`**:
    * Loads the trained model from `trained_model.sav` using `pickle.load()`.
    * Uses Streamlit (`streamlit as st`) to create the web interface with input fields (`st.text_input()`) and a button (`st.button()`).
    * The `diabtes_prediction()` function takes user inputs, reshapes them, and uses the loaded model's `predict()` method to get the prediction.
    * Displays the prediction result using `st.success()`.
* **`predictive system.py`**:
    * Loads the trained model.
    * Demonstrates making a prediction for a sample data point using the loaded model.

## Contributing

Contributions to this project are welcome. Feel free to fork the repository and submit pull requests with improvements or bug fixes.
