{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d75bd5f2-e9a9-4ef2-80ac-bc8f45fdf91e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "\n",
       "        <iframe\n",
       "            width=\"100%\"\n",
       "            height=\"650\"\n",
       "            src=\"http://127.0.0.1:8050/\"\n",
       "            frameborder=\"0\"\n",
       "            allowfullscreen\n",
       "            \n",
       "        ></iframe>\n",
       "        "
      ],
      "text/plain": [
       "<IPython.lib.display.IFrame at 0x282a0ada660>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import dash\n",
    "from dash import html, dash_table\n",
    "import pandas as pd\n",
    "\n",
    "# Dati della tabella\n",
    "df = pd.DataFrame({\n",
    "    \"crlo\": [1, 1, 1],\n",
    "    \"miro\": [2, 2, 2],\n",
    "    \"ponio\": [3, 3, 3]\n",
    "})\n",
    "\n",
    "# Crea l'app\n",
    "app = dash.Dash(__name__)\n",
    "app.layout = html.Div([\n",
    "    html.H2(\"Tabella pubblica\"),\n",
    "    dash_table.DataTable(\n",
    "        data=df.to_dict('records'),\n",
    "        columns=[{\"name\": i, \"id\": i} for i in df.columns],\n",
    "        style_cell={'textAlign': 'center'}\n",
    "    )\n",
    "])\n",
    "\n",
    "# Modifica per Render\n",
    "if __name__ == \"__main__\":\n",
    "    import os\n",
    "    port = int(os.environ.get(\"PORT\", 8050))\n",
    "    app.run(port=port)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7491de57-b809-46d6-9d9b-abac4931c2ab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
