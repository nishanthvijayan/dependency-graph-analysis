from urllib2 import urlopen
import json
from threading import  Thread

def crawl(input_char):
    
    f = open("data/input/"+input_char+"_input",'r')
    h = open("data/output/"+input_char+"_output",'w')

    for line in f.readlines():
        gem_name = line.strip("\n")
        page = urlopen("https://rubygems.org/api/v1/gems/"+gem_name+".json")

        req = json.load(page)["dependencies"]["runtime"]
        req_list = gem_name
        for item in req: req_list += " "+(item["name"])
        h.write(req_list+"\n")

    h.close()
    f.close()

seq = list("yz")
for letter in seq:
    t = Thread(target = crawl,args=(letter,))                                                                                                           
    t.start()