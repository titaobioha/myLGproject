import json
from flask import Flask, jsonify, render_template, request
from collections import OrderedDict # for orderedDict

app = Flask(__name__)


# get file
filename = 'location_db.txt'

# create "maps" List
maps = [] 

with open(filename) as fh:
    for line in fh:
        # Create maps direction details dictionary as Ordered. 
        # Used to ensure that first item entered is first on list
        direction_details = OrderedDict() 
        
        # split data of from db to address and direction
        address, direction = line.strip().split(' ', 1) 

        # split the direction into array
        direction_array = direction.split(' ') 

        # Assign key name to "address"
        direction_details['name']= address 
        
        # Assign directions to up, down, left and right as needed
        # split the direction array by '='. Then make the first part dictionary key and 2nd part dict value 
        for detail in direction_array:
          key,value = detail.split('=')
          direction_details[key] = value
        
        # Append the dictionary to the list
        maps.append(direction_details) # Make the address as key and direction as value in the Map dictionary

# Function to check for location value
def check_key(val):
  uio = []
  for n in range(len(maps)):
    #print(n)
    you = OrderedDict()
    for key, value in maps[n].items():
      # Use this if you want report of all records with the location (including directions)
      if (value == val):
      # Use this if you want records only with name of location
      #if (key == 'name' and value == val):
          #return maps[n]
          uio.append(maps[n])
  if not uio:
    t = {"404 Error": "Record does not Exist"}
    uio.append(t)

  return uio

@app.route('/')
def home():  
  return json.dumps(maps, indent=2)

@app.route('/count')
def count():  
  result = {
        "count": len(maps)
    }
  return jsonify(result)

@app.route('/search')
def search():  
  # get argument from the browser (search?location=??)
  location = request.args.get('location')

  return json.dumps(check_key(location), indent=2)

