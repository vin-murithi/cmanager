import streamlit as st
import plotly.graph_objects as go

# Specify the page layout using streamlit
st.set_page_config(
    page_title='Progress',
    page_icon=':bar_chart',
)


#Create Angular gauge indicator for optimistic progress
optimistic_progress = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = 131,
    delta = {'reference': 335},
    title = {'text': "Optimistic Progress"},
    domain = {'x': [0, 0.5], 'y': [0, 0.5]}
))
#Create Angular gauge indicator for pessimistic progress
pessimistic_progress = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = 131,
    delta = {'reference': 250},
    title = {'text': "Pessimistic Progress"},
    domain = {'x': [0, 0.5], 'y': [0, 0.5]}
))




st.plotly_chart(optimistic_progress)
st.plotly_chart(pessimistic_progress)