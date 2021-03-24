import sys # lets program read in items from system arguments
import json #library for working with json

newJson = {}
def main(data,val =""):
    start = "" #defines a str to add to start of key
    if val!="":  
        start = val+'.'
    for i in data :
        if(isinstance(data[i], dict )):
            main(data[i],i )
        else:
            newJson[start+i] = data[i]

file = ""
#opens the file
if len(sys.argv)>=2 : 
    file =open(sys.argv[1]) 
else : 
    file = open("input.json")
#loads the  data from the file and structures it as a dictionary
data = json.loads(file.read())
#calls method with json from input file
main(data)
#prints the new dictionary/json
print(newJson)
#closes the input file
file.close()
#get output file
if len(sys.argv)>=3:
    file = open(sys.argv[2], "w")
else:
    file = open("newOutput.json", "w")
#write to output file using the populated dictionary
file.write(json.dumps(newJson, indent=5))
#closes the file
file.close()
