import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
import plotly.io as pio
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from Home import df_recruited_voters
from utilities.init_state_session import init_session_state_values

#session state variables
ss = st.session_state

#Function to filter recruited voters by time recruited
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
    recruited_voters['recruitment_date'] = pd.to_datetime(recruited_voters['recruitment_date']).dt.date
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

#Create a pie chart for male and female recruits
recruit_gender = px.pie(
    data_frame=df_recruited_voters,
    names='sex',
    color='sex',
    color_discrete_sequence=['red','blue'],
    title='Gender ratio',
    template='presentation',
    # width=600,
    # height=250,
    # hole=0.5,
)
recruit_gender.update_traces(text = df_recruited_voters['sex'].value_counts(), textinfo = 'percent')


#Get the age distribution of recruited voters
a18_24 = df_recruited_voters[(df_recruited_voters['age']>17) & (df_recruited_voters['age']<25)]
a25_34 = df_recruited_voters[(df_recruited_voters['age']>24) & (df_recruited_voters['age']<35)]
a35_44 = df_recruited_voters[(df_recruited_voters['age']>34) & (df_recruited_voters['age']<45)]
a45_64 = df_recruited_voters[(df_recruited_voters['age']>44) & (df_recruited_voters['age']<65)]
a65plus = df_recruited_voters[df_recruited_voters['age']>64]
#create a dictionary for the age distributions
age_dist_data={
    'age':['18 to 24',' 25 to 34','35 to 44','45 to 64','above 65'],
    'distribution':[len(a18_24),len(a25_34),len(a35_44),len(a45_64),len(a65plus)]}
#Create a dataframe out of the dictionary
df_age_dist = pd.DataFrame(age_dist_data)
#plot the dataframe into a pie chart
age_dist_pie = px.pie(
    data_frame=df_age_dist,
    values='distribution',
    names='age',
    color='age',
    title='Age distribution',
    template='presentation',
    # width=600,
    # height=250,
    # hole=0.5,
)
age_dist_pie.update_traces(text = df_age_dist['age'], textinfo = 'percent')
#Create a voter count figure
recruited_voters_count = df_recruited_voters['name'].count()
#Add to session state values
ss.recruited_voters_count = recruited_voters_count
#recruited voters figure
recruited_voters_count_fig = go.Figure(go.Indicator(
            mode = "number",
            value = recruited_voters_count,
            title = {'text': "Current recruited voters"},
        ))

st.plotly_chart(recruited_voters_count_fig)
#Gender ratio chart
st.plotly_chart(recruit_gender)
#Age dist chart
st.plotly_chart(age_dist_pie)


#Create a dropdown to take input for period to display
timePeriodOptions = ["To Date", "Today", "Yesterday","This Week", "Last Week", "This Month", "Last Month"]
recruitments_in_period = st.selectbox(
    "View Recruited voters for: ", timePeriodOptions)
#Pass input to filter function and get rows filtered by time
recruitment_in_given_period = filterByDate(recruitments_in_period)
#Recruitee table
st.table(recruitment_in_given_period)
