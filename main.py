import json
import itertools
import random

def held_karp(dists):
    
    n = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    return opt, list(reversed(path))


level0=open("Inputdata\level0.json") 
# json data has been read



data=json.load(level0) 
#json file has been loaded to the data

distances=[] # to convet a json data to a 2D -list
#restaurants=[]
restaurants=[]
for i in data['restaurants']['r0']['neighbourhood_distance']:
    restaurants.append(i)
restaurants.insert(0,0)
distances.append(restaurants)

for j in data["neighbourhoods"]:

    neighborhood_Distance=[]

    for i in data['neighbourhoods'][j]['distances']:
        #print(i) # printing distances
        neighborhood_Distance.append(i)
    #print('\n')
    distances.append(neighborhood_Distance)
    #print(distances)
#
for i in range(1,len(distances)):
    distances[i].insert(0,restaurants[i-1])
#restaurants.append(0)
#distances.append(restaurants)
"""
for i in range(len(distances)):
    print(distances[i])
"""
output=held_karp(distances)
#output=(8731,[0,14,9,4,17,2,19,3,15,10,13,11,16,5,18,20,8,7,6,12,1])
path=output[1]
output_path=[]
for i in range(len(path)):
    if path[i]==0:
        output_path.append("r0")
    elif path[i]==1:
        output_path.append("n0")
    elif path[i]==2:
        output_path.append("n1")
    elif path[i]==3:
        output_path.append("n2")
    elif path[i]==4:
        output_path.append("n3")
    elif path[i]==5:
        output_path.append("n4")    
    elif path[i]==6:
        output_path.append("n5")    
    elif path[i]==7:
        output_path.append("n6")    
    elif path[i]==8:
        output_path.append("n7")    
    elif path[i]==9:
        output_path.append("n8")    
    elif path[i]==10:
        output_path.append("n9")    
    elif path[i]==11:
        output_path.append("n10")    
    elif path[i]==12:
        output_path.append("n11")    
    elif path[i]==13:
        output_path.append("n12")    
    elif path[i]==14:
        output_path.append("n13")    
    elif path[i]==15:
        output_path.append("n14")    
    elif path[i]==16:
        output_path.append("n15")    
    elif path[i]==17:
        output_path.append("n16")    
    elif path[i]==18:
        output_path.append("n17")    
    elif path[i]==19:
        output_path.append("n18")    
    elif path[i]==20:
        output_path.append("n19")
    else:
        print("0")
output_path.append("r0")
value=output[0]    
dct={"v0":{"path":output_path}}
print(dct)
with open("level0_output.json",'w') as write_file:
    json.dump(dct,write_file)   
    

#file1=open("Test.txt","w")
#file1.writelines(str(distances))
#file1.close
#print("Written") 
