PROPOSED SOLUTION
Sheet 1: Spreadsheet for projection data
- No of voters
- Optimistic projection: percentage & value
- Pessimistic projection: percentage & value

Sheet 2,3,4: There needs to be a list of: 
- Counties with constituencies 
- Constituencies with their wards 
- Wards with polling stations & Registered voters in each polling station.

Sheet 5: Where will their recruits list be added in? 
- Have one voter list where their ID's identify with recruitor ID?
- Have a sheet titled recruitor with recruitee list


Autofilling info: Use If function to autofill cells (Can be done using python or Excel)
- Input Polling station name - Autofill: Ward, constituency, county as appropriate

Required voter details:
-ID
-Name
-ID
-Phone_number
-email
-polling station
-ward_autofill
-const_autofill
-county_autofill


Proposed tools: 
- Python web app using streamlit library (Visualization aka Dashboard)
- Excel(Entry and storage)

Uncertainities: How to organize and split data in Excel (Whether to split data into many sheets or workbooks)
Current suggestion: 3 workbooks with sheets
- Administrative regions workbook (sheets: list of counties, constituencies, ward, polling stations & registered voters)
- Projection data workbook (sheets: projections sheet)
- Recruitment workbook (sheets: either 1 sheet with all voters, identified with concatenated recruiter-recruitee IDs 
	or multiple sheets with recruitor as title and recruitees as rows)
	
	
This is the preliminary system analysis and design. requirements may evolve and Implementation change from new developments.

Youtube Sources:
https://youtu.be/Sb0A9i6d320
**************************************************************************************************************************************
EXCEL DOCUMENTATION
Worksheet 1: Administrative regions
-List of counties:	
-List of constituencies per county
-List of wards per constituency
-List of polling stations per ward & Number of registered voters in each ward

Worksheet 2: Recruited voters
-Recruitment level [affiliate level]
-Recruitor ID [Id of person who recruited the voter]
-ID [ID of the recruited voter]
-Recruitment Date [Date voter was recruited]
-National ID [ID number or passport]
-Name [Name in ID]
-DOB [DOB in ID]
-Phone Number 
-Email
-Polling station [Last manual entry]
-Ward [Autofill]
-Constituency [Autofill]
-County [Autofill]


**************************************************************************************************************************************
what to visualize:
-Percentage of voters recruited against both optimistic and pessimistic projections
-Recruited voters in the last week and month
-Recruited voter Ages 18-29 30-39 40-49 50-60
-Recruited voters gender Male v Female

What to process:
-Autofill ward, constituency, county
-ID with level-recruitor-id 3-4-5

creating functions or screens or pages in streamlit
processing and filtering data using pandas date, count, 

06-07-2022
2. Recruited voters gender Male v Female
3. Recruited voters against optimistic projections
4. Filter registred voter data by: County, constituency, ward, polling station

12-07-2022 - 13-07-2022
1. Recruited voters in the last month, week
2. Create a data entry interface with data validation

14-07-2022
1. Use Excel writer to append the data

18-07-2022
Visualization:
	1.Refine the UI
		Separate code for pages into functions and more documents.
		Grid UI components: make them flow and compact
	2.Tally voters per ward, make the program ward oriented
	3.Make Projections consequential
input:
	4.Make New recruitees added append to recruited_voters.xlsx **
	5.Calculate the age on entry**
	6.Create Compound ID on entry
	7.Add Autofill on entry
Administrative regions Worksheet
Meru Worksheet
	1.Constituencies
	2.Ward
	3.Polling stations  & no of registered voters

With County and polling sttion, how do I autofill constituency and ward
	-I need to check polling station against wards 
	-then wards against constituency
	for this I will need a list of constituencies and wards
	This will use string comparison
Or:
	I can get the polling station code and split the code as it is made up of a concantenation of it's Supers codes.
	-I will need a dictionary of polling stations and their codes
	-Dictionary of polling wards, constituencies, counties with their codes.
	This will use number comparison
I need to create datasets: Meru
Get rows with meru: Get constituencies, get wards in those constituencies, get polling stations in those wards.

**************************************************************************************************************************************
DOCUMENTATION
Installation
-pip install python 3.9
-pip install pandas
-pip install openpyxl
-pip install streamlit
-pip install plotly-express

File Descriptions
app.py
-Entry point point of the program
-Read the file as panda dataframe
-Create the layout of the dashboard

entry.py
-Has a form with 7 inputs and a submit button
-Form data saves in a dictionary
-Dictionary is saved in a list
-List converted to a dataframe and written to an excel file.


