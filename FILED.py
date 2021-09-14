import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
a = px.scatter(df,x="country",y="date",color="country",size="cases")

a.show()