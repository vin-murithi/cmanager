import streamlit as st
import pandas as pd
from datetime import date, datetime

#Page configuration
st.set_page_config(
    page_title='Add a voter',
    page_icon=':bar_chart',
)
st.title('Add new recruited voter')

#Create the form
with st.form('add_recruited_voter'):
    polling_station = st.text_input("Voter's Polling Station")
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
        new_voter = {
            'level':4,
            'recruitor_id':5,
            'ID':10,
            'recruitment_date': date.today(),
            'nationalID':national_id,
            'name':full_name,
            'sex':sex,	
            'DOB':dob,	
            'phoneNumber':phone_number,
            'email':email,
            'pollingStation':polling_station,
            'ward_autofill':'',
            'constituenceyAutofill':'',
            'county_autofill':'',
        }
        #For some reason, I have to wrap dictionary in list due to scalar values or sth.
        df_new_voter = pd.DataFrame([new_voter])
        #Add an Excel writer to enable appending to excel files.
        with pd.ExcelWriter(
            'recruited_voters.xlsx',
            mode='a',
            engine='openpyxl',
            if_sheet_exists='overlay',
        ) as writer:
            sheet_title = str(datetime.today().timestamp())
            df_new_voter.to_excel(writer, sheet_title, index = False)
            print(df_new_voter)
    

