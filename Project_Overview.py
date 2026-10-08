import streamlit as st

st.set_page_config(
    page_title="ForestLens India - Project Overview",
    page_icon=":material/forest:",
    layout="wide"
)

# Custom CSS: Sidebar content ko navigation links ke upar move karne ke liye
st.markdown("""
    <style>
        div[data-testid="stSidebarContent"] {
            display: flex !important;
            flex-direction: column !important;
        }
        div[data-testid="stSidebarUserContent"] {
            order: 1 !important;
            padding-bottom: 0px !important;
        }
        div[data-testid="stSidebarNav"] {
            order: 2 !important;
            padding-top: 0px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Main Title (Ab yeh navigation links ke upar aayega)
st.sidebar.markdown("## :material/forest: **ForestLens India**")
st.sidebar.divider()

# Main Header
st.title(" :material/forest: ForestLens India")
st.subheader("India Forest Cover & Deforestation Analytics Dashboard (2001–2020)")

st.divider()

# Project Overview Section
st.header(" :material/info: Project Overview")
st.write(
    "This dashboard is designed to understand and analyze forest cover and deforestation across India. "
    "It converts the data into simple visual insights and helps identify changes over time and areas with higher forest loss."
)

st.divider()

# Dashboard Pages Section
st.header(" :material/space_dashboard: Dashboard Pages")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    * **:material/dashboard: Page 1: India Overview**  
      Provides an overall view of forest loss and forest cover across India.
    
    * **:material/map: Page 2: State-wise Analysis**  
      Compares different states and identifies states with higher forest loss.
    
    * **:material/show_chart: Page 3: Trend Analysis**  
      Shows how forest loss has changed over the years and highlights important trends.
    """)

with col2:
    st.markdown("""
    * **:material/psychology: Page 4: AI Prediction**  
      Uses a machine learning model to compare actual and predicted forest loss and estimate future trends.
    
    * **:material/insights: Page 5: Key Insights**  
      Highlights the states and years with the highest forest loss.
    
    * **:material/travel_explore: Page 6: District Explorer**  
      Provides a closer look at district-level forest loss and helps identify potential hotspots.
    """)

st.divider()

# Main Goal Section
st.header(" :material/ads_click: Main Goal")
st.write(
    "The main goal is to use data analysis, visualization, and AI to understand deforestation "
    "patterns in India and present the findings in a simple and useful way."
)

st.caption("Data Source: Global Forest Watch (GFW) / University of Maryland")