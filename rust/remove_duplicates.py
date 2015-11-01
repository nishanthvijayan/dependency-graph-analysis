f = open("edge_list",'r')
h = open("edge_list_cleaned",'w')
for line in f.readlines():
    h.write(" ".join((list(set( line.split() ) ) )) + "\n")
f.close()
h.close()