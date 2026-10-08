import streamlit as st
import pandas as pd
import plotly.express as px
from theme import apply_chart_theme, COLOR_GREEN, COLOR_LIME

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

st.sidebar.markdown("## :material/forest: **ForestLens India**")
st.sidebar.divider()

st.set_page_config(page_title="Trend Analysis", page_icon=":material/show_chart:", layout="wide")
st.title(" :material/show_chart: Page 3: Trend Analysis")

df_country = pd.read_csv('data/processed/country_loss.csv').sort_values('Year')

# 1. Annual Forest Loss Trend
st.subheader("1. Annual Forest Loss Trend :material/show_chart:")
df_country['3Y_Moving_Avg'] = df_country['Tree_Cover_Loss_ha'].rolling(window=3).mean()

fig1 = px.line(df_country, x='Year', y=['Tree_Cover_Loss_ha', '3Y_Moving_Avg'],
              color_discrete_sequence=[COLOR_GREEN, COLOR_LIME],
              labels={'value': 'Loss (ha)', 'variable': 'Metric'},
              title="Annual Forest Loss with 3-Year Moving Average")
fig1 = apply_chart_theme(fig1)
st.plotly_chart(fig1, use_container_width=True)

# 2. Year-over-Year Forest Loss Change
st.subheader("2. Year-over-Year Forest Loss Change :material/bar_chart:")
df_country['YoY_Change_ha'] = df_country['Tree_Cover_Loss_ha'].diff()
df_country['Change_Type'] = df_country['YoY_Change_ha'].apply(lambda x: 'Increase in Loss' if x > 0 else 'Decrease in Loss')

fig2 = px.bar(df_country.dropna(subset=['YoY_Change_ha']), x='Year', y='YoY_Change_ha', color='Change_Type',
              color_discrete_map={'Increase in Loss': COLOR_GREEN, 'Decrease in Loss': COLOR_LIME},
              labels={'YoY_Change_ha': 'YoY Change in Loss (ha)'},
              title="Year-over-Year Absolute Change in Tree Cover Loss")
fig2 = apply_chart_theme(fig2)
st.plotly_chart(fig2, use_container_width=True)