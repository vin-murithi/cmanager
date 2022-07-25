import streamlit as st
import plotly.graph_objects as go
from datetime import date
from dateutil.relativedelta import relativedelta
from utilities.init_state_session import init_session_state_values


#Initialize state values using custom imported function 
ss = st.session_state


#get days to elections
def days_to_elections():
    election_date = date(2022,8,9)
    today = date.today()
    days_to_elections = election_date - today
    return days_to_elections.days



#Create Angular gauge indicator for optimistic progress
optimistic_progress = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = ss.recruited_voters_count,
    delta = {'reference': int(ss.optimistic_turnout)},
    title = {'text': "Optimistic Progress"},
    domain = {'x': [0, 0.5], 'y': [0, 0.5]}
))
#Create Angular gauge indicator for pessimistic progress
pessimistic_progress = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = ss.recruited_voters_count,
    delta = {'reference': int(ss.pessimistic_turnout)},
    title = {'text': "Pessimistic Progress"},
    domain = {'x': [0, 0.5], 'y': [0, 0.5]}
))

#Days to elections figure
days_to_elections_fig = go.Figure(go.Indicator(
            mode = "number",
            value = days_to_elections(),
            title = {'text': "Days to Elections"},
        ))


st.plotly_chart(days_to_elections_fig)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(optimistic_progress)
with col2:
    st.plotly_chart(pessimistic_progress)
