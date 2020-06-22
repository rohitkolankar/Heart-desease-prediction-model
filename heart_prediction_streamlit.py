# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:55:54 2020

@author: HP
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifierheart.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(age,sex,cp,trestbph,chol,fbs,thalach,oldpeak,restecg,exang,slope,ca,thal):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    list = [age,sex,cp,trestbph,chol,fbs,thalach,oldpeak,restecg,exang,slope,ca,thal]
    new = np.array(list,dtype=np.float32)
    prediction=classifier.predict([new])
    print(prediction)
    return prediction



def main():
    st.title("Heart Disease prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Heart disease prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("age","Type Here")
    sex = st.text_input("sex","Type Here")
    cp = st.text_input("cp","Type Here")
    trestbph = st.text_input("trestbph","Type Here")
    chol= st.text_input("chol","Type Here")
    fbs = st.text_input("fbs","Type Here")
    restecg = st.text_input("restecg","Type Here")
    thalach= st.text_input("thalach","Type Here")
    exang = st.text_input("exang","Type Here")
    slope = st.text_input("slope","Type Here")
    oldpeak = st.text_input("oldpeak","Type Here")
    ca= st.text_input("ca","Type Here")
    thal= st.text_input("thal","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(age,sex,cp,trestbph,chol,fbs,thalach,oldpeak,restecg,exang,slope,ca,thal)
    if result=='':
        st.success('Please Enter the data')
    elif result==0:
        st.success('You have no heart desease. your output is {}'.format(result))
    else:
        st.success('You have heart desease. your output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    