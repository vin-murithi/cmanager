import streamlit as st
import pandas as pd
from data import county_list
from datetime import date
from dateutil.relativedelta import *

#Page configuration
st.set_page_config(
    page_title='Add a voter',
    page_icon=':bar_chart',
)
st.title('Add new recruited voter')

#Function for appending to worksheet
def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)

#Function to autofill ward and constituency.

#Create the form
with st.form('add_recruited_voter'):
    polling_station = st.text_input("Voter's Polling Station")
    county = st.selectbox("County", county_list)
    national_id = st.text_input('National ID number')
    full_name = st.text_input('Full Name')
    sex = st.selectbox("Sex", ['male', 'female'])
    dob = st.date_input('Date of birth', min_value=date(1900, 1, 1), max_value=date.today())
    phone_number = st.text_input('Phone number')
    email = st.text_input('Email')
    #submit button
    submit_button = st.form_submit_button('Add Voter')
    #On submit
    if submit_button:
        #Calculate age
        today = date.today()
        age = relativedelta(today,dob).years
        #Autofill ward and constituency

        #create id

        #New recruitee info
        new_recruitee = {
            'affiliate_level':4,
            'recruitor_id':5,
            'identifier':11,
            'id':4511,
            'recruitment_date': today,
            'nationalID':national_id,
            'name':full_name,
            'sex':sex,	
            'DOB':dob,
            'age':age,
            'phoneNumber':phone_number,
            'email':email,
            'pollingStation':polling_station,
            'county':county,
            'ward_autofill':'',
            'constituenceyAutofill':'',
        }
        #For some reason, I have to wrap dictionary in list due to scalar values or sth.
        df_new_voter = pd.DataFrame([new_recruitee])
        #Append new recruitee to recruited voter file
        append_df_to_excel(df_new_voter, 'recruited_voters.xlsx')
      
    

