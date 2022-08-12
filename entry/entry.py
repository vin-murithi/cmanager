import streamlit as st
import pandas as pd
from tomlkit import key
from data.data import county_list
from datetime import date
from utilities.df_to_list import get_column_values
from utilities.locate_row import get_row
from dateutil.relativedelta import *

# Page configuration
st.set_page_config(
    page_title='Add a voter',
    page_icon=':bar_chart',
)
st.title('Add new recruited voter')

#Initialize state values
if 'registration_centers' and 'county' not in st.session_state:
    st.session_state.registration_centers = ['Please fill in county to get Polling Stations']
    st.session_state.county = ''

# Function for appending to worksheet
def append_df_to_excel(df, excel_path):
    df_excel = pd.read_excel(excel_path)
    result = pd.concat([df_excel, df], ignore_index=True)
    result.to_excel(excel_path, index=False)

# Values for autofill ward and constituency.
file = 'registered_voters.xlsx'
column = 'REGISTRATION CENTRE NAME'

#Get polling centers within a county given the county [save them in a state variable]
def get_centers():
    given_county = st.session_state.county
    given_county = str(given_county).upper()
    if given_county:
        st.session_state.registration_centers = get_column_values(file,given_county,column)

#get affiliate level
def get_affiliate_level(recruitor_id):
    #split recruitor id
    recruitor_affiliate_level = recruitor_id[2]
    #take the first section of Id
    recruitor_affiliate_level = int(recruitor_affiliate_level)
    #increment id and return it
    recruitee_affiliate_level = recruitor_affiliate_level+1
    return str(recruitee_affiliate_level)

# Create the form 
county = st.selectbox("County", county_list, on_change=get_centers(), key='county')
with st.form('add_recruited_voter'):
    polling_station = st.selectbox("Voter's Polling Station", st.session_state.registration_centers)
    national_id = st.text_input('National ID number')
    full_name = st.text_input('Full Name')  
    sex = st.selectbox("Sex", ['male', 'female'])
    dob = st.date_input('Date of birth', min_value=date(
        1900, 1, 1), max_value=date.today())
    phone_number = st.text_input('Phone number')
    email = st.text_input('Email')
    recruitor_id = st.text_input('Recruitor ID')
    # submit button
    submit_button = st.form_submit_button('Add Voter')
    # On submit: calculate age, autofill fields, ,create id, create dictionary, add to excel file
    if submit_button:
        # Calculate age
        today = date.today()
        age = relativedelta(today, dob).years
        # Autofill ward and constituency [make county uppercase when calling function]
        row = get_row(file,county.upper(),column,polling_station)
        print(row)
        constituency_name = row['CONSTITUENCY NAME'].iloc[0]
        ward_name = row['CAW_NAME'].iloc[0]

        # create id: affiliate_level-recruitor_id-identifier [A-A1-2]
        affiliate_level = get_affiliate_level(str(recruitor_id))

        # New recruitee info
        new_recruitee = {
            'affiliate_level': affiliate_level.zfill(3),
            'recruitor_id': recruitor_id,
            'recruitment_date': today,
            'nationalID': national_id,
            'name': full_name,
            'sex': sex,
            'DOB': dob,
            'age': age,
            'phoneNumber': phone_number,
            'email': email,
            'county': county.upper(),
            'constituencey_autofill': constituency_name,
            'ward_autofill': ward_name,
            'pollingStation': polling_station,
        }
        print(new_recruitee)
        # For some reason, I have to wrap dictionary in list due to scalar values or sth.
        df_new_voter = pd.DataFrame([new_recruitee])
        # Append new recruitee to recruited voter file
        print(df_new_voter)
        if age < 18:
            st.warning('Age not of an eligible voter')
        else:
            append_df_to_excel(df_new_voter, 'recruited_voters.xlsx')
