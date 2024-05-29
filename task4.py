import json as js

with open ('personal.json','r') as openfile3:
    file3content=openfile3.read()
    read3=js.loads(file3content)
with open('personal1.json','w') as creatfile2:
    write2content=creatfile2.write(file3content)
    write2=js.dump(write2content,creatfile2)
    # 
'''
dumps(): it uses to serialize a Python object
(e.g., a dictionary) into a JSON-formatted string.
It does not write data to a file; it simply converts
a Python object to a JSON string, which can then be
used elsewhere or saved to a file using file I/O operations.
json.dump():is used to write a Python object 
(e.g., a dictionary) to a JSON file.
It takes two arguments: the Python object to be 
serialized and a file-like object
It writes the serialized JSON data directly to the 
specified file.
'''



print(read3)

# with open('personal2.json','r') as openfile4:
#     write2=js.dump(openfile4)
#     print(write2)

# # write1=json.dumps(jsonContent)

# jsonContent={"Name":"Ammar",
#         'address' : 'Germany',
#         'date of birth' : 1991,
#         'city' : 'Damascus',
#         'country' : 'Syria',
#         'Email' : 'Ammar.nam@hotmail.com',
#         'phone number' : '01783315261'
#         }

# import json
# dumps1=json.dumps(jsonContent)
# print(type(dumps1))
# open1=open('personal1.json','w')
# write1=open1.write(dumps1)
# print(dumps1)
