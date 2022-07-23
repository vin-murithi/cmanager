import plotly_express as px

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