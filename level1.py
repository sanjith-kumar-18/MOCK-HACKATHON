import json

level1=open("Inputdata\level1a.json")

data=json.load(level1)

distances=[] # to convet a json data to a 2D -list

restaurants=[]
for i in data['restaurants']['r0']['neighbourhood_distance']:
    restaurants.append(i)

for j in data["neighbourhoods"]:

    neighborhood_Distance=[]

    for i in data['neighbourhoods'][j]['distances']:
        #print(i) # printing distances
        neighborhood_Distance.append(i)
    #print('\n')
    distances.append(neighborhood_Distance)
    #print(distances)
#
untained_distances=distances.copy()
order_quantity=[]

for i in data["neighbourhoods"]:
    order_quantity.append(data["neighbourhoods"][i]["order_quantity"])
print(order_quantity)
#print(sum(order_quantity))

print(restaurants)
print("\n")
for i in range(0,len(distances)):
    distances[i].insert(0,restaurants[i])
restaurants.insert(0,0)
distances.insert(0,restaurants)
"""
for i in range(len(distances)):
    print(distances[i])
"""
