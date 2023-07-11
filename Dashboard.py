import dash
import dash_html_components as html

app = dash.Dash(__name__)
server = app.server

# Create the layout
app.layout = html.Div([
    html.H1('Dashboard'),
    html.Iframe(
        src="<https://app.powerbi.com/reportEmbed?reportId=42540ef2-36bb-41dc-a02c-b428da54e322&autoAuth=true&ctid=401c0fa2-ef1c-4c22-8636-c8f8ecbc97d6>",
        style={'width': '100%', 'height': '600px', 'border': 'none'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
