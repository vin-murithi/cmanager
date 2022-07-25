session_values = [
    'county',
    'target_office',
    'registration_centers',
    'constituency',
    'ward',
    'name',
    'total_voters',
    'total_constituencies',
    'total_wards',
    'total_polling_stations',
    'optimistic_projection',
    'pessimistic_projection',
    'optimistic_turnout',
    'pessimistic_turnout',
    'recruited_voters',
]

def init_session_state_values(ss):
    for value in session_values:
        if value not in ss:
            if value is 'optimistic_projection':
                ss[value] = 80
            elif value is 'pessimistic_projection':
                ss[value] = 50
            elif value is 'county':
                ss[value] = 'MERU'
            elif value is 'target_office':
                ss[value] = 'GOVERNOR'
            else:
                ss[value] = ''


# #A function to initialize all session state values at once.
# def init_session_state_values(ss):
#     #Initialize state values
#     if 'county' and 'target_office' and 'registration_centers' and 'optimistic_projection' not in ss:
#         #profile values
#         ss.county = ''
#         ss.target_office = ''
#         ss.registration_centers = ''
#         ss.constituency = ''
#         ss.ward = ''
#         ss.name = ''
#         #regional statistics
#         ss.total_voters = 1000
#         ss.total_constituencies = ''
#         ss.total_wards = ''
#         ss.total_polling_stations = ''
#         #projection values
#         ss.optimistic_projection = '80'
#         ss.pessimistic_projection = '50'
#         ss.optimistic_turnout = 2
#         ss.pessimistic_turnout = 4
#         #Recruitement values
#         ss.recruited_voters = 2
