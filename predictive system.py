# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the save model
loaded_model = pickle.load(open(r"c:/Users/user/Desktop/Machine learning pratice/Deploy diabtes prediction Model using streamlit/trained_model.sav", 'rb'))


# input_data = (4,110,92,0,0,37.6,0.191,30)  not diabetic 
input_data = (5,166,72,19,175,25.8,0.587,51)  # diabetic

# input data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped) # imp line
# print(prediction)

if (prediction[0]==0):
  print('The person is not diabetic')
else:
  print('The person is diabetic')
