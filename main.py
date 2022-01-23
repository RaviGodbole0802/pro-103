from turtle import title
from numpy import tile
import pandas as pd
import plotly_express as px

df = pd.read_csv("covid_casses.csv")

fig = px.scatter(df,x="date",y="cases",color="country",title="Covid data")

fig.show()