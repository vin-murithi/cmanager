import streamlit as st
from data.data import county_list
from utilities.df_to_list import get_column_values



# Specify the page layout using streamlit
st.set_page_config(
    page_title='Your Profile',
    page_icon=':bar_chart',
)

st.title('Add your profile')
#session state variables
ss = st.session_state

#global variables for this file
file = 'registered_voters.xlsx'

#Get regions according to county and office
def get_admin_regions(admin_region):
    print(ss.county)
    regions = get_column_values(file,ss.county,admin_region)
    return regions
def get_mca_admin_regions(admin_region):
    regions = get_column_values(file,ss.county,admin_region,'CONSTITUENCY NAME',ss.constituency) 
    return regions

#Your Name
name = st.text_input('Your Name', key='name')
#Select county
county = st.selectbox("County", county_list, key='county')
#Select target office
target_offices = ['','GOVERNOR','SENATOR','MP','MCA']
target_office = st.selectbox("Target Office", target_offices, key='target_office')
#Once you select county and target office, the other options appear conditionally depending on target office
if ss.county and ss.target_office:
    if ss.target_office == 'GOVERNOR':
            st.write("Focus is on all of constituencies, wards and polling stations in " +ss.county+ " county")
    elif ss.target_office == 'SENATOR':
            st.write("Focus is on all of constituencies, wards and polling stations in " +ss.county+ " county")
    elif ss.target_office == 'MP':
        #get constituencies of chosen county
        admin_region = 'CONSTITUENCY NAME'
        constituencies = get_admin_regions(admin_region)
        constituency = st.selectbox("Select Constituency", constituencies, key='constituency')
        if ss.constituency:
            st.write("Focus is on the "+ ss.constituency + " constituency it's wards and polling stations")
    elif ss.target_office == 'MCA':
        #get constituencies of chosen county
        admin_region = 'CONSTITUENCY NAME'
        constituencies = get_admin_regions(admin_region)
        constituency = st.selectbox("Select Constituency", constituencies, key='constituency')
        #if consituency set, get wards in constituency
        if ss.constituency:
            admin_region = 'CAW_NAME'
            #return wards in the given constituency in the given county
            wards = get_mca_admin_regions(admin_region)
            constituency = st.selectbox("Select Ward", wards, key='ward')
            if ss.ward:
                st.write("Focus is on the "+ ss.ward + " ward and it's polling stations")

#Save the profile info here
save_profile = st.button('Save profile')
if save_profile:
    st.write(ss.name)
    st.write(ss.county)
    st.write(ss.target_office)
    st.write(ss.constituency)
    st.write(ss.ward)
