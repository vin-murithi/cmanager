import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utilities.locate_row import get_row
from utilities.get_sheet import get_sheet_df
from utilities.init_state_session import init_session_state_values

# Specify the page layout using streamlit
st.set_page_config(
    page_title='IEBC Data',
    page_icon=':bar_chart',
)


#session state variables
ss = st.session_state
#Initialize state values using custom imported function 
init_session_state_values(ss)
ss

#variables local to this file
file = 'registered_voters.xlsx'
sheet_name = ss.county
column = 'CONSTITUENCY NAME'
column_value = ss.constituency
column2 = 'CAW_NAME'
column2_value = ss.ward



df_registered_voters = pd.read_excel(
    io='mauaVoters.xlsx',
    engine='openpyxl',
    sheet_name='maua',
    skiprows=0,
    usecols='A:K',
    # nrows=18,
)

#get registered voters according to the user profile: call get_row() from utilities.locate_row
if ss.county and ss.target_office:
    if not ss.constituency and not ss.ward:
        iebc_data = get_sheet_df(file,sheet_name)
#get sum of voters, constituencies, polling centers and wards
        total_voters = iebc_data['VOTERS PER REGISTRATION CENTRE'].sum()
        total_constituencies = iebc_data['CONSTITUENCY NAME'].drop_duplicates().count()
        total_wards = iebc_data['CAW_NAME'].drop_duplicates().count()
        total_polling_stations = iebc_data['REGISTRATION CENTRE NAME'].count()
        #Save values to state
        ss.total_constituencies = total_constituencies
        ss.total_wards = total_wards
        ss.total_polling_stations = total_polling_stations
        ss.total_voters = total_voters
        #total voters in county figure
        total_voters_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_voters,
            title = {'text': "Total voters in " + ss.county +" county"},
        ))
        #total polling stations in county figure
        total_constituencies_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_constituencies,
            title = {'text': "Total constituencies in " + ss.county +" county"},
        ))
        #total polling stations in county figure
        total_wards_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_wards,
            title = {'text': "Total wards in " + ss.county +" county"},
        ))
        #total wards in county figure
        total_polling_stations_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_polling_stations,
            title = {'text': "Total polling stations in " + ss.county +" county"},
        ))
        st.plotly_chart(total_voters_fig)
        st.plotly_chart(total_constituencies_fig)
        st.plotly_chart(total_wards_fig)
        st.plotly_chart(total_polling_stations_fig)
        st.table(iebc_data)
    elif not ss.ward:
        iebc_data = get_row(file, sheet_name, column, column_value)
        #get sum of voters, polling centers and wards
        total_voters = iebc_data['VOTERS PER REGISTRATION CENTRE'].sum()
        total_wards = iebc_data['CAW_NAME'].drop_duplicates().count()
        total_polling_stations = iebc_data['REGISTRATION CENTRE NAME'].count()
        #Save values to session state
        ss.total_wards = total_wards
        ss.total_polling_stations = total_polling_stations
        ss.total_voters = total_voters
        #total voters in constituency
        total_voters_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_voters,
            title = {'text': "Total voters in " + ss.constituency +" constituency"},
        ))
        #total polling stations in constituency
        total_wards_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_wards,
            title = {'text': "Total wards in " + ss.constituency +" constituency"},
        ))
        #total wards in constituency
        total_polling_stations_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_polling_stations,
            title = {'text': "Total polling stations in " + ss.constituency +" constituency"},
        ))
        st.plotly_chart(total_voters_fig)
        st.plotly_chart(total_wards_fig)
        st.plotly_chart(total_polling_stations_fig)
        st.table(iebc_data)
    elif ss.constituency and ss.ward:
        iebc_data = get_row(file, sheet_name, column, column_value, column2, column2_value)
        #get sum of voters and polling centers
        total_voters = iebc_data['VOTERS PER REGISTRATION CENTRE'].sum()
        total_polling_stations = iebc_data['REGISTRATION CENTRE NAME'].count()
        #save values into state
        ss.total_polling_stations = total_polling_stations
        ss.total_voters = total_voters
        #total voters in ward
        total_voters_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_voters,
            title = {'text': "Total voters in " + ss.ward +" ward"},
        ))
        #total polling centers in ward
        total_polling_stations_fig = go.Figure(go.Indicator(
            mode = "number",
            value = total_polling_stations,
            title = {'text': "Total polling stations in " + ss.ward +" ward"},
        ))
        st.plotly_chart(total_voters_fig)
        st.plotly_chart(total_polling_stations_fig)
        st.table(iebc_data)
else:
    st.title('Please create a profile to get pertinent data')
