from urllib2 import urlopen
from bs4 import BeautifulSoup
from threading import  Thread

def gen_names():
    f = open("package_names",'w')
    
    page = urlopen("http://hackage.haskell.org/packages/")
    soup = BeautifulSoup(page)
    package_sections = soup.findAll("ul",attrs={"class":"packages"})
    for package_section in package_sections:
        package_rows = section.findAll("li")
        for package_row in package_rows:
            f.write( package_row.a.string + "\n")

    f.close()
    

    

def consstruct_edgelist(input_char):
    
    f = open("data/"+input_char+"_input",'r')
    h = open("data/"+input_char+"_output",'w')
    
    for line in f.readlines():
        try:

            name = line.strip()
            reqlist = name

            page = urlopen("http://hackage.haskell.org/package/"+name+"/dependencies")
            soup = BeautifulSoup(page)
            tables = soup.findAll("div",attrs={"id":"detailed-dependencies"})
            for table in tables:
                dependencies = table.findAll("li")
                for dependency in dependencies:
                    if dependency.a != None:
                        reqlist += " "+ (dependency.a.string)
            h.write(reqlist + "\n")

        except Exception,err:
            print line.strip().split(",")[0],err
            h.write(reqlist+" "+str(err)+"\n")

    f.close()
    h.close()


if __name__ == '__main__':
    seq = range(5)
    for number in seq:
        t = Thread(target = contruct_edgelist,args=(str(number),))                                                                                                           
        t.start()