# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:31:17 2024

@author: Sandeep
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetics_model = pickle.load(open('trained_model.sav', 'rb'))
heart_model = pickle.load(open('trained_model_1.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disesase Prediction',
                           ['Diabetics Prediction', 'Heart Disease Prediction'],
                           icons=['activity', 'heart'],
                           default_index=0)
    
    
if (selected=='Diabetics Prediction'):    
    st.title('Diabetic Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies:")
    with col1:
        Glucose = st.text_input("Glucose Level:")
    with col1:
        BloodPressure = st.text_input("Blood Pressure:")
    with col2:
        SkinThickness = st.text_input("SkinThickness:")
    with col2:
        Insulin = st.text_input("Insulin Level:")
    with col2:
        BMI = st.text_input("BMI:")
    with col3:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function:")
    with col3:
        Age = st.text_input("Age:")
    
    diabetics_diagnosis = ''
    if st.button('Diabetics Test Prediction'):
        diagnosis = diabetics_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diagnosis[0]==1:
            diabetics_diagnosis = "The Person is Diabetic"
        else:
            diabetics_diagnosis = "The Person is NOT Diabetic"
    
    st.success(diabetics_diagnosis)
    
    
elif (selected=='Heart Disease Prediction'):    
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Age	= st.text_input("Age:") 
    with col1:
        Sex	= st.text_input("Gender:") 
    with col1:    
        Cp = st.text_input("CP:") 
    with col2:
        TrestBPs = st.text_input("TrestBPs:") 
    with col2:
        Chol = st.text_input("Chol:") 
    with col2:
        Fbs	= st.text_input("Fbs:") 
    with col3:
        Restecg = st.text_input("Restecg:") 	
    with col3:
        Thalach	= st.text_input("Thalach:") 
    with col3:
        Exang = st.text_input("Exang:") 
    with col4:
        Oldpeak	= st.text_input("Oldpeak:") 
    with col4:
        Slope = st.text_input("Slope:") 
    with col4:
        Ca = st.text_input("Ca:") 
    with col4:
        Thal = st.text_input("Thal:") 
        
    heart_diagnosis = ''
    if st.button('Heart Disease Prediction'):
        diagnosis = heart_model.predict([[Age, Sex, Cp, TrestBPs, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]])
        
        if diagnosis[0]==1: 
            heart_diagnosis = "The Person has Heart Condition"
        else:
            heart_diagnosis = "The Person DOESN'T have any Heart Condition"
    
    st.success(heart_diagnosis)
