from pkg_resources import *
import networkx as nx
import matplotlib.pyplot as plt

pkgs = []
f = open("req.txt",'r')
for line in f.readlines():
	a,b = line.strip().split('==')
	pkgs.append(a)
f.close()

G = nx.DiGraph()

print "Number of libraries",len(pkgs)

for pkg in pkgs:
	try:
		deps = require(pkg)
		for dep in  deps:
			name = str(dep).split()[0]
			G.add_edge(pkg,name)	
	except:
		print pkg
		pass
	
	
print "Number of nodes in graph",len(G.nodes())	

nx.write_graphml(G,'so.graphml')