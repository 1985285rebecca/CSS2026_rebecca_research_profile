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
    # We try multiple encodings because "UnicodeDecodeError" is picky
    for enc in ['utf-8', 'latin1', 'cp1252', 'utf-16']:
        try:
            uploaded_file.seek(0)  # Reset the file pointer to the start
            publications = pd.read_csv(uploaded_file, encoding=enc)
            st.success(f"Successfully loaded using {enc} encoding!")
            break # It worked! Stop the loop.
        except UnicodeDecodeError:
            continue # Try the next encoding in the list
        except Exception as e:
            st.error(f"A different error occurred: {e}")
            break
    else:
        st.error("Could not decode the file. Please try saving your CSV as 'UTF-8' in Excel.")

    # Only show the table if 'publications' was successfully created
    if 'publications' in locals():
        st.write(publications)

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

# Add eTender PortalData Section
st.header("Explore eTender Portal Data")

# Add a contact section
st.header("Contact Information")
email = "rebecca.setino@gmail.com"
st.write(f"You can reach {name} at {email}.")





