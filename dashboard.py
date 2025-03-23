import streamlit as st
import duckdb
import pandas as pd

#Function to load data from the parquet file
def load_data():
    con = duckdb.connect()
    df = con.execute("SELECT * FROM 'data/measurements_summary.parquet'").df()
    con.close()
    return df

#Principal function to create the dashboard
def main():
    st.title("Weather Station Summary")
    st.write("This Dashboard shows the summary of temperature")

    #Load the data
    data = load_data()

    #Display the data on a format table
    st.dataframe(data)

if __name__ == "__main__":
    main()
    