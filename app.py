#This is a commission dashboard using streamlit
# This is for my work at phone doctors i will be coming up with some fake numbers to put up on git hub
#however the version i share with my co workers will be private commission data
#

#intially gonna be using streamlit to make this dashboard 
#will likely have to rely on numpy and pandas by the end of this project tho 

#
#this is the first version of the dashboard
import streamlit as st
import pandas as pd
import sqlite3
from employee_1 import compute_and_visualize
from employee_2 import compute_and_visualize2
from employee_3 import compute_and_visualize3
from employee_4 import compute_and_visualize4
from emplopyee_5 import compute_and_visualize5

# Connect to the SQLite database
database = sqlite3.connect("comish2.db")
cursor = database.cursor()

# Fetch the required columns from the database
query = "SELECT employee, date, ticket, invoice, product, unit_price , total_cost, total_price, total_net FROM employees;"  # SQL query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Create a DataFrame from the fetched rows
df = pd.DataFrame(rows, columns=["employee", "date", "ticket", "invoice", "product", "unit_price", "total_cost", "total_price", "total_net"])

# Sidebar buttons
st.sidebar.title("Technician")
sidebar_button = st.sidebar.button("Home")
sidebar_button1 = st.sidebar.button("employee 1")
sidebar_button2 = st.sidebar.button("employee 2")
sidebar_button3 = st.sidebar.button("employee 3")
sidebar_button4 = st.sidebar.button("employee 4")
sidebar_button5 = st.sidebar.button("employee 5")

# Perform computation and visualization specific to the current technician (Anthony Lee, Caleb Geelen, etc.)
if sidebar_button:
    st.title("Commission Dashboard!")
    # discribe the data frame
    st.write("This is a first draft of the commision dashaboard To get started please click your name on the side bar buttons Below you will find some initial data about overall in this store how the month is going as far as commission stats go ")
    # Display the full dataframe
    st.write(df)

if sidebar_button1:
    st.title("Empoyee1")
    compute_and_visualize()

elif sidebar_button2:
    st.title("Employee 2")
    compute_and_visualize2()

elif sidebar_button3:
    st.title("Employee 3")
    compute_and_visualize3()

elif sidebar_button4:
    st.title("Employee 4")
    compute_and_visualize4()

elif sidebar_button5:
    st.title("Employee 5")
    compute_and_visualize5()

# Close the database connection
cursor.close()
database.close()










st.write("This is a starting draft for this application any feedback is welcome. Any suggesstions for furtheriing development or adding any features please feel welcome to let me know!")