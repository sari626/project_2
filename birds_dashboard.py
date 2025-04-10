import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_folium import st_folium
import folium
import os

st.set_page_config(page_title="Bird Species Dashboard", layout="wide")

st.title("🕊️ Bird Species Observation Dashboard")

# Load Excel files
try:
    df_forest = pd.read_excel("Bird_Monitoring_Data_FOREST.XLSX", engine="openpyxl")
    df_grassland = pd.read_excel("Bird_Monitoring_Data_GRASSLAND.XLSX", engine="openpyxl")

    df_forest["habitat"] = "forest"
    df_grassland["habitat"] = "grassland"

    df = pd.concat([df_forest, df_grassland], ignore_index=True)
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    # Sidebar filters
    st.sidebar.header("🔎 Filter Options")
    selected_habitat = st.sidebar.selectbox("Select Habitat", df['habitat'].unique())
    df = df[df['habitat'] == selected_habitat]

    selected_year = st.sidebar.selectbox("Select Year", sorted(df['year'].dropna().unique()))
    selected_observer = st.sidebar.selectbox("Select Observer", sorted(df['observer'].dropna().unique()))

    filtered_df = df[(df['year'] == selected_year) & (df['observer'] == selected_observer)]

    # Summary stats
    st.subheader("📈 Summary Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Observations", len(filtered_df))
    col2.metric("Unique Species", filtered_df['scientific_name'].nunique())
    col3.metric("Sites Covered", filtered_df['site_name'].nunique())

    # Top species chart
    st.subheader("🔝 Top 10 Bird Species")
    top_species = filtered_df['scientific_name'].value_counts().head(10)
    st.bar_chart(top_species)

    # Observations by year
    st.subheader("📅 Observations by Year")
    obs_year = df['year'].value_counts().sort_index()
    st.line_chart(obs_year)

    # Bird map (sample only)
    st.subheader("📍 Sample Bird Sightings Map")
    sample_species = df['scientific_name'].dropna().unique()[:5]
    dummy_coords = [[22.5, 78.9], [21.0, 77.5], [23.0, 80.2], [24.2, 75.3], [25.6, 79.1]]

    m = folium.Map(location=[22.5, 78.9], zoom_start=5)
    for name, coords in zip(sample_species, dummy_coords):
        folium.Marker(location=coords, popup=name).add_to(m)

    st_folium(m, width=700, height=500)

except FileNotFoundError:
    st.error("❌ One of the bird monitoring Excel files was not found in the folder.")

except Exception as e:
    st.error(f"⚠️ Error occurred: {e}")