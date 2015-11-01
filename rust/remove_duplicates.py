f = open("edge_list",'r')
h = open("edge_list_cleaned",'w')
for line in f.readlines():
    h.write(line.split()[0]+" "+" ".join(list(set( line.split()[1:] ) )) + '\n')
f.close()
h.close()