import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# ------------------------------------------------------------------------------
# Create example figures (Placeholder data)
# ------------------------------------------------------------------------------

# 1. A sample gauge chart for "Load Maintenance"
load_maintenance_fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=65,  # placeholder load value
    title={'text': "Load Maintenance"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "royalblue"},
        'bgcolor': "white",
    }
))
load_maintenance_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

# 2. A sample gauge chart for "Surge/Drop Tracker"
surge_drop_fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=2,  # placeholder event count
    title={'text': "Surge Events"},
    gauge={
        'axis': {'range': [0, 10]},
        'bar': {'color': "red"},
    }
))
surge_drop_fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

# 3. A sample line chart for "Energy Demand"
time = pd.date_range("2025-01-01", periods=30, freq='D')
demand = np.random.randint(900, 1300, size=30)
energy_demand_fig = go.Figure(go.Scatter(
    x=time, y=demand, mode='lines+markers', name='Energy Demand',
    line=dict(color='cyan', width=2)
))
energy_demand_fig.update_layout(
    title="Energy Demand (Daily)",
    xaxis_title="Date",
    yaxis_title="Demand (kWh)",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

# 4. A sample bar chart for "Dynamic Pricing"
pricing_levels = ['Peak', 'Off-Peak', 'Shoulder']
prices = [0.25, 0.10, 0.18]  # $/kWh placeholders
dynamic_pricing_fig = go.Figure(go.Bar(
    x=pricing_levels, y=prices,
    marker_color=['red', 'green', 'orange']
))
dynamic_pricing_fig.update_layout(
    title="Dynamic Pricing",
    xaxis_title="Pricing Tier",
    yaxis_title="Price ($/kWh)",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="white"
)

# ------------------------------------------------------------------------------
# Create Cards (Placeholder Data)
# ------------------------------------------------------------------------------
# Each card can represent a particular metric or module.
card_style = {
    "backgroundColor": "#2a2a2a",
    "color": "white",
    "borderRadius": "10px",
    "margin": "10px"
}

card1 = dbc.Card([
    dbc.CardHeader("Predictive Maintenance", style={"backgroundColor": "#333333"}),
    dbc.CardBody([
        html.H4("Next Service: 02 Days", className="card-title"),
        html.P("Monitor critical assets for maintenance intervals."),
        dbc.Progress(value=40, color="warning", striped=True, animated=True, className="mb-2"),
        html.Small("Maintenance Completion: 40%")
    ])
], style=card_style)

card2 = dbc.Card([
    dbc.CardHeader("AI Analytics", style={"backgroundColor": "#333333"}),
    dbc.CardBody([
        html.H4("Inference Time: 02 ms", className="card-title"),
        html.P("Real-time anomaly detection and demand forecasting."),
        dbc.Progress(value=70, color="info", striped=True, animated=True, className="mb-2"),
        html.Small("Anomaly Probability: 30%")
    ])
], style=card_style)

card3 = dbc.Card([
    dbc.CardHeader("Load Balancing", style={"backgroundColor": "#333333"}),
    dbc.CardBody([
        html.H4("Grid Efficiency: 85%", className="card-title"),
        html.P("Dynamic load routing to optimize grid usage."),
        dbc.Progress(value=85, color="success", striped=True, animated=True, className="mb-2"),
        html.Small("Capacity Usage: 85%")
    ])
], style=card_style)

card4 = dbc.Card([
    dbc.CardHeader("Demand Response", style={"backgroundColor": "#333333"}),
    dbc.CardBody([
        html.H4("Active Sessions: 12", className="card-title"),
        html.P("User-based load shifting to reduce peak stress."),
        dbc.Progress(value=55, color="danger", striped=True, animated=True, className="mb-2"),
        html.Small("Peak Reduction: 45%")
    ])
], style=card_style)

# ------------------------------------------------------------------------------
# Dash App & Layout
# ------------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])
server = app.server  # for production deployments

app.layout = dbc.Container(fluid=True, children=[
    # Title / Header
    dbc.Row([
        dbc.Col(html.H1("Smart Grid Optimization Dashboard", 
                        style={"textAlign": "center", "marginTop": 20}), width=12)
    ]),

    # Row of Cards (Predictive Maintenance, AI Analytics, etc.)
    dbc.Row([
        dbc.Col(card1, md=3),
        dbc.Col(card2, md=3),
        dbc.Col(card3, md=3),
        dbc.Col(card4, md=3),
    ], style={"marginBottom": 30}),

    # Row of Graphs: left = Energy Demand, right = Dynamic Pricing
    dbc.Row([
        dbc.Col(dcc.Graph(figure=energy_demand_fig, style={"height": "400px"}), md=6),
        dbc.Col(dcc.Graph(figure=dynamic_pricing_fig, style={"height": "400px"}), md=6),
    ], style={"marginBottom": 30}),

    # Row of Gauges: left = Load Maintenance, right = Surge/Drop
    dbc.Row([
        dbc.Col(dcc.Graph(figure=load_maintenance_fig, style={"height": "400px"}), md=6),
        dbc.Col(dcc.Graph(figure=surge_drop_fig, style={"height": "400px"}), md=6),
    ], style={"marginBottom": 30}),
    
    # Footer or Additional Info
    dbc.Row([
        dbc.Col(html.Div("© 2025 Smart Grid Analytics | All rights reserved.",
                         style={"textAlign": "center", "marginBottom": 20}), width=12)
    ])
])

if __name__ == "__main__":
    app.run(debug=True)
