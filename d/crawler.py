from urllib2 import urlopen
from bs4 import BeautifulSoup

def gen_names():
    f = open("package_names",'w')
    
    page = urlopen("http://code.dlang.org/?sort=updated&category=library")
    soup = BeautifulSoup(page)
    package_rows = soup.findAll("tr")[1:]
    for row in package_rows:
        f.write( row.td.a.string + "\n")
    f.close()
    

def contruct_edgelist():
    h = open("edge_list",'w')
    f = open("package_names",'r')
    
    for line in f.readlines():
        try:

            name = line.strip()
            reqlist = name

            page = urlopen("http://code.dlang.org/packages/"+name)
            soup = BeautifulSoup(page)
            table = soup.findAll("table")[0]
            rows = table.findAll("td")
            dependencies =  rows[len(rows)-1].findAll('a')
            
            for dependency in dependencies:
                reqlist += " "+ (dependency.string)
            h.write(reqlist + "\n")

        except Exception,err:
            print line.strip().split(",")[0],err
            h.write(req_list+" "+str(err)+"\n")

    f.close()
    h.close()


if __name__ == '__main__':
    contruct_edgelist()