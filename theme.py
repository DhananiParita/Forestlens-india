import plotly.io as pio

# Custom Palette Hex Codes
COLOR_GREEN = "#133215"
COLOR_LIME = "#92B775"
COLOR_BEIGE = "#F3E8D3"

# Categorical Palette for multi-line / multi-bar charts
COLOR_SEQUENCE = ["#133215", "#92B775", "#5C8D4B", "#386629", "#809A68"]

def apply_chart_theme(fig):
    """
    Applies custom palette colors and transparent backgrounds so charts 
    seamlessly adapt to both Streamlit Light and Dark modes.
    """
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="sans-serif", size=12),
        margin=dict(l=20, r=20, t=40, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    fig.update_xaxes(showgrid=True, gridcolor='rgba(128,128,128,0.2)', zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(128,128,128,0.2)', zeroline=False)
    return fig