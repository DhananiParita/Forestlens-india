import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
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

st.set_page_config(page_title="AI Prediction", page_icon=":material/psychology:", layout="wide")
st.title(" :material/psychology: Page 4: AI Prediction")

df_country = pd.read_csv('data/processed/country_loss.csv').sort_values('Year')

# Fit Model
X = df_country[['Year']].values
y = df_country['Tree_Cover_Loss_ha'].values

model = LinearRegression()
model.fit(X, y)

df_country['Predicted_Loss'] = model.predict(X)
df_country['Residual_Error'] = df_country['Tree_Cover_Loss_ha'] - df_country['Predicted_Loss']

# Predict Future Years (2021 - 2030)
future_years = np.array(range(2021, 2031)).reshape(-1, 1)
future_preds = model.predict(future_years)
df_future = pd.DataFrame({'Year': future_years.flatten(), 'Predicted_Loss': future_preds})

# 1. Actual vs Predicted Forest Loss
st.subheader("1. Actual vs Predicted Forest Loss :material/show_chart:")

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df_country['Year'], y=df_country['Tree_Cover_Loss_ha'], mode='lines+markers', name='Actual Loss', line=dict(color=COLOR_GREEN)))
fig1.add_trace(go.Scatter(x=df_country['Year'], y=df_country['Predicted_Loss'], mode='lines', name='Model Trend (Historical)', line=dict(color=COLOR_LIME)))
fig1.add_trace(go.Scatter(x=df_future['Year'], y=df_future['Predicted_Loss'], mode='lines+markers', name='Forecast (2021-2030)', line=dict(color='#386629', dash='dash')))

fig1.update_layout(title="Actual vs Predicted & Forecasted Forest Loss", xaxis_title="Year", yaxis_title="Loss (ha)")
fig1 = apply_chart_theme(fig1)
st.plotly_chart(fig1, use_container_width=True)

# 2. Prediction Error
st.subheader("2. Prediction Error (Residuals) :material/bar_chart:")
fig2 = px.bar(df_country, x='Year', y='Residual_Error',
              color_discrete_sequence=[COLOR_GREEN],
              labels={'Residual_Error': 'Error (Actual - Predicted)'},
              title="Model Residual Error per Year")
fig2 = apply_chart_theme(fig2)
st.plotly_chart(fig2, use_container_width=True)