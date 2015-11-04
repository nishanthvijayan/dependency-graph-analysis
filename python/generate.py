import json
from base64 import b64decode
import networkx as nx

def generator():
    f = open("pypi-deps.csv",'r')
    h = open("edge_list",'w')
    for line in f.readlines():
        try:
            package_name,package_version,package_dep_encoded = map(str,line.split("\t")) 
            dependencies =  " ".join(json.loads(b64decode(package_dep_encoded)))
            reqlist = package_name + " " + dependencies
            h.write(reqlist.replace("\n","") + "\n")
        except Exception,err:
            print line,err
        
    
    f.close()
    h.close()

def generator_given():
    data = []
    G=nx.Graph()
    with open('pypi-deps.csv', 'r') as file:
        for line in file:
            name, version, deps = line.split('\t')
            deps = json.loads(b64decode(deps))
            data+= [(name, version, deps)]

    for ex in data:
        name, version, deps = ex
        G.add_node("%s-%s" % (name.lower(), version))
        for dep in deps:
            if not '#' in dep: G.add_edge("%s-%s" % (name.lower(), version), dep.replace("\"", "").replace("\n", "").lower())

    nx.write_adjlist(G,"adj_list")

def remove_duplicates():
    f = open("edge_list",'r')
    h = open("edge_list_better",'w')
    li = []
    for line in f.readlines():
        name = line.split()[0]
        if name not in li:
            li.append(name)
            h.write(line)
    f.close()
    h.close()



if __name__ == '__main__':
    # generator_given()
    # generator()
    remove_duplicates()