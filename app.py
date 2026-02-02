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


import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Procurement & Publications Dashboard", layout="wide")

def load_etender_data():
    try:
        # Load the local CSV (skipping the title row as per previous step)
        df = pd.read_csv('Procurement plans - eTenders Portal 2.csv', skiprows=1)
        date_columns = ['Envisaged advert date', 'Envisaged closing date', 'Envisaged award date']
        for col in date_columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        return df
    except Exception as e:
        st.error(f"Error loading local eTender data: {e}")
        return pd.DataFrame()

etender_df = load_etender_data()

st.header("Publications")

if uploaded_file is not None:
    # Try multiple encodings for the uploaded file
    publications = None
    for enc in ['utf-8', 'latin1', 'cp1252', 'utf-16']:
        try:
            uploaded_file.seek(0)  # Reset pointer
            publications = pd.read_csv(uploaded_file, encoding=enc)
            st.success(f"Successfully loaded publications using {enc} encoding!")
            break 
        except UnicodeDecodeError:
            continue 
        except Exception as e:
            st.error(f"A different error occurred: {e}")
            break
    
    if publications is not None:
        # Keyword Filtering
        keyword = st.text_input("Filter publications by keyword", "")
        if keyword:
            # Search across all columns
            filtered = publications[publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered, use_container_width=True)
        else:
            st.write("Showing all publications")
            st.dataframe(publications, use_container_width=True)


        st.header("Publication Trends")
        if "Year" in publications.columns:
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.info("The uploaded CSV does not have a 'Year' column to visualize trends.")
else:
    st.info("Please upload a CSV file in the sidebar to see the Publications section.")

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

    # Table
    st.subheader("Procurement Plan Detail View")
    st.dataframe(df_filtered, use_container_width=True)
else:
    st.warning("Local eTender data could not be loaded.")
# Add a contact section
st.header("Contact Information")
email = "rebecca.setino@gmail.com"
st.write(f"You can reach {name} at {email}.")






