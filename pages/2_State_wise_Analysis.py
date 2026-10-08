import streamlit as st
import pandas as pd
import plotly.express as px
from theme import apply_chart_theme, COLOR_GREEN, COLOR_LIME, COLOR_SEQUENCE

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

st.set_page_config(page_title="State-wise Analysis", page_icon=":material/map:", layout="wide")
st.title(" :material/map: Page 2: State-wise Analysis")

df_state = pd.read_csv('data/processed/state_loss.csv')

# 1. Top States by Forest Loss
st.subheader("1. Top States by Forest Loss :material/bar_chart:")
top_n = st.slider("Select number of top states to display:", 5, 25, 10)
state_totals = df_state.groupby('subnational1')['Tree_Cover_Loss_ha'].sum().reset_index()
state_totals = state_totals.sort_values(by='Tree_Cover_Loss_ha', ascending=False).head(top_n)

fig1 = px.bar(state_totals, x='Tree_Cover_Loss_ha', y='subnational1', orientation='h',
              color_discrete_sequence=[COLOR_GREEN],
              labels={'Tree_Cover_Loss_ha': 'Total Loss (ha)', 'subnational1': 'State'},
              title=f"Top {top_n} States by Cumulative Forest Loss")
fig1.update_layout(yaxis={'categoryorder': 'total ascending'})
fig1 = apply_chart_theme(fig1)
st.plotly_chart(fig1, use_container_width=True)

# 2. State-wise Forest Loss Trend
st.subheader("2. State-wise Forest Loss Trend :material/show_chart:")
all_states = sorted(df_state['subnational1'].unique())
selected_states = st.multiselect("Select states to compare trends:", all_states, default=all_states[:3])

if selected_states:
    filtered_df = df_state[df_state['subnational1'].isin(selected_states)]
    fig2 = px.line(filtered_df, x='Year', y='Tree_Cover_Loss_ha', color='subnational1', markers=True,
                   color_discrete_sequence=COLOR_SEQUENCE,
                   labels={'Tree_Cover_Loss_ha': 'Loss (ha)', 'subnational1': 'State'},
                   title="Annual Forest Loss Trend Comparison")
    fig2 = apply_chart_theme(fig2)
    st.plotly_chart(fig2, use_container_width=True)

# 3. State-wise Forest Cover
st.subheader("3. Baseline Forest Cover by State :material/bar_chart:")
state_cover = df_state.groupby('subnational1')['extent_2000_ha'].first().reset_index()
fig3 = px.bar(state_cover.sort_values(by='extent_2000_ha', ascending=False),
              x='subnational1', y='extent_2000_ha',
              color_discrete_sequence=[COLOR_LIME],
              labels={'extent_2000_ha': '2000 Forest Extent (ha)', 'subnational1': 'State'},
              title="Baseline Forest Cover (Year 2000) by State")
fig3 = apply_chart_theme(fig3)
st.plotly_chart(fig3, use_container_width=True)