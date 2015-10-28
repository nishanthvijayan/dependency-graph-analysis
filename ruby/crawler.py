from urllib2 import urlopen
import json
from threading import  Thread
from time import time

def crawl(input_char):
    
    f = open("data/input/"+input_char+"_input",'r')
    h = open("data/output/"+input_char+"_output",'a')
    log = open("log",'a')

    time1 = time()
    counter = 0

    for line in f.readlines():
        gem_name = line.strip("\n")
        req_list = gem_name
        counter += 1
        try:
            page = urlopen("https://rubygems.org/api/v1/gems/"+gem_name+".json")
            req = json.load(page)["dependencies"]["runtime"]
            for item in req: req_list += " "+(item["name"])
            h.write(req_list+"\n")
        except Exception,err:
            print gem_name,err
            h.write(req_list+" "+str(err)+"\n")
    h.close()
    f.close()

    time2 = time()
    total_time = time2- time1
    log.write(input_char+" "+str(int(total_time))+" "+str(counter)+'\n')
    log.close()

seq = list("bdefg")
for letter in seq:
    t = Thread(target = crawl,args=(letter,))                                                                                                           
    t.start()