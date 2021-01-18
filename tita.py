#print("Code for Tita")
#=============Test code=======================
# txt = 'ConnellyRapids down=SummerMall\nPredovicPark up=LewisFalls right=SydnieManor\nQuigleyPrairie up=ReedLights right=HilllTunnel'
# txt = 'ConnellyRapids down=SummerMall'
# txt = 'PredovicPark up=LewisFalls right=SydnieManor'

# maps = {} # create maps dict

# address, direction = txt.strip().split(' ', 1) # split data of from db to address and direction

# direction_array = direction.split(' ') # split the direction into array
# print(direction_array)

# direction_dict = {} # declare direction dictionary
# #split the direction array by '='. Then make the first part dictionary key and 2nd part dict value 
# for dir in direction_array:
#   dir_key,dir_value = dir.split('=')
#   direction_dict[dir_key] = dir_value
# #print(direction_dict)

# maps[address] = direction_dict # Make the address as key and direction as value in the Map dictionary
# print(maps) #print dictionary
# print(len(maps)) #print length of map dictionary

#=============test Code end======================================

#============Working===============

# import json
# # from collections import OrderedDict # for orderedDict

# filename = 'location_db_few.txt'

# maps = {} # create maps dict
# #maps = OrderedDict() # create maps dict - Ordered. Used to ensure that first item enter is first on list

# with open(filename) as fh:
#     for line in fh:
#         address, direction = line.strip().split(' ', 1) # split data of from db to address and direction

#         direction_array = direction.split(' ') # split the direction into array

#         direction_dict = {} # declare direction dictionary
#         direction_dict['name']= address 
#         #split the direction array by '='. Then make the first part dictionary key and 2nd part dict value 
#         for dirc in direction_array:
#           dir_key,dir_value = dirc.split('=')
#           direction_dict[dir_key] = dir_value
        
#         maps[address] = direction_dict # Make the address as key and direction as value in the Map dictionary

# # print(json.dumps(maps, indent=2, sort_keys=True))
# print(len(maps))

# # x = maps['DustyViaduct']
# # print(x)

# for dict_objects in maps.values():
#   print(dict_objects)
#   for key in dict_objects:
#     print("Key: " + key + "\nvalue: " + dict_objects[key])

#===============end working================


#======USE THIS!!!!=====
import json
from collections import OrderedDict # for orderedDict

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

#Print the List (with Dict inside). Using indent for good visibility
#print(json.dumps(maps, indent=2))
print(len(maps))

# x = maps['DustyViaduct']
# print(x)

# for dict_objects in maps.values():
#   #print(dict_objects)
#   for key in dict_objects:
#     #print("Key: " + key + "\nvalue: " + dict_objects[key])
#=================



#==========not working===============
# import json
# from collections import OrderedDict # for orderedDict

# filename = 'location_db_few.txt'


# maps = []
# locations = {}
# #locations = OrderedDict() # Used to ensure that "name" comes up first


# with open(filename) as fh:
#   for line in fh:
#     address, direction = line.strip().split(' ', 1) # split data of from db to address and direction
#     name = "name"
#     locations[name] = address

#     direction_array = direction.split(' ') # split the direction into array

#     # split the direction array by '='. Then make the first part dictionary key and 2nd part dict value 
#     # for dirc in direction_array:
#     #   dir_key,dir_value = dirc.split('=')
#     #   locations[dir_key] = dir_value
    
#     maps.append(locations)
#     # print(json.dumps(locations, indent=2, sort_keys=True)) # sort_keys will put the dictioney keys out of required order
#     #print(json.dumps(locations, indent=2))
    
#     #print(json.dumps(locations, indent=2))
#     #print(json.dumps(maps, indent=2))
#   #maps.append(locations)
#==========================================

# =================trying again==================

# import json


# filename = 'location_db.txt'

# maps = {} # create maps dict


# with open(filename) as fh:
#     for line in fh:
#         address, direction = line.strip().split(' ', 1) # split data of from db to address and direction

#         direction_array = direction.split(' ') # split the direction into array

#         direction_dict = {} # declare direction dictionary
#         #split the direction array by '='. Then make the first part dictionary key and 2nd part dict value 
#         for dirc in direction_array:
#           dir_key,dir_value = dirc.split('=')
#           direction_dict[dir_key] = dir_value
#         direction_dict['name']= address
#         maps[address] = direction_dict # Make the address as key and direction as value in the Map dictionary

# #print(json.dumps(maps, indent=2, sort_keys=True))

# print(len(maps))






#==============find in Dict==============


# #===== Get Value from Key====
# for key, value in maps[0].items():
#   if value== 'ConnellyRapids':
#     print("This is key: " + key + "\nThis is value: " + value)
#     print(json.dumps(maps[0], indent=2))


#========check with function
def check_key(val):
  uio = []
  for n in range(len(maps)):
    #print(n)
    you = OrderedDict()
    for key, value in maps[n].items():
      # Use this is you want report of all record with the location
      # if (value == val):
      if (key == 'name' and value == val):
          #return maps[n]
          uio.append(maps[n])
  if not uio:
    t = {"404 Error": "Record does not Exist"}
    uio.append(t)

  return uio

check = check_key('BaumbahExpressway')
print(json.dumps(check, indent=2))


# def check_key(val):
#   for n in range(len(maps['map'])):
#     #print(n)
#     for key, value in maps['map'][n].items():
#       if val == value:
#           return maps['map'][n]

#   return "key doesn't exist"


#check = check_key('ArturoCourse')
#check = check_key('HalvorsonLand')
#print(json.dumps(check, indent=2))

#print(maps['map'][9].items())

# #Count Dictionary
# for n in range(len(maps['map'])):
#   print(n)

# ====================================
# d1 = {"name":"EsperanzaInlet","down":"HandWalks","up":"HarveyStreet","right":"KubForges","left":"RandallExtension"}
# d2 = {"name":"OletaDrive","down":"FavianPrairie","up":"AntonettaLocks","right":"LethaHill","left":"RandallExtension"}

# d = []
# #print(d1)
# #print(d2)
# d.append(d1)
# #print(json.dumps(d, indent=2))
# d.append(d2)
# #print(json.dumps(maps, indent=2))