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
def tops(countryname,n=5):
    countrydata=read[read["country"]==countryname]
    return countrydata.nlargest(n,"confirmed")
#usa state analysis
usas=tops("US")
figure=go.Figure()
figure.add_bar(name="confirmed",x=usas["confirmed"],y=usas["state"],orientation="h")
figure.add_bar(name="deaths",x=usas["deaths"],y=usas["state"],orientation="h")
figure.update_layout(title="most affected states in usa",barmode="group",height=600)
figure.write_html("hello.html",auto_open=True)

#india state analysis
indias=tops("India")
figure=go.Figure()
figure.add_bar(name="confirmed",x=indias["confirmed"],y=indias["state"],orientation="h")
figure.add_bar(name="deaths",x=indias["deaths"],y=indias["state"],orientation="h")
figure.update_layout(title="most affected states in india",barmode="group",height=600)
figure.write_html("Title.html",auto_open=True)

#calculating recovery rate and death rate
read["recover_rate"]=(read["recovered"]/read["confirmed"])*100

read["death_rate"]=(read["deaths"]/read["confirmed"])*100

recover_rate=(read.groupby("country")["recover_rate"].mean().nlargest(5))
print("top5 countries recovery rate")
print(recover_rate)

death_rate=(read.groupby("country")["death_rate"].mean().nlargest(5))
print("top5 countries death rate")
print(death_rate)

#global covid piechart
confirmedal=read["confirmed"].sum()
deathsall=read["deaths"].sum() 
recoveredall=read["recovered"].sum()
active=read["active"].sum()
pies=px.pie(names=["confirmed","deaths","recovered","active"],values=[confirmedal,deathsall,recoveredall,active],title="covid cases")
pies.write_html("covid-19.html",auto_open=True)





