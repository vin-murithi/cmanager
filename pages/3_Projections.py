import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly_express as px
import plotly.io as pio
from Home import df_registered_voters
from utilities.init_state_session import init_session_state_values

#session state variables
ss = st.session_state


st.subheader('What is your projected voter turnout in % ?')
optimistic_projection = st.text_input("Optimistic Projection", ss.optimistic_projection, key='optimistic_projection')
pessimistic_projection = st.text_input("Pessimistic Projection", ss.pessimistic_projection, key='pessimistic_projection')

#Get voter turnout for each case
optimistic_turnout = (ss.total_voters * int(ss.optimistic_projection))/100
pessimistic_turnout = (ss.total_voters * int(ss.pessimistic_projection))/100
#Add values to session state
ss.optimistic_turnout = optimistic_turnout
ss.pessimistic_turnout = pessimistic_turnout

#Create figures for both cases
optimistic_turnout_fig = go.Figure(go.Indicator(
            mode = "number",
            value = optimistic_turnout,
            title = {'text': "Optimistic voter turnout"},
            domain = {'x': [0, 0.4], 'y': [0, 0.5]}

        ))
pessimistic_turnout_fig = go.Figure(go.Indicator(
            mode = "number",
            value = pessimistic_turnout,
            title = {'text': "Pessimistic voter turnout"},
            domain = {'x': [0, 0.4], 'y': [0, 0.5]}
        ))

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(optimistic_turnout_fig)
with col2:
    st.plotly_chart(pessimistic_turnout_fig)