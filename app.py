#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:46:13 2026

@author: rebeccaseteno
"""

import streamlit as st
import pandas as pd

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
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)
# Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

st.header("Publication Trends")

if uploaded_file:
# Changed to check for 'Year' since the header is 'Trends'
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "rebecca.setino@gmail.com"
st.write(f"You can reach {name} at {email}.")






















