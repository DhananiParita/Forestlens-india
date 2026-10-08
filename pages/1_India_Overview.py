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

st.set_page_config(page_title="India Overview", page_icon=":material/dashboard:", layout="wide")
st.title(" :material/dashboard: Page 1: India Overview")

df_country = pd.read_csv('data/processed/country_loss.csv').sort_values('Year')
df_state = pd.read_csv('data/processed/state_loss.csv')

baseline = df_country['extent_2000_ha'].iloc[0]
df_country['Cumulative_Loss'] = df_country['Tree_Cover_Loss_ha'].cumsum()
df_country['Forest_Cover_ha'] = baseline - df_country['Cumulative_Loss']

# 1. Forest Loss by Year
st.subheader("1. Forest Loss by Year :material/show_chart:")
fig1 = px.line(df_country, x='Year', y='Tree_Cover_Loss_ha', markers=True,
               color_discrete_sequence=[COLOR_GREEN],
               labels={'Tree_Cover_Loss_ha': 'Tree Cover Loss (ha)'},
               title="Annual Forest Loss in India (2001–2020)")
fig1 = apply_chart_theme(fig1)
st.plotly_chart(fig1, use_container_width=True)

# 2. Forest Cover by Year
st.subheader("2. Forest Cover by Year :material/area_chart:")
fig2 = px.area(df_country, x='Year', y='Forest_Cover_ha',
               color_discrete_sequence=[COLOR_LIME],
               labels={'Forest_Cover_ha': 'Remaining Cover (ha)'},
               title="Estimated Remaining Forest Cover Trajectory")
fig2 = apply_chart_theme(fig2)
st.plotly_chart(fig2, use_container_width=True)

# 3. Forest Loss by State
st.subheader("3. Forest Loss by State :material/bar_chart:")
state_totals = df_state.groupby('subnational1')['Tree_Cover_Loss_ha'].sum().reset_index()
fig3 = px.bar(state_totals.sort_values(by='Tree_Cover_Loss_ha', ascending=False),
              x='subnational1', y='Tree_Cover_Loss_ha',
              color_discrete_sequence=[COLOR_GREEN],
              labels={'subnational1': 'State / UT', 'Tree_Cover_Loss_ha': 'Total Loss (ha)'},
              title="Total Cumulative Forest Loss by State")
fig3 = apply_chart_theme(fig3)
st.plotly_chart(fig3, use_container_width=True)