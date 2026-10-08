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

st.set_page_config(page_title="Insights", page_icon=":material/insights:", layout="wide")
st.title(" :material/insights: Page 5: Key Insights")

df_country = pd.read_csv('data/processed/country_loss.csv')
df_state = pd.read_csv('data/processed/state_loss.csv')

# 1. Top 10 States with Highest Forest Loss
st.subheader("1. Top 10 States with Highest Forest Loss :material/bar_chart:")
top10_states = (
    df_state.groupby('subnational1')['Tree_Cover_Loss_ha']
    .sum()
    .reset_index()
    .sort_values(by='Tree_Cover_Loss_ha', ascending=False)
    .head(10)
)

fig1 = px.bar(
    top10_states, x='subnational1', y='Tree_Cover_Loss_ha', text_auto='.2s',
    color_discrete_sequence=[COLOR_GREEN],
    labels={'subnational1': 'State', 'Tree_Cover_Loss_ha': 'Total Loss (ha)'},
    title="Top 10 States Ranked by Forest Loss (2001–2020)"
)
fig1 = apply_chart_theme(fig1)
st.plotly_chart(fig1, use_container_width=True)

# 2. Highest Forest-Loss Years
st.subheader("2. Highest Forest-Loss Years :material/bar_chart:")
ranked_years = df_country.sort_values(by='Tree_Cover_Loss_ha', ascending=False)

fig2 = px.bar(
    ranked_years, x='Year', y='Tree_Cover_Loss_ha', text_auto='.2s',
    color_discrete_sequence=[COLOR_LIME],
    labels={'Year': 'Year', 'Tree_Cover_Loss_ha': 'Loss (ha)'},
    title="Years Ranked by Total National Forest Loss"
)
fig2.update_xaxes(type='category')
fig2 = apply_chart_theme(fig2)
st.plotly_chart(fig2, use_container_width=True)