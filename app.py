#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:46:13 2026

@author: rebeccaseteno
"""

import streamlit as st


# Title of the app
st.title("Researcher Profile Page with Supply Chain Data")

# Collect basic information
name = "Rebecca Setino"
field = "Supply Chain"
institution = "Wits University"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")


# Add a section for publications
st.header("Publications")
if uploaded_file is not None:
    # Add the encoding parameter here
    publications = pd.read_csv(uploaded_file, encoding='latin1', on_bad_lines='skip', encoding_errors='replace')

    # Add filtering for year or keyword
keyword = st.text_input("Filter by keyword", "")
if keyword:
    ArithmeticErrorfiltered = publications[publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)]
    st.write(f"Filtered Results for '{keyword}':")
    st.dataframe(filtered)
else:
    st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")"""

# Add STEM Data Section
st.header("Explore STEM Data")




# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")



