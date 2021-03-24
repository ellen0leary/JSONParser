import sys # lets program read in items from system arguments
import json #library for working with json

newJson = {}
def main(data,val =""):
    start = ""
    if val!="": 
        start = val+'.'
    for i in data :
        if(isinstance(data[i], dict )):
            main(data[i],i )
        else:
            newJson[start+i] = data[i]

f = open(sys.argv[1]) # open the file
data = json.loads(f.read())
main(data)
print(newJson)
f.close()
f = open("output.json", "w")
f.write(json.dumps(newJson))
f.close()
