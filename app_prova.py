import dash
from dash import html, dash_table
import pandas as pd
import os

# Dati della tabella
df = pd.DataFrame({
    "crlo": [1, 1, 1],
    "miro": [2, 2, 2],
    "ponio": [3, 3, 3]
})

# Crea l'app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H2("Tabella pubblica"),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_cell={'textAlign': 'center'}
    )
])

# Per render.com o esecuzione locale
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(port=port)

