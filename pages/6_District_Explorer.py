import streamlit as st
import pandas as pd
import plotly.express as px
from theme import apply_chart_theme, COLOR_GREEN

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

st.set_page_config(page_title="District Explorer", page_icon=":material/travel_explore:", layout="wide")
st.title(" :material/travel_explore: Page 6: District Hotspot Explorer")

df_district = pd.read_csv('data/processed/district_loss.csv')

# State Filter Selection
selected_state = st.selectbox("Select State to Explore Districts:", sorted(df_district['subnational1'].unique()))
df_filtered = df_district[df_district['subnational1'] == selected_state]

# 1. Total Forest Loss by District
st.subheader(f"1. Total Tree Cover Loss by District in {selected_state} :material/bar_chart:")
dist_totals = (
    df_filtered.groupby('subnational2')['Tree_Cover_Loss_ha']
    .sum()
    .reset_index()
    .sort_values(by='Tree_Cover_Loss_ha', ascending=False)
)

fig_bar = px.bar(
    dist_totals, x='subnational2', y='Tree_Cover_Loss_ha', text_auto='.2s',
    color_discrete_sequence=[COLOR_GREEN],
    labels={'subnational2': 'District', 'Tree_Cover_Loss_ha': 'Total Loss (ha)'},
    title=f"District-level Total Loss Breakdown for {selected_state}"
)
fig_bar = apply_chart_theme(fig_bar)
st.plotly_chart(fig_bar, use_container_width=True)

# 2. Raw District Data Table
st.subheader("2. Detailed District Data Table :material/table_view:")
st.dataframe(
    df_filtered[['subnational2', 'Year', 'Tree_Cover_Loss_ha', 'extent_2000_ha']]
    .rename(columns={'subnational2': 'District', 'extent_2000_ha': 'Baseline Extent 2000 (ha)'}),
    use_container_width=True
)