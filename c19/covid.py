import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

read=pd.read_csv("cdata.csv")
read=read[
    [
        "Province_State",
        "Country_Region",
        "Last_Update",
        "Lat",
        "Long_",
        "Confirmed",
        "Recovered",
        "Deaths",
        "Active"
    ]
]
#renaming colums
read.columns=["state","country","update","lat","long","confirmed","recovered","deaths","active"]
#filling misssing values
read["state"].fillna("",inplace=True)
print(read.head())
print(read.info())
top10=(read.groupby("country")["confirmed"].sum().nlargest(10).sort_values(ascending=False))
#bubbleplot
plot=px.scatter(x=top10.index,y=top10.values,size=top10.values,color=top10.index,size_max=120,title="Confirmed total cases")
plot.write_html("plot1.html",auto_open=True)
#top 10 countires by death
top10=(read.groupby("country")["deaths"].sum().nlargest(10).sort_values(ascending=False))
#bubbleplot
plot=px.scatter(x=top10.index,y=top10.values,size=top10.values,color=top10.index,size_max=120,title="Confirmed total deaths")
plot.write_html("plot1.html",auto_open=True)
#top10 recovery
top10=(read.groupby("country")["recovered"].sum().nlargest(10).sort_values(ascending=False))
#bubbleplot
plot=px.scatter(x=top10.index,y=top10.values,size=top10.values,color=top10.index,size_max=120,title="Confirmed total recpvery")
plot.write_html("plot1.html",auto_open=True)