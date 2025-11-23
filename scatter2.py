import matplotlib.pyplot as plt
#cat1 carbs
carbs=["bread","rice","pasta"]
calfood=[80,130,158]
carbsp=[3.5,2.7,6]
carbscolor="Yellow"

#cat2 protein
protein=["chicken","fish","eggs"]
calprotein=[165,206,70]
proteinp=[31,22,6]
proteincolor="Red"

#cat3 fruit
fruit=["Banana","Apple","Orange"]
calfruit=[105,95,70]
fruitp=[1.3,0.5,1.2]
fruitcolor="Blue"

#cat4 vegetable
vegetable=["Tomato","onion","lettuce"]
calvegetable=[22,40,15]
vegetablep=[1,1.1,1.4]
vegetablecolor="Green"

#plotting the graph

plt.figure(figsize=(10,7))
plt.scatter(calfood,carbsp,color=carbscolor,s=150,label="CARBS")
plt.scatter(calprotein,proteinp,color=proteincolor,s=150,label="PROTEIN")
plt.scatter(calfruit,fruitp,color=fruitcolor,s=150,label="FRUIT")
plt.scatter(calvegetable,vegetablep,color=vegetablecolor,s=150,label="VEGE")

#ADDING TEXT LABELS
for i in range(len(carbs)):
    plt.text(calfood[i],carbsp[i],carbs[i])
for i in range(len(protein)):
    plt.text(calprotein[i],proteinp[i],protein[i])
for i in range(len(fruit)):
    plt.text(calfruit[i],fruitp[i],fruit[i])
for i in range(len(vegetable)):
    plt.text(calvegetable[i],vegetablep[i],vegetable[i])
plt.xlabel("CALORIES")
plt.ylabel("PROTEIN")
plt.title("CALS VS PROTEIN")
plt.legend()
plt.show()