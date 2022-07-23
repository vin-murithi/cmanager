#A function to initialize all session state values at once.
def init_session_state_values(ss):
    #Initialize state values
    if 'county' and 'target_office' and 'registration_centers' and 'optimistic_projection' not in ss:
        #profile values
        ss.county = 'MERU'
        ss.target_office = 'GOVERNOR'
        ss.registration_centers = ''
        ss.constituency = ''
        ss.ward = ''
        ss.name = 'vin'
        #regional statistics
        ss.total_voters = 1000
        ss.total_constituencies = ''
        ss.total_wards = ''
        ss.total_polling_stations = ''
        #projection values
        ss.optimistic_projection = '80'
        ss.pessimistic_projection = '50'
        ss.optimistic_turnout = 2
        ss.pessimistic_turnout = 4
        #Recruitement values
        ss.recruited_voters = 2