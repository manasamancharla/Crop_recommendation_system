#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:27:45 2022

@author: mac
"""

import numpy as np
import pickle
import streamlit as st
from PIL import Image


#loading the saved model
loaded_model = pickle.load(open('/Users/mac/Desktop/CRS/SavedModels/RandomForest.pkl','rb'))

st.set_page_config(
    page_title="CROP RECOMENDATION ",
    page_icon=":ear_of_rice:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        #'Get Help': 'https://www.extremelycoolapp.com/help',
        #'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

#prediction function

def cr_prediction(input_data):
    #data = np.array([[104,18, 30, 23.603016, 60.3, 6.7, 140.91]])
    #prediction = loaded_model.predict(input_data)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction
    

 
def jls_extract_def():
    
    return 


def main():
    
    #Title
    
    #demo
    
    #Getting the input data from the user
    #N	P	K	temperature	humidity	ph	rainfall	label
    
    #st.caption('This is a string that explains something above.')
    #st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

    with st.sidebar:
        st.write("LOGIN")
        a = st.text_input('UserName')
        st.write(a)
        c = st.text_input('password')
        #(passward, type="password")
        st.write(c)

    rad = st.sidebar.radio("MENU",["Introduction","Predictor",])

    if rad=="Introduction":
        image = Image.open('/Users/mac/Desktop/CRS/download.jpg')
        st.image(image,width = 800 ,use_column_width=False) 
        st.text("\n")
        st.title( ":ear_of_rice: Introduction to the project")
        st.write("India is ranked 2nd worldwide in farm output. Agriculture and allied sectors like forestry and fisheries accounted for 16.6 percent of the GDP 2009, about 50 percent of the overall workforce. The monetary contribution of agriculture to India‘s GDP is regularly declining. The crop yield of plants relies on different factors like on climatic, geographical, organic, political and financial elements. For farmers, it is difficult when there is more than one crop to grow especially when the market prices are unknown to them. Citing the Wikipedia statistics, the farmer suicide rate in India has ranged between 1.4 and 1.8 per 100000 total population, over a 10-year period through 2005. While 2014 saw 5650 farmer suicides, the figure crossed 8000 in 2015. ")
        st.text("\n")
        st.write("Agriculture and its allied sectors are undoubtedly the largest providers of livelihoods in rural India.The  agriculture sector contributors 18% to the country’s Gross Domestic Product (GDP).However, regrettable is the yield per hectare of crops in comparison to international standards.This is one of the possible causes for a higher suicide rate among marginal farmers in India. The user provides the climatic and soil conditions as input  Machine learning algorithms allow choosing the most profitable crop list or predicting the crop yield for a user-selected crop as output.To predict the crop yield, selected Machine Learning algorithms such as Support Vector Machine (SVM), Random Forest (RF), Navie-bayes Classification, XG Boost, Linear Regression (LR), and Decision Trees are used.Among them, the Random Forest showed the best results with 95% accuracy. ")
        
        image = Image.open('/Users/mac/Desktop/CRS/download-1.jpg')
        st.image(image, caption='crops',width =700)
        st.text("\n")
        st.subheader("2. Objectives")
        st.write("Integrating farming and machine learning, we can lead to further advancements in agriculture by maximizing yield and optimizing the use of resources involved. Previous year‘s production data is an essential element for predicting the current yield.The goal of this project is to help the farmers by combining agriculture and technology. The end result is an application that is available on the web as well as mobile.The system uses machine learning to make predictions of the crop and Python as the programming language. Machine learning uses historical data and information to gain experiences and generate a trained model by training it with the dataMachine learning is a tool for turning information into knowledge. ")
        st.text("\n\n")
        st.subheader("3. WORKING OF PROJECT")
        st.text("\n")
        st.write("The goal of this project is to help the farmers by combining agriculture and technology. The end result is an application that is available on the web \n The application has the following features: \n i.	Login/Register: The user can register themselves by providing a username of their choice and a password. After the registration, they can login to use the application further and view all the options that are provided to them. \n ii.	Yield Prediction: This is one of the modules available in the application that enables the user to view the yield predictions of crops. The user is given two choices here: \n •	‗I know what to plant‘: This option is for those users who already have a crop in their mind that they want to grow. When chosen, the user will be given choices of crops that they must select along with other inputs .i.e., Area and the soil type. After processing the inputs, the application will return the predicted yield on the user‘s screen. \n •	‗Yet to decide the crop‘: This option is when the user is not sure between some crops or has no crop in mind. The user has to input the soil type and the area. The input is again processed at the back end by the modelled algorithm and the predicted yield is returned to the user. ")
        
        

    if rad=="Predictor":
        st.title(':seedling: Crop Recommendation System')
        with st.container():
            st.write("Enter the following values")
            N = st.text_input('Nitrogen :')
            P = st.text_input('Phosphorus :')
            K = st.text_input('Potassium :')
            temperature = st.text_input('Temperature :')
            humidity = st.text_input('Humidity :')
            ph = st.text_input('ph :')
            rainfall = st.text_input('Rainfall :')
    
    # code for prediction
        label = ''
    
    # Creating a button 
    
        if st.button('Prediction'):
            st.write("The predicted value is:")
            label = cr_prediction([N,P,K,temperature,humidity,ph,rainfall])
        
        st.success(label)
    
   
if __name__=='__main__':
    main()    