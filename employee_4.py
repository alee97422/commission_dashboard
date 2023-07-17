import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sqlite3

def compute_and_visualize4():
    # Connect to the SQLite database
    database = sqlite3.connect("comish2.db")
    cursor = database.cursor()

    # Fetch the required columns from the database
    query = "SELECT employee, total_net, date FROM employee 4;"  # SQL query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Create a DataFrame from the fetched rows
    df = pd.DataFrame(rows, columns=['Employee', 'Total Net', 'Date'])

    # Display the DataFrame
    st.write(df)

    # Get the number of repairs
    num_repairs = len(df)

    # Display the number of repairs
    st.write("Number of Repairs:", num_repairs)

    # Get the sum of the 'Total Net' column
    total_net_sum = df['Total Net'].sum()

    # Store the result as a variable
    st.write("Total Net Profit of Repairs:", total_net_sum)
    # Store the result as a variable
    st.write("Commision Percentage: 4%")
    st.write("Total Commission: $", total_net_sum * 0.04)

    # Create a separate DataFrame for the specific employee 
    employee_name = 'Employee 4'
    employee_df = df[df['Employee'] == employee_name]

    # Group the data by date and calculate the sum of the 'Total Net' column per day
    grouped_df = df.groupby('Date')['Total Net'].sum().reset_index()

    # Create the Plotly chart
    fig = go.Figure()

    # Add a scatter trace for the sum of 'Total Net' per day
    fig.add_trace(
        go.Scatter(x=grouped_df['Date'], y=grouped_df['Total Net'], mode='markers+lines', name='Sum per Day')
    )

    # Customize the chart layout
    fig.update_layout(
        title="Sum of Total Net per Day",
        xaxis_title="Date",
        yaxis_title="Sum of Total Net ($)",
        autosize=True,  # Enable autosizing to make the chart responsive
        margin=dict(l=40, r=40, t=60, b=40),  # Adjust the margins for better spacing
        height=400  # Set the initial height of the chart
    )

    # Enable hover text with the sum value
    fig.update_traces(hovertemplate='Date: %{x}<br>Sum: $%{y}')

    # Display the chart
    st.plotly_chart(fig)

# Call the compute_and_visualize function
compute_and_visualize4()
