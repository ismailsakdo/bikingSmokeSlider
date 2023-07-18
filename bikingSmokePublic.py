
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

model = pickle.load(open('/Users/ismailsa/DATASET/newBikingSmoke/bikingSmoke.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Biking and Smoke ML',
                          
                          ['Biking and Smoke ML',
                           'Menu 2',
                           'Menu 3'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Biking and Smoke ML'):
    
    # page title
    st.title('How To Estimate Heart Disease Based on 2 Factors')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        biking = st.slider('Percentage of Biking')
        
    with col2:
        smoking = st.slider('Percentage of Smoking')
    
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_diagnosis = model.predict([[biking, smoking]])
        
    st.success(heart_diagnosis)
















