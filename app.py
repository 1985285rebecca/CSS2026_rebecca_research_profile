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

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Department" in publications.columns:
        departments_counts = publications["Department"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add  Procurement Data Section
st.header("Explore Procurement Data")


st.divider()
st.header("Explore eTender Portal Data")

if not etender_df.empty:
    # Sidebar Filters for eTender Data
    st.sidebar.divider()
    st.sidebar.subheader("eTender Filters")
    depts = sorted(etender_df['Department'].unique())
    selected_dept = st.sidebar.multiselect("Select Department", options=depts)
    etender_search = st.sidebar.text_input("Search Procurement Description")

    # Filter Logic
    df_filtered = etender_df.copy()
    if selected_dept:
        df_filtered = df_filtered[df_filtered['Department'].isin(selected_dept)]
    if etender_search:
        df_filtered = df_filtered[df_filtered['Description of goods, services and works'].str.contains(etender_search, case=False, na=False)]

    # Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Items", len(df_filtered))
    m2.metric("Departments", df_filtered['Department'].nunique())
    latest = df_filtered['Envisaged advert date'].max()
    m3.metric("Latest Advert", latest.strftime('%Y-%m-%d') if pd.notnull(latest) else "N/A")

    # Chart
    dept_counts = df_filtered['Department'].value_counts().reset_index()
    dept_counts.columns = ['Department', 'Count']
    fig = px.bar(dept_counts.head(15), x='Count', y='Department', orientation='h', 
                 title="Top 15 Departments by Procurement Volume",
                 color='Count', color_continuous_scale='Blues')
    st.plotly_chart(fig, use_container_width=True)

# Add a contact section
st.header("Contact Information")
email = "rebecca.setino@gmail.com"
st.write(f"You can reach {name} at {email}.")









