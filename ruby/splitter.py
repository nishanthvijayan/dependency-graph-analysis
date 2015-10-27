f = open("gem_names",'r')
for line in f.readlines():
    gem_name = line.split()[0]

    if gem_name[0].isalpha():
        h = open('data/input/'+gem_name[0].lower()+'_input','a+')
        h.write(gem_name+"\n")
    else:
        h = open('data/input/symbol_input','a+')
        h.write(gem_name+"\n")
    h.close()
f.close()