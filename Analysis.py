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
	G.add_edge(match["loser"], match["winner"])

#pagerank
pr = nx.pagerank(G, alpha=0.85)
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

