from datetime import date
from dateutil.relativedelta import relativedelta

#get days to elections
def days_to_elections():
    election_date = date(2022,8,9)
    today = date.today()
    days_to_elections = election_date - today
    return days_to_elections.days
