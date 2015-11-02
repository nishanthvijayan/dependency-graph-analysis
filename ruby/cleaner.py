from urllib2 import urlopen
import json

def combine():
    f = open("data/edge_list",'w')

    seq = list("abcdefghijklmnopqrstuvwxyz0")
    for letter in seq:
        h = open("data/output/"+letter+"_output",'r')
        for line in h.readlines():
            if "Err" not in line:
                f.write(line)
        f.write("\n")

def fixer():
    h = open("data/edge_list",'a')
    f = open("log",'r')

    for line in f.readlines():
        gem_name = line.strip("\n").split()[0]
        print gem_name
        req_list = gem_name
        try:
            page = urlopen("https://rubygems.org/api/v1/gems/"+gem_name+".json")
            req = json.load(page)["dependencies"]["runtime"]
            for item in req: 
                if item["name"]!=None:
                    req_list += " "+(item["name"])
            h.write(req_list+"\n")
        except Exception,err:
            print gem_name,err
            h.write(req_list+" "+str(err)+"\n")
    h.close()
    f.close()

fixer()