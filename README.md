# JSONParser

by Ellen O Leary

### Requirements
You will need Python installed. I used python3 with this project.

### Set up
1. Clone repositry and move to cloned File in terminal
2. Run script<br />  

For this script you can specify the either the input json file or the output json file as well. You can also leave the arguments blank and teh file will you the input file supplied in the repository.
Here are the example 
```
python3 JSONParser.py "input json file"
python3 JSONParser.py "input json file" "output json file"
python3 JSONParser.py
```
#### Description
This project deconstructs a json that is supplied to the programme. I will break down any array that the json contains and write it to a file with the array key and inner array key deconstructed. For example, this is the input2.json file:

```
{
    "a": 1,
    "b": true,
    "c": {
        "d": 3,
        "e": "test"
    },
   "f" : false,
   "g" : {
        "h": "word",
	      "i": 7
   }
}
```

Once this is run through the program we can see the arrays hae been deconscructed. We can also see this in output2.json

```
{
     "a": 1,
     "b": true,
     "c.d": 3,
     "c.e": "test",
     "f": false,
     "g.h": "word",
     "g.i": 7
}
```
