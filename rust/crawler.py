from urllib2 import urlopen
import json

def gen_names():
    f = open("crates_names",'a')
    for page in range(1,34):
        page = urlopen("https://crates.io/api/v1/crates?page="+str(page)+"&per_page=100")
        crates = json.load(page)["crates"]
        for crate in crates:
            f.write(crate["name"]+","+crate["max_version"]+","+str(crate["downloads"])+"\n")
    f.close()

def construct_edgelist():
    h = open("edge_list",'a')
    f = open("crates_names",'r')
    for line in f.readlines():
        try:
            name = line.strip().split(",")[0]
            version = line.strip().split(",")[1]
            reqlist = name

            page = urlopen("https://crates.io/api/v1/crates/"+name+"/"+version+"/dependencies")
            dependencies = json.load(page)["dependencies"]
            for dependency in dependencies:
                reqlist += " "+dependency["crate_id"]
            h.write(reqlist + "\n")
        except Exception,err:
            print line.strip().split(",")[0],err
    h.close()
    f.close()


if __name__ == '__main__':
    contruct_edgelist()