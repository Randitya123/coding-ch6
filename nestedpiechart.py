import matplotlib.pyplot as plt
outer=["Protein","carbs","sugar","fat","potassium"]
outersize=[130,75,0.5,75,3]
outercolor=["red","green","purple","orange","yellow"]
inner=["chicken","fish","eggs","bread","potato","pasta","cake","ice-cream","gulab jamun","cheese","oil","avacado","banana","coconut water","spinach"]
innercolor=["#03fc5e","#0352fc","#fcbe03","#d703fc","#039dfc","#fc3003","#fc035a","#7bfc03","#fc030b","#fc9d03","#03f8fc","#c6fc03","#d703fc","#38a15b","#6e310e"]
innersize=[62,50,18,30,25,20,0.1,0.2,0.3,10,28,37,0.840,1.2,0.960]
fig,ax=plt.subplots(figsize=(9,9))
#outerring
ax.pie(outersize,labels=outer,radius=1.3,colors=outercolor,startangle=90,wedgeprops=dict(width=0.3,edgecolor='white'))
#innnerring
ax.pie(innersize,labels=inner,radius=0.9,colors=innercolor,startangle=90,wedgeprops=dict(width=0.3,edgecolor='white'))
plt.title("FOOD AND DIET")
plt.show()
