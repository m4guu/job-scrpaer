import dash
from dash import html, dcc, dash_table
from io import StringIO

import pandas as pd
import plotly.express as px

from ...database import get_today_jobs, save_statistics
from ...functions import generate_todays_basic_statistics, apply_common_layout

dash.register_page(__name__)

# DATA
df = pd.DataFrame(generate_todays_basic_statistics(get_today_jobs()))
fig = px.bar(
    df,
    x="Job Board",
    y="Job Count",
    title="number of ads depending on the Platform".upper(),
    barmode="group",
)
fig = apply_common_layout(fig)

# SAVE STATISTICS TO DATABASE
csv_data = StringIO()
df.to_csv(csv_data, index=False)
csv_data.seek(0)
save_statistics(csv_data)

# LAYOUT
layout = html.Div(
    children=[
        html.H1(className="dashboard-title", children="CHART"),
        dcc.Graph(figure=fig),
        html.H1(className="dashboard-title", children="TABLE"),
        dash_table.DataTable(
            columns=[{"name": col, "id": col} for col in df.columns],
            style_cell={"textAlign": "left"},
            style_header={
                "backgroundColor": "#252529",
                "color": "#10b981",
                "border": "2px solid rgba(82, 82, 89, 0.32)",
                "fontWeight": "bold",
            },
            style_data={
                "backgroundColor": "#252529",
                "border": "2px solid rgba(82, 82, 89, 0.32)",
                "color": "rgb(255, 255, 245, 0.86)",
            },
            data=df.to_dict("records"),
        ),
    ]
)
