# -*- coding: utf-8 -*-
"""
Created on Thu May 15 09:47:03 2025

@author: user
"""

import numpy as np
import pickle
import streamlit as st


#loading the save model
loaded_model = pickle.load(open(r"c:/Users/user/Desktop/Machine learning pratice/Deploy diabtes prediction Model using streamlit/trained_model.sav", 'rb'))

# creating a function for prediction

def diabtes_prediction(input_data):

    # input data into numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped) # imp line
    print(prediction)

    if (prediction[0]==0):
      return('The person is not diabetic')
    else:
      return('The person is diabetic')


def main():
    
    # giving a title
    st.title('diabetes prediction web App')
    
    # getting thr input data from the user
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        # Convert input values to appropriate numerical types (float)
        try:
            pregnancies = float(Pregnancies)
            glucose = float(Glucose)
            bloodpressure = float(BloodPressure)
            skinthickness = float(SkinThickness)
            insulin = float(Insulin)
            bmi = float(BMI)
            diabetespedigreefunction = float(DiabetesPedigreeFunction)
            age = float(Age)

            diagnosis = diabtes_prediction([pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, diabetespedigreefunction, age])
        except ValueError:
            st.error("Please enter valid numerical values for all the features.")

    st.success(diagnosis)

    

if __name__ == '__main__':
    main()

    
