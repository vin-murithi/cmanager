import pandas as pd
import plotly_express as px
import plotly.io as pio
import streamlit as st
import plotly.graph_objects as go
from tomlkit import datetime
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from zmq import REQ_CORRELATE

# Specify the page layout using streamlit
st.set_page_config(
    layout='wide',
    page_title='Campaign Dashboard',
    page_icon=':bar_chart',
)


# Reads an excel file as a panda Dataframe: 2 dimensional array with labeled rows and columns
df_registered_voters = pd.read_excel(
    io='mauaVoters.xlsx',
    engine='openpyxl',
    sheet_name='maua',
    skiprows=0,
    usecols='A:K',
    # nrows=18,
)
# Read excel list of recruited voters
df_recruited_voters = pd.read_excel(
    io='recruited_voters.xlsx',
    engine='openpyxl',  
    sheet_name='Recruited Voters',
    skiprows=0,
    usecols='A:N',
    # nrows=18,
)

#Get dataframe of voters recruited in the last week
recruitment_dates = pd.read_excel(
    io='recruited_voters.xlsx',
    engine='openpyxl',
    sheet_name='Recruited Voters',
    skiprows=0,
    usecols='D',
    # nrows=18,
)




#Create a pie chart for optimistic values
df_regvoters = df_registered_voters[df_registered_voters['voters']<548 ]
optimistic_pie = px.pie(
    data_frame=df_regvoters,
    values='voters',
    names='pollingStationName',
    color='pollingStationName',
    color_discrete_sequence=['red','green','blue'],
    hover_name='pollingStationName',
    # hover_data='voters',
    title='Polling stations with least voters',
    template='presentation',
    # width=600,
    # height=250,
    hole=0.5,
)




#Create a pie chart for male and female recruits
recruit_gender = px.pie(
    data_frame=df_recruited_voters,
    names='sex',
    color='sex',
    color_discrete_sequence=['red','blue'],
    title='Recruited voters per gender',
    template='presentation',
    # width=600,
    # height=250,
    hole=0.5,
)
recruit_gender.update_traces(text = df_recruited_voters['sex'].value_counts(), textinfo = 'percent')

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


def filterByDate(period):
    recruited_voters = df_recruited_voters
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    weekday = date.today().weekday()
    last_week = date.today() - timedelta(days=weekday)
    last_week2 = date.today() - timedelta(days=(weekday+7))
    current_month = date.today().month
    last_month = current_month-1
    month_ago = today - relativedelta(months=+1)


    #Convert the date column to date format first
    recruited_voters['recruitment_date'] = pd.to_datetime(recruited_voters['recruitment_date'],format='%d%m%Y:%H:%M:%S.%f').dt.date
    recruited_voters['Month'] = pd.DatetimeIndex(recruited_voters['recruitment_date']).month
    
    #determine time to filter to
    if period == "Today":
        recruited_voters = recruited_voters.loc[recruited_voters['recruitment_date'] == today]
    elif period == 'Yesterday':
        recruited_voters = recruited_voters.loc[(recruited_voters['recruitment_date'] == yesterday)]
    elif period == 'This Week':
        date_filter = (recruited_voters['recruitment_date'] <= today) & (recruited_voters['recruitment_date'] >= last_week)
        recruited_voters = recruited_voters.loc[date_filter]
    elif period == 'Last Week':
        date_filter = (recruited_voters['recruitment_date'] < last_week) & (recruited_voters['recruitment_date'] >= last_week2)
        recruited_voters = recruited_voters.loc[date_filter]
    elif period == 'This Month':
        date_filter = (recruited_voters['Month'] == current_month)
        recruited_voters = recruited_voters.loc[date_filter]
        print('this month is ' + str(current_month))
    elif period == 'Last Month':
        date_filter = (recruited_voters['Month'] == last_month)
        recruited_voters = recruited_voters.loc[date_filter]
        print('Last month ' + str(last_month))
    return recruited_voters

# Create a sidebar
st.sidebar.header('Select insights to preview')
sidebarOptions = ["IEBC Data","Projections", "Recruitments", "Progress"]
displayed_data = st.sidebar.selectbox(
    "What do you want to display?", sidebarOptions)



#Display according to user choice in drop down
if displayed_data == 'IEBC Data':
    st.table(df_registered_voters)
elif displayed_data == 'Projections':
    optimistic_projection = st.text_input("Optimistic Projection", 80)
    pessimistic_projection = st.text_input("Pessimistic Projection", 50)
    st.plotly_chart(optimistic_pie)
elif displayed_data == 'Recruitments':
    #Create a dropdown to take input for period to display
    timePeriodOptions = ["To Date", "Today", "Yesterday","This Week", "Last Week", "This Month", "Last Month"]
    recruitments_in_period = st.selectbox(
        "View Recruited voters for: ", timePeriodOptions)
    #Pass input to filter function and get rows filtered by time
    recruitment_in_given_period = filterByDate(recruitments_in_period)
    #Recruitee table
    st.table(recruitment_in_given_period)
    #Gender ratio chart
    st.plotly_chart(recruit_gender)

    # st.table(recruitment_dates)
elif displayed_data == 'Progress':
    st.plotly_chart(optimistic_progress)
    st.plotly_chart(pessimistic_progress)



