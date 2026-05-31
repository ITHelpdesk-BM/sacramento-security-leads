import streamlit as st
import pandas as pd

st.title("Sacramento Leads")

# Display the data saved by the scraper
try:
    df = pd.read_csv("results.csv")
    st.dataframe(df)
    
    # Download Button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download as CSV", csv, "leads.csv", "text/csv")
except:
    st.write("No leads found yet. Trigger the scraper!")
