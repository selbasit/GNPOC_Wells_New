import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('GNPOC_Wells.csv')

# Data cleaning (add your cleaning steps here if needed)
# For example:
# df = df.dropna(subset=['LATITUDE', 'LONGITUDE'])

# Streamlit app
st.title("GNPOC Wells Dashboard")

# Dropdown for block selection
selected_block = st.selectbox(
    "Select Block:",
    sorted(df['BLOCK #'].dropna().unique())
    
# Filter data based on selection
block_df = df[df['BLOCK #'] == selected_block]

# Create two columns for the charts
col1, col2 = st.columns(2)

with col1:
    # Well Type Distribution
    st.subheader(f"Well Types in {selected_block}")
    fig1 = px.histogram(block_df, x="WELL TYPE", color="WELL TYPE")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    # Map Visualization
    st.subheader("Well Locations")
    fig2 = px.scatter_mapbox(block_df,
                           lat='LATITUDE', lon='LONGITUDE',
                           color='WELL TYPE',
                           hover_name='WELL NAME',
                           mapbox_style='carto-positron',
                           zoom=10)
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig2, use_container_width=True)