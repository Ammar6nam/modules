myDict={'Name':'Ammar Nam',
        'address' : 'Germany',
        'date of birth' : 1991,
        'city' : 'Damascus',
        'country' : 'Syria',
        'Email' : 'Ammar.nam@hotmail.com',
        'phone number' : '01783315261'
        }

import json

write=open('personal.json','w')
jsonContent=json.dumps(myDict)
write.write(jsonContent)
print(jsonContent)