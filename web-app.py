import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import streamlit as st
import pickle 

st.set_page_config(
    page_title='Are You Competitive or Funny? ',
    page_icon= 'ඞ', #command control space
    initial_sidebar_state = 'expanded'
)

#will show up in all the pages because it is run before the individual pages
st.title('AmongUsCompetitive or AmongUsMemes?')


#Adding a selct box -- making individual pages 
page = st.sidebar.selectbox(
    'Select a page:',
    ('About', 'Making a Prediction')
)
#Individual pages 
if page == 'About':
    #Contents of the about page
    st.subheader('About this Project')
    st.write('This project is aimed to making a prediction based off of the two subreddits that the model was given.')

elif page == 'Making a Prediction':
    #Contents of the Make a Prediction page
    st.subheader('You Can Make a Prediction!')
    with open('modeling-code/amongus_gs.pkl', mode ='rb') as pickle_in:
        gs = pickle.load(pickle_in)

    #Get input from user 
    #Add default prediction less confusing
    user_text = st.text_input(
        'Please enter some text: ', 
        value='You are a meme',
        )

    #Make the prediction 
    prediction = gs.predict([user_text])[0]

    #use st.write to write a message out to the user 
    st.write(f"You write like {prediction}.")
