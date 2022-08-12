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
