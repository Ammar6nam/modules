import json

with open('personal1.json','r') as open2:
    contentfile=open2.read()
    read2=json.loads(contentfile)

with open ('personal1.json','r') as open3:
    read3=json.load(open3)
    
print("Reading json file...")
print (read2,read3,sep='\n')
print("Finished reading json file...")





# import json as js
# with  open('personal.json') as openfile2:
#     read2=js.load(openfile2)
#     print(read2)
# '''The different between loads and load:
# loads: it pass to json string and converts 
# the data to paythonic form of data structure.
# load: it pass to the json file itself
# '''
# print (type(read2))