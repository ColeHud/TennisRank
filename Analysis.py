import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import json
from pprint import pprint

#open match data from json
with open('data.json') as data_file:    
    data = json.load(data_file)
pprint(data)
matches = data["matches"]

#find all unique players from data
nodes = []
for match in matches:
	if match["winner"] not in nodes:
		nodes.append(match["winner"])
	if match["loser"] not in nodes:
		nodes.append(match["loser"])

#create graph
G = nx.DiGraph()

#add nodes
for player in nodes:
	G.add_node(player)

#add edges
for match in matches:
	loser = match["loser"]
	winner = match["winner"]

	edgeData = G.get_edge_data(loser, winner)

	if edgeData:
		G.add_edge(loser, winner, weight=(1+edgeData['weight'])) 
	else:
		G.add_edge(loser, winner, weight=1)  #edge from loser to winner

#pagerank
pr = nx.pagerank(G, alpha=0.9)
pprint(pr)

#do a naive sort on the pagerank      SWITCH TO SOMETHING LIKE MERGESORT LATER
pagerankList = []
while len(pr) > 0:
	largestPagerank = 0
	playerWithLargestPagerank = ""
	for player in pr:
		pagerank = pr[player]
		if pagerank > largestPagerank:
			largestPagerank = pagerank
			playerWithLargestPagerank = player

	del pr[playerWithLargestPagerank]
	pagerankList.append(playerWithLargestPagerank)

#print ranked list
print "Ranked Players:"
for player in pagerankList:
	print player

#print
nx.draw(G, with_labels=True)
plt.show()

